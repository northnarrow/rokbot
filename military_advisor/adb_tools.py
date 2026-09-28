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

# Il gioco forza l'orientamento orizzontale. Con il gioco davvero visibile lo
# screenshot è più largo che alto; uno screenshot verticale vuol dire che stiamo
# guardando la schermata di blocco o l'interfaccia di sistema.
# Misurato sul telefono di test (SM-S938B): gioco 1560x720, blocco 720x1560.


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


def keyguard_showing(serial: str) -> Optional[bool]:
    """True se la schermata di blocco sta coprendo lo schermo.

    Serve perché ``foreground_package`` da solo NON basta: con il telefono
    bloccato ``dumpsys window`` continua a riportare il gioco come finestra a
    fuoco. Verificato sul telefono di test il 28/09/2026 (test T16): schermo
    riacceso, ``mCurrentFocus`` ancora sul gioco, e intanto
    ``mDreamingLockscreen=true`` con la schermata di blocco davanti.

    Chi si fida solo del pacchetto in primo piano manda tocchi alla schermata
    di blocco credendo di parlare col gioco.
    """
    out = shell("dumpsys window | grep -E 'mDreamingLockscreen|mShowingLockscreen'", serial)
    for pat in (r"mDreamingLockscreen=(true|false)", r"mShowingLockscreen=(true|false)"):
        m = re.search(pat, out)
        if m:
            return m.group(1) == "true"
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


def game_visible(serial: str, out_dir: Path) -> Dict[str, object]:
    """Il controllo da fare PRIMA di mandare qualsiasi tocco.

    Mette insieme quattro segnali, perché nessuno da solo è affidabile:
    schermo acceso, schermata di blocco assente, pacchetto giusto in primo
    piano e soprattutto **screenshot orizzontale**. L'ultimo è quello che
    smaschera la schermata di blocco, che gli altri lasciano passare.

    Restituisce ``{'ok': bool, 'motivo': str, ...}``. Non solleva eccezioni:
    un errore diventa ``ok=False`` con il motivo scritto, così chi chiama può
    fermarsi invece di andare avanti alla cieca.
    """
    res: Dict[str, object] = {"ok": False, "motivo": "", "serial": serial}
    try:
        res["schermo_acceso"] = screen_on(serial)
        if res["schermo_acceso"] is False:
            res["motivo"] = "schermo spento"
            return res

        res["blocco"] = keyguard_showing(serial)
        if res["blocco"]:
            res["motivo"] = "schermata di blocco attiva: serve lo sblocco a mano"
            return res

        shot = screenshot(serial, Path(out_dir) / "_stato.png")
        size = png_size(shot)
        res["screenshot"] = str(shot)
        res["dimensione"] = size
        if not size:
            res["motivo"] = "screenshot illeggibile"
            return res
        if size[0] <= size[1]:
            res["motivo"] = (
                f"screenshot verticale {size[0]}x{size[1]}: il gioco non è visibile "
                "(schermata di blocco o interfaccia di sistema)"
            )
            return res

        fg = foreground_package(serial)
        res["primo_piano"] = fg
        if not fg or not (fg in ROK_PACKAGES or any(h in fg for h in ROK_PACKAGE_HINTS)):
            res["motivo"] = f"in primo piano c'è {fg or 'un pacchetto sconosciuto'}, non il gioco"
            return res

        res["ok"] = True
        res["motivo"] = "gioco visibile"
        return res
    except Exception as exc:  # noqa: BLE001
        res["motivo"] = f"controllo fallito: {exc}"
        return res


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
    step("schermata di blocco", lambda: keyguard_showing(serial))
    pk = step("Rise of Kingdoms installato", lambda: rok_packages(serial) or None)
    step("app in primo piano", lambda: foreground_package(serial))
    shot = step("screenshot", lambda: str(screenshot(serial, Path(out_dir) / "screenshot_test.png")))
    if shot:
        step("dimensione screenshot", lambda: png_size(Path(shot)))

    # Verdetto vero. Non basta confrontare il pacchetto in primo piano: con la
    # schermata di blocco attiva quello continua a dire "gioco". Vedi game_visible.
    verdetto = game_visible(serial, Path(out_dir))
    rep["steps"].append({"step": "gioco visibile", "ok": bool(verdetto["ok"]), "value": verdetto["motivo"], "error": verdetto["motivo"]})
    rep["rok_in_foreground"] = bool(verdetto["ok"])
    rep["motivo"] = verdetto["motivo"]
    return rep
