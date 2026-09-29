"""Un solo modo di parlare al gioco, su telefono o su PC.

L'obiettivo del progetto e' un bot per **Android**. Il client PC e' servito
come banco di prova: schermo grande, finestra stabile, niente cavo. Ma la
logica scritta sopra pc_tools non gira sul telefono, e riscriverla due volte
significherebbe correggere ogni errore due volte.

Qui c'e' l'interfaccia comune. La logica - raccogliere, mandare marce,
leggere lo stato - parla solo con questa, e non sa su cosa sta girando.

Quello che si porta dietro dal lavoro sul PC:
  - il METODO: sonde di colore per riconoscere la schermata, OCR con
    ritaglio mirato per i numeri, verifica dopo ogni azione;
  - la CONOSCENZA del gioco: dove stanno le cose, cosa fa ogni pulsante,
    quali non vanno toccati mai.

Quello che NON si porta dietro sono le coordinate: il telefono e' 1560x720,
il PC 1796x1040, e non e' nemmeno una questione di scala perche' le
proporzioni sono diverse (2.17 contro 1.73). Ogni dispositivo ha il suo
file in riferimenti_ui/.
"""

from __future__ import annotations

import abc
import time
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image


class Dispositivo(abc.ABC):
    """Cosa serve saper fare per pilotare il gioco."""

    nome = "?"

    @abc.abstractmethod
    def dimensioni(self) -> Tuple[int, int]:
        """Larghezza e altezza dello spazio in cui valgono le coordinate."""

    @abc.abstractmethod
    def schermo(self, dove: Path) -> Image.Image:
        """Uno screenshot. Deve fallire, non mentire, se il gioco non si vede."""

    @abc.abstractmethod
    def tocca(self, x: int, y: int, attesa: float = 0.9) -> None:
        """Un tocco. Deve rifiutarsi se il punto cade fuori o il gioco non c'e'."""

    @abc.abstractmethod
    def trascina(self, x1: int, y1: int, x2: int, y2: int, ms: int = 600) -> None:
        """Una trascinata lenta: scorre le liste e sposta la telecamera."""

    @abc.abstractmethod
    def pronto(self, cartella: Path) -> Tuple[bool, str]:
        """(va bene?, perche'). Da chiamare prima di ogni ciclo."""

    def scorri(self, x: int, y: int, tacche: int, attesa: float = 0.6) -> None:
        """Scorrimento di una lista.

        Il PC ha la rotella; il telefono no, e usa una trascinata. Chi scrive
        la logica non deve saperlo, quindi il default e' la trascinata e il
        PC la sovrascrive.
        """
        L, A = self.dimensioni()
        passo = min(A // 3, 260)
        for _ in range(abs(tacche) // 3 + 1):
            dy = passo if tacche > 0 else -passo
            self.trascina(x, y, x, max(10, min(A - 10, y + dy)), 700)
        time.sleep(attesa)


class DispositivoPC(Dispositivo):
    """Il client ufficiale per Windows, pilotato con mouse e screenshot."""

    nome = "PC"

    def __init__(self):
        from . import pc_tools as P
        self._P = P
        self.w = P.find_game_window()
        if not P.bring_to_front(self.w):
            raise RuntimeError("non riesco a portare davanti la finestra del gioco")
        P.fissa_dimensioni(self.w)

    def dimensioni(self):
        return self.w.width, self.w.height

    def schermo(self, dove: Path) -> Image.Image:
        self._P.bring_to_front(self.w)
        return Image.open(self._P.screenshot_window(self.w, dove))

    def tocca(self, x, y, attesa=0.9):
        self._P.click(self.w, x, y, attesa)

    def trascina(self, x1, y1, x2, y2, ms=600):
        raise NotImplementedError("trascinata col mouse non ancora implementata sul PC")

    def scorri(self, x, y, tacche, attesa=0.6):
        self._P.scroll(self.w, x, y, tacche, attesa)

    def pronto(self, cartella: Path):
        try:
            im = self.schermo(cartella / "_pronto.png")
        except Exception as exc:  # noqa: BLE001
            return False, str(exc)
        return True, f"finestra {im.width}x{im.height}"


class DispositivoAndroid(Dispositivo):
    """Il telefono via ADB. E' il bersaglio vero del progetto."""

    nome = "Android"

    def __init__(self, serial: Optional[str] = None):
        from . import adb_tools as A
        self._A = A
        self.serial = serial or A.pick_device()
        self._dim: Optional[Tuple[int, int]] = None

    def dimensioni(self):
        if self._dim is None:
            # Il gioco forza l'orizzontale: 'wm size' dice 720x1560 ma lo
            # spazio in cui si tocca e' quello dello screenshot, 1560x720.
            p = Path("test_telefono/_dim.png")
            self._A.screenshot(self.serial, p)
            self._dim = self._A.png_size(p) or (1560, 720)
        return self._dim

    def schermo(self, dove: Path) -> Image.Image:
        return Image.open(self._A.screenshot(self.serial, dove))

    def _controlla(self, x, y):
        L, A = self.dimensioni()
        if not (0 <= x < L and 0 <= y < A):
            raise RuntimeError(f"punto ({x}, {y}) fuori dallo schermo {L}x{A}: non tocco")

    def tocca(self, x, y, attesa=0.9):
        self._controlla(x, y)
        self._A.shell(f"input tap {int(x)} {int(y)}", self.serial)
        time.sleep(attesa)

    def trascina(self, x1, y1, x2, y2, ms=600):
        self._controlla(x1, y1)
        self._controlla(x2, y2)
        self._A.shell(f"input swipe {int(x1)} {int(y1)} {int(x2)} {int(y2)} {int(ms)}",
                      self.serial)
        time.sleep(ms / 1000 + 0.4)

    def pronto(self, cartella: Path):
        v = self._A.game_visible(self.serial, cartella)
        return bool(v["ok"]), str(v["motivo"])


def apri(preferito: Optional[str] = None) -> Dispositivo:
    """Restituisce il dispositivo da usare.

    Di default prova prima il telefono, che e' il bersaglio del progetto, e
    ripiega sul PC solo se non c'e'.
    """
    ordine = [preferito] if preferito else ["android", "pc"]
    errori = []
    for nome in ordine:
        try:
            if nome == "android":
                return DispositivoAndroid()
            if nome == "pc":
                return DispositivoPC()
        except Exception as exc:  # noqa: BLE001
            errori.append(f"{nome}: {exc}")
    raise RuntimeError("nessun dispositivo disponibile -> " + "; ".join(errori))
