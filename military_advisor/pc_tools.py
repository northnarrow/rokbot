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


def foreground(w) -> bool:
    return bool(getattr(w, "isActive", False))


def bring_to_front(w, attesa: float = 0.2, tentativi: int = 10) -> bool:
    """Porta davanti la finestra del gioco.

    È l'unico effetto di questo modulo sul sistema: cambia quale finestra ha il
    fuoco. Non manda nessun clic né tasto al gioco.
    """
    import time

    try:
        if getattr(w, "isMinimized", False):
            w.restore()
        w.activate()
    except Exception:  # noqa: BLE001
        # Su Windows activate() a volte viene rifiutato: il giro
        # riduci-e-ripristina di solito ottiene lo stesso risultato.
        try:
            w.minimize()
            w.restore()
        except Exception:  # noqa: BLE001
            pass
    for _ in range(tentativi):
        if foreground(w):
            return True
        time.sleep(attesa)
    return foreground(w)


def screenshot_window(w, dest: Path, richiedi_primo_piano: bool = True) -> Path:
    """Salva uno screenshot della finestra del gioco.

    ``mss`` cattura l'AREA DI SCHERMO occupata dalla finestra, non il contenuto
    della finestra: se davanti c'è dell'altro, nello screenshot finisce quello.
    Senza il controllo sul primo piano questa funzione restituisce felicemente
    l'immagine del terminale o del browser, e chi la chiama non se ne accorge.
    Verificato il 28/09/2026: con il gioco dietro, lo screenshot conteneva
    l'editor e il prompt dei comandi, mentre il controllo diceva OK.
    """
    mss = _need("mss")
    import mss.tools  # noqa: F401
    if getattr(w, "isMinimized", False):
        raise RuntimeError("la finestra del gioco è ridotta a icona: riaprila (uno screenshot di una finestra ridotta è nero)")
    if richiedi_primo_piano and not foreground(w):
        raise RuntimeError(
            "la finestra del gioco non è in primo piano: lo screenshot riprenderebbe "
            "quello che le sta davanti. Usa bring_to_front() prima di catturare."
        )
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with mss.mss() as sct:
        box = {"left": w.left, "top": w.top, "width": w.width, "height": w.height}
        img = sct.grab(box)
        mss.tools.to_png(img.rgb, img.size, output=str(dest))
    return dest


# ----------------------------------------------------------------- puntatore
# I clic usano coordinate RELATIVE alla finestra, cioe' le stesse che si
# leggono sullo screenshot salvato da screenshot_window(). Cosi' un punto
# misurato su un'immagine si puo' cliccare senza conversioni a mano, e resta
# valido anche se la finestra viene spostata.

_MOUSE_SINISTRO_GIU = 0x0002
_MOUSE_SINISTRO_SU = 0x0004
_MOUSE_ROTELLA = 0x0800


def _user32():
    import ctypes

    if sys.platform != "win32":
        raise RuntimeError("i clic sul client PC funzionano solo su Windows")
    return ctypes.windll.user32


def to_screen(w, x: int, y: int):
    """Da coordinate dello screenshot a coordinate dello schermo."""
    return w.left + int(x), w.top + int(y)


def _controlla(w, x: int, y: int) -> None:
    if not foreground(w):
        raise RuntimeError("la finestra del gioco non e' in primo piano: non clicco")
    if not (0 <= x < w.width and 0 <= y < w.height):
        raise RuntimeError(f"punto ({x}, {y}) fuori dalla finestra {w.width}x{w.height}: non clicco")


def click(w, x: int, y: int, attesa: float = 0.9) -> None:
    """Clic singolo dentro la finestra del gioco, in coordinate dello screenshot.

    Si rifiuta di cliccare se la finestra non e' davanti o se il punto cade
    fuori: un clic a vuoto fuori dalla finestra finirebbe su un'altra
    applicazione, e un clic mentre il gioco e' dietro non arriva al gioco.
    """
    import time

    _controlla(w, x, y)
    u = _user32()
    sx, sy = to_screen(w, x, y)
    u.SetCursorPos(sx, sy)
    time.sleep(0.05)
    u.mouse_event(_MOUSE_SINISTRO_GIU, 0, 0, 0, 0)
    time.sleep(0.05)
    u.mouse_event(_MOUSE_SINISTRO_SU, 0, 0, 0, 0)
    time.sleep(attesa)


def scroll(w, x: int, y: int, tacche: int, attesa: float = 0.6) -> None:
    """Rotella del mouse sul punto indicato. Tacche negative = verso il basso."""
    import time

    _controlla(w, x, y)
    u = _user32()
    sx, sy = to_screen(w, x, y)
    u.SetCursorPos(sx, sy)
    time.sleep(0.05)
    for _ in range(abs(tacche)):
        u.mouse_event(_MOUSE_ROTELLA, 0, 0, 120 if tacche > 0 else -120, 0)
        time.sleep(0.05)
    time.sleep(attesa)


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
    davanti = step("finestra in primo piano", lambda: bring_to_front(w) or (_ for _ in ()).throw(
        RuntimeError("non sono riuscito a portarla davanti: clicca tu sulla finestra del gioco e rilancia")))
    if not davanti:
        rep["ok"] = False
        return rep
    shot = step("screenshot della finestra", lambda: str(screenshot_window(w, Path(out_dir) / "pc_screenshot_test.png")))
    rep["ok"] = bool(shot)
    return rep
