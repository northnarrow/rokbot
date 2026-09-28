"""Legge nome + formazione degli armamenti dall'inventario del client PC.

SOLA LETTURA: seleziona le caselle e legge il pannello di destra. Non preme
Potenzia, Ricicla ne' altro.

Serve a confermare l'abbinamento nome -> formazione ricavato dal Codice, dove
veniva dedotto dall'ordine dei gruppi. Qui invece il gioco lo scrive:
"Pergamena del nord / Per Formazione ad arco".

Da lanciare con Articoli -> ARMAMENTI aperto:
    python -m military_advisor.pc_verifica_formazioni
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List

from PIL import Image

from . import pc_tools as P

DEST = Path("test_pc/formazioni")

# Griglia dell'inventario: 6 colonne, 4 righe visibili.
COLONNE = (321, 475, 629, 783, 938, 1092)
RIGHE = (358, 505, 652, 799)

# Nome e formazione nel pannello di destra.
ETICHETTA = (1228, 438, 1572, 516)

# Sonda: i pulsanti Potenzia/Ricicla sono azzurri solo qui, con un armamento
# selezionato. Sono anche i due da non premere mai.
SONDA = (1240, 800, 1370, 848)


def _media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def e_inventario_armamenti(im: Image.Image) -> bool:
    r, g, b = _media(im, SONDA)
    return b > 200 and g > 140 and r < 90


def main(argv: List[str] | None = None) -> int:
    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1
    DEST.mkdir(parents=True, exist_ok=True)

    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra")
        return 1
    P.fissa_dimensioni(w)

    def guarda() -> Image.Image:
        return Image.open(P.screenshot_window(w, DEST / "_ultimo.png"))

    im = guarda()
    if not e_inventario_armamenti(im):
        print(f"[ERR] non siamo nell'inventario armamenti (sonda {_media(im, SONDA)}).")
        print("      Apri Articoli -> ARMAMENTI e seleziona un armamento, poi rilancia.")
        return 1
    print("[OK ] inventario armamenti riconosciuto")

    etichette: List[Image.Image] = []
    for pagina in range(1, 9):
        for y in RIGHE:
            for x in COLONNE:
                P.click(w, x, y, 0.6)
                etichette.append(guarda().crop(ETICHETTA))
        print(f"  pagina {pagina}: {len(etichette)} etichette")
        P.scroll(w, 700, 600, -4)

    larghezza = etichette[0].width
    altezza = etichette[0].height
    per_foglio = 16
    for n in range(0, len(etichette), per_foglio):
        gruppo = etichette[n:n + per_foglio]
        f = Image.new("RGB", (larghezza * 2, altezza * ((len(gruppo) + 1) // 2)), (12, 12, 12))
        for i, e in enumerate(gruppo):
            f.paste(e, ((i % 2) * larghezza, (i // 2) * altezza))
        f.save(DEST / f"etichette_{n // per_foglio + 1:02d}.png")
    print(f"salvate {len(etichette)} etichette")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
