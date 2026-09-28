"""Strumenti ADB minimi e in SOLA LETTURA per il primo test con il telefono.

Nessuna funzione di questo file tocca lo schermo o modifica il telefono:
leggono stato, risoluzione, app in primo piano e fanno screenshot. I tocchi
restano nel bot, e passano sempre da ``MilitaryAdvisor.gate()``.

Richiede ``adb`` (Android Platform Tools) nel PATH del PC, oppure il percorso
in ADB_PATH. Sul telefono: Opzioni sviluppatore -> Debug USB attivo, e
accettare l'impronta del PC al primo collegamento.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Pacchetti noti di Rise of Kingdoms. Il primo è la versione Google Play;
# gli altri vengono cercati con "pm list packages" per le versioni di altri store.
ROK_PACKAGES = ["com.lilithgame.roc.gp"]
ROK_PACKAGE_HINTS = ("lilithgame.roc", "lilith.roc", "riseofkingdoms")


class AdbError(RuntimeError):
    pass


def adb_path() -> str:
    p = os.environ.get("ADB_PATH") or shutil.which("adb")
    if not p:
        raise AdbError(
            "adb non trovato. Installa Android Platform Tools "
            "(https://developer.android.com/tools/releases/platform-tools) "
            "e aggiungilo al PATH, oppure imposta ADB_PATH."
        )
    return p


def run(args: List[str], serial: Optional[str] = None, timeout: int = 20, binary: bool = False):
    cmd = [adb_path()] + (["-s", serial] if serial else []) + args
    try:
        res = subprocess.run(cmd, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise AdbError(f"timeout: {' '.join(args)}") from exc
    if res.returncode != 0:
        raise AdbError((res.stderr or res.stdout).decode(errors="replace").strip() or f"errore {res.returncode}")
    return res.stdout if binary else res.stdout.decode(errors="replace")


def shell(cmd: str, serial: Optional[str] = None, timeout: int = 20) -> str:
    return run(["shell", cmd], serial, timeout)


# ---------------------------------------------------------------- parsing
def parse_devices(out: str) -> List[Tuple[str, str]]:
    """'adb devices' -> [(serial, stato)], stato = device | unauthorized | offline"""
    devs = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 2:
            devs.append((parts[0], parts[1]))
    return devs


def parse_wm_size(out: str) -> Optional[Tuple[int, int]]:
    """'Physical size: 1080x2400\\nOverride size: ...' -> dimensione effettiva
    (l'override, se presente, è quella che vede il gioco)."""
    override = re.search(r"Override size:\s*(\d+)x(\d+)", out)
    physical = re.search(r"Physical size:\s*(\d+)x(\d+)", out)
    m = override or physical
    return (int(m.group(1)), int(m.group(2))) if m else None


def parse_density(out: str) -> Optional[int]:
    override = re.search(r"Override density:\s*(\d+)", out)
    physical = re.search(r"Physical density:\s*(\d+)", out)
    m = override or physical
    return int(m.group(1)) if m else None


def parse_focus(out: str) -> Optional[str]:
    """Estrae il pacchetto in primo piano da dumpsys window / activity."""
    for pat in (r"mCurrentFocus=Window\{[^}]*\s([\w.]+)/", r"mFocusedApp=.*?\s([\w.]+)/",
                r"mResumedActivity:.*?\s([\w.]+)/", r"topResumedActivity=.*?\s([\w.]+)/"):
        m = re.search(pat, out)
        if m:
            return m.group(1)
    return None


def parse_packages(out: str) -> List[str]:
    return [l.split(":", 1)[1].strip() for l in out.splitlines() if l.startswith("package:")]


# ------------------------------------------------------------ letture
def devices() -> List[Tuple[str, str]]:
    return parse_devices(run(["devices"]))


def pick_device() -> str:
    devs = devices()
    if not devs:
        raise AdbError("Nessun telefono collegato. Controlla cavo, Debug USB e 'adb devices'.")
    ready = [s for s, st in devs if st == "device"]
    if not ready:
        states = ", ".join(f"{s}={st}" for s, st in devs)
        raise AdbError(f"Telefono non autorizzato o offline ({states}). Sblocca il telefono e accetta la richiesta di debug USB.")
    return ready[0]


def rok_packages(serial: str) -> List[str]:
    pk = parse_packages(shell("pm list packages", serial))
    found = [p for p in pk if p in ROK_PACKAGES or any(h in p for h in ROK_PACKAGE_HINTS)]
    return found


def foreground_package(serial: str) -> Optional[str]:
    pkg = parse_focus(shell("dumpsys window | grep -E 'mCurrentFocus|mFocusedApp'", serial))
    if not pkg:
        pkg = parse_focus(shell("dumpsys activity activities | grep -E 'mResumedActivity|topResumedActivity'", serial))
    return pkg


def screen_on(serial: str) -> Optional[bool]:
    out = shell("dumpsys power | grep -E 'mWakefulness=|Display Power: state='", serial)
    if "mWakefulness=Awake" in out or "state=ON" in out:
        return True
    if "mWakefulness=" in out or "state=OFF" in out:
        return False
    return None


def screenshot(serial: str, dest: Path) -> Path:
    data = run(["exec-out", "screencap", "-p"], serial, timeout=30, binary=True)
    if not data.startswith(b"\x89PNG"):
        raise AdbError("screencap non ha restituito un PNG (schermo bloccato o protetto?)")
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return dest


def png_size(path: Path) -> Optional[Tuple[int, int]]:
    head = Path(path).read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def phone_report(out_dir: Path) -> Dict[str, object]:
    """Controllo completo in sola lettura. Non lancia eccezioni: ogni passo
    riporta ok/errore, così si vede subito dove si blocca."""
    rep: Dict[str, object] = {"steps": []}

    def step(name, fn):
        try:
            val = fn()
            rep["steps"].append({"step": name, "ok": True, "value": val})
            return val
        except Exception as exc:  # noqa: BLE001
            rep["steps"].append({"step": name, "ok": False, "error": str(exc)})
            return None

    step("adb installato", adb_path)
    serial = step("telefono collegato e autorizzato", pick_device)
    if not serial:
        return rep
    step("modello", lambda: shell("getprop ro.product.model", serial).strip())
    step("versione Android", lambda: shell("getprop ro.build.version.release", serial).strip())
    step("risoluzione", lambda: parse_wm_size(shell("wm size", serial)))
    step("densità", lambda: parse_density(shell("wm density", serial)))
    step("schermo acceso", lambda: screen_on(serial))
    pk = step("Rise of Kingdoms installato", lambda: rok_packages(serial) or None)
    fg = step("app in primo piano", lambda: foreground_package(serial))
    rep["rok_in_foreground"] = bool(pk and fg and fg in pk)
    shot = step("screenshot", lambda: str(screenshot(serial, Path(out_dir) / "screenshot_test.png")))
    if shot:
        step("dimensione screenshot", lambda: png_size(Path(shot)))
    return rep
