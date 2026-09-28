"""Strumenti per il client ufficiale di Rise of Kingdoms su Windows.

SOLA LETTURA: trova la finestra del gioco e ne salva uno screenshot.
Nessun clic e nessun tasto: i clic arrivano dopo, dal bot, e passano
sempre da ``MilitaryAdvisor.gate()``.

Dipendenze (solo sul PC Windows):  pip install mss pygetwindow
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Optional

WINDOW_HINTS = ("rise of kingdoms", "riseofkingdoms", "rok")


def _need(mod: str):
    try:
        return __import__(mod)
    except ImportError as exc:
        raise RuntimeError(f"manca il modulo '{mod}': esegui  pip install mss pygetwindow") from exc


def find_game_window():
    if sys.platform != "win32":
        raise RuntimeError("il client PC di Rise of Kingdoms gira su Windows: lancia questo comando sul PC")
    gw = _need("pygetwindow")
    wins = [w for w in gw.getAllWindows() if w.title and any(h in w.title.lower() for h in WINDOW_HINTS)]
    # "rok" è corto: preferisci i titoli che contengono il nome completo
    wins.sort(key=lambda w: ("rise of kingdoms" not in w.title.lower(), -w.width * w.height))
    if not wins:
        titles = [w.title for w in gw.getAllWindows() if w.title][:15]
        raise RuntimeError(f"finestra del gioco non trovata. Finestre aperte: {titles}")
    return wins[0]


def window_info(w) -> Dict[str, object]:
    return {"title": w.title, "left": w.left, "top": w.top, "width": w.width, "height": w.height,
            "minimized": bool(getattr(w, "isMinimized", False)), "active": bool(getattr(w, "isActive", False))}


def screenshot_window(w, dest: Path) -> Path:
    mss = _need("mss")
    import mss.tools  # noqa: F401
    if getattr(w, "isMinimized", False):
        raise RuntimeError("la finestra del gioco è ridotta a icona: riaprila (uno screenshot di una finestra ridotta è nero)")
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with mss.mss() as sct:
        box = {"left": w.left, "top": w.top, "width": w.width, "height": w.height}
        img = sct.grab(box)
        mss.tools.to_png(img.rgb, img.size, output=str(dest))
    return dest


def pc_report(out_dir: Path) -> Dict[str, object]:
    rep: Dict[str, object] = {"steps": []}

    def step(name, fn):
        try:
            val = fn()
            rep["steps"].append({"step": name, "ok": True, "value": val})
            return val
        except Exception as exc:  # noqa: BLE001
            rep["steps"].append({"step": name, "ok": False, "error": str(exc)})
            return None

    step("sistema Windows", lambda: sys.platform if sys.platform == "win32" else (_ for _ in ()).throw(
        RuntimeError("non sei su Windows")))
    step("moduli mss e pygetwindow", lambda: (_need("mss"), _need("pygetwindow")) and "ok")
    w = step("finestra del gioco", find_game_window)
    if w is None:
        return rep
    step("posizione e dimensioni", lambda: window_info(w))
    shot = step("screenshot della finestra", lambda: str(screenshot_window(w, Path(out_dir) / "pc_screenshot_test.png")))
    rep["ok"] = bool(shot)
    return rep
