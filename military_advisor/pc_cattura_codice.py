"""Cattura il catalogo armamenti dalla schermata Codice del client PC.

SOLA LETTURA. Seleziona le voci del catalogo per leggerne il nome e scorre
l'elenco: non preme Fonte, Ricicla, Potenzia ne' nessun altro pulsante che
cambi qualcosa. Tutti i clic restano dentro il pannello di sinistra.

Da lanciare con il Codice gia' aperto:
    Menu -> Comandante -> icona Formazione -> CODICE

    python -m military_advisor.pc_cattura_codice

Produce in test_pc/codice/ un foglio per schermata: a sinistra il pannello
con i gruppi per formazione, a destra i nomi letti nello stesso ordine.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image

from . import pc_tools as P

DEST = Path("test_pc/codice")

# Pannello del catalogo, a sinistra. Tutti i clic stanno qui dentro.
PANNELLO = (20, 260, 350, 1035)
COLONNE = (64, 144, 223, 303)

# Nome dell'armamento selezionato, nel pannello di destra. Il riquadro parte
# alto perche' i nomi lunghi vanno a capo su due righe e la prima finirebbe
# tagliata (es. "Stendardo di battaglia del Nord").
NOME = (1420, 255, 1796, 358)

# Schede di rarita' in cima al pannello.
SCHEDE = {"Leggendario": (78, 282), "Epico": (184, 282), "Elite": (291, 282)}

# Sonda: il pulsante Fonte e' azzurro pieno solo su questa schermata.
SONDA_FONTE = (1520, 760, 1680, 800)

PUNTO_ROTELLA = (185, 700)


def _azzurro(rgb) -> bool:
    r, g, b = rgb
    return b > 200 and g > 140 and r < 60


def e_schermata_codice(im: Image.Image) -> bool:
    return _azzurro(P_media(im, SONDA_FONTE))


def P_media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def _arancione(rgb) -> bool:
    r, g, b = rgb
    return r > 140 and 60 < g < 190 and b < 110


def righe_voci(im: Image.Image) -> List[int]:
    """Trova le y delle righe di voci guardando la prima colonna.

    Le voci sono riquadri arancioni; intestazioni e sfondo no. Cosi' non si
    devono scrivere a mano le posizioni, che cambiano a ogni scorrimento.
    """
    dentro: List[int] = []
    for y in range(PANNELLO[1] + 20, PANNELLO[3] - 20, 4):
        if _arancione(P_media(im, (COLONNE[0] - 18, y - 6, COLONNE[0] + 18, y + 6))):
            dentro.append(y)
    righe, gruppo = [], []
    for y in dentro:
        if gruppo and y - gruppo[-1] > 12:
            righe.append(sum(gruppo) // len(gruppo))
            gruppo = []
        gruppo.append(y)
    if gruppo:
        righe.append(sum(gruppo) // len(gruppo))
    # scarta righe troppo vicine al bordo: sono voci tagliate a meta'
    return [y for y in righe if PANNELLO[1] + 40 < y < PANNELLO[3] - 40]


def foglio(pannello: Image.Image, nomi: List[Image.Image], dest: Path) -> Path:
    larghezza = pannello.width + (nomi[0].width if nomi else 0)
    altezza = max(pannello.height, sum(n.height for n in nomi) if nomi else 0)
    out = Image.new("RGB", (larghezza, altezza), (12, 12, 12))
    out.paste(pannello, (0, 0))
    y = 0
    for n in nomi:
        out.paste(n, (pannello.width, y))
        y += n.height
    out.save(dest)
    return dest


def main(argv: Optional[List[str]] = None) -> int:
    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1
    DEST.mkdir(parents=True, exist_ok=True)

    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra del gioco")
        return 1
    print(f"[OK ] finestra {P.fissa_dimensioni(w)[0]}x{P.fissa_dimensioni(w)[1]}: "
          "se cambia dimensione i clic si fermano")

    def guarda(nome: str = "_ultimo.png") -> Image.Image:
        return Image.open(P.screenshot_window(w, DEST / nome))

    im = guarda()
    if not e_schermata_codice(im):
        print(f"[ERR] non siamo sulla schermata Codice (sonda Fonte {P_media(im, SONDA_FONTE)}).")
        print("      Apri Menu -> Comandante -> icona Formazione -> CODICE e rilancia.")
        return 1
    print("[OK ] schermata Codice riconosciuta")

    for rarita, (tx, ty) in SCHEDE.items():
        print(f"--- {rarita}")
        P.click(w, tx, ty, 1.5)
        im = guarda()
        if not e_schermata_codice(im):
            print(f"  [ERR] persa la schermata Codice dopo il cambio scheda: mi fermo")
            return 1
        # torna in cima all'elenco
        P.scroll(w, PUNTO_ROTELLA[0], PUNTO_ROTELLA[1], 25)

        visti: List[List[int]] = []
        precedente: Optional[bytes] = None
        for pagina in range(1, 16):
            im = guarda()
            pannello = im.crop(PANNELLO)
            impronta = pannello.convert("L").resize((40, 90)).tobytes()
            if impronta == precedente:
                print("  il pannello non cambia piu': fine elenco")
                break
            precedente = impronta

            righe = righe_voci(im)
            nomi: List[Image.Image] = []
            for y in righe:
                for x in COLONNE:
                    P.click(w, x, y, 0.7)
                    # Si tiene OGNI nome letto, anche se ripetuto. Provare a
                    # scartare i doppioni qui confrontando miniature del
                    # riquadro del nome non funziona: a bassa risoluzione nomi
                    # diversi sullo stesso sfondo collassano nella stessa
                    # immagine, e il 28/09/2026 questo ha ridotto 25 voci a 7.
                    # Le ripetizioni si tolgono leggendo i fogli.
                    nomi.append(guarda().crop(NOME))
            if nomi:
                foglio(pannello, nomi, DEST / f"{rarita.lower()}_{pagina:02d}.png")
                print(f"  pagina {pagina}: {len(righe)} righe, {len(nomi)} nomi nuovi")
            else:
                print(f"  pagina {pagina}: nessun nome nuovo")
            P.scroll(w, PUNTO_ROTELLA[0], PUNTO_ROTELLA[1], -7)
        print(f"  {rarita}: {len(visti)} voci distinte")

    print("fatto")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
