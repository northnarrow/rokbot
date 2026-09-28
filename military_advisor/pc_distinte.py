"""Riduce le etichette nome+formazione raccolte a quelle distinte.

Le etichette sono state salvate in fogli da 16 (2 colonne x 8 righe). Qui si
ritagliano di nuovo una per una e si tengono solo quelle diverse.

A differenza dei nomi dei comandanti, qui il confronto per somiglianza e'
affidabile: lo sfondo e' sempre la stessa pergamena, quindi due etichette
differiscono solo per il testo.
"""

from pathlib import Path
from typing import List

from PIL import Image

DEST = Path("test_pc/formazioni")
COLONNE, RIGHE = 2, 8
SOGLIA = 3.0


def _firma(im: Image.Image) -> List[int]:
    return list(im.convert("L").resize((96, 22), Image.LANCZOS).tobytes())


def _distanza(a, b) -> float:
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def main() -> int:
    fogli = sorted(DEST.glob("etichette_*.png"))
    if not fogli:
        print("nessun foglio da leggere")
        return 1

    firme: List[List[int]] = []
    distinte: List[Image.Image] = []
    totale = 0
    for f in fogli:
        im = Image.open(f)
        w, h = im.width // COLONNE, im.height // RIGHE
        for r in range(RIGHE):
            for c in range(COLONNE):
                e = im.crop((c * w, r * h, (c + 1) * w, (r + 1) * h))
                if e.convert("L").resize((8, 8)).tobytes().count(0) > 50:
                    continue  # riquadro vuoto in coda al foglio
                totale += 1
                s = _firma(e)
                if any(_distanza(s, g) < SOGLIA for g in firme):
                    continue
                firme.append(s)
                distinte.append(e)

    print(f"{totale} etichette lette, {len(distinte)} distinte")
    if not distinte:
        return 1
    w, h = distinte[0].width, distinte[0].height
    colonne = 2
    righe = (len(distinte) + colonne - 1) // colonne
    out = Image.new("RGB", (w * colonne, h * righe), (12, 12, 12))
    for i, e in enumerate(distinte):
        out.paste(e, ((i % colonne) * w, (i // colonne) * h))
    p = DEST.parent / "formazioni_distinte.png"
    out.save(p)
    print("salvato", p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
