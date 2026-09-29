"""Riconoscimento dei pulsanti del gioco, per colore e non per testo.

L'OCR a schermo intero legge bene le etichette e male proprio i pulsanti:
testo bianco stilizzato su fondo azzurro saturo. Il 29/09/2026 non e'
riuscito a leggere "CONFERMA" su un bottone e ha invece trovato la stessa
parola dentro la frase del messaggio, mandando il clic sul testo.

I pulsanti pero' hanno tutti la stessa tinta - azzurro pieno, circa
(7, 184, 239) - e quella si riconosce senza leggere una lettera. Trovato il
pulsante si legge la sua etichetta con un ritaglio mirato ingrandito, che e'
molto piu' affidabile della passata a schermo intero.

    python -m military_advisor.pulsanti --prova
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image

from . import ocr


@dataclass
class Pulsante:
    riquadro: Tuple[int, int, int, int]
    etichetta: str = ""

    @property
    def centro(self) -> Tuple[int, int]:
        x1, y1, x2, y2 = self.riquadro
        return (x1 + x2) // 2, (y1 + y2) // 2

    @property
    def dimensioni(self) -> Tuple[int, int]:
        x1, y1, x2, y2 = self.riquadro
        return x2 - x1, y2 - y1


# Il gioco ha due stili di pulsante, misurati il 29/09/2026:
#   - pieni, azzurro acceso: (7,184,239) su Fonte, (15,174,233) su Abilita'.
#     Differenza blu-rosso oltre 200.
#   - icone rotonde, azzurro pallido: (111,167,192) su Codice. Differenza 81.
# Una soglia sola non li prende entrambi, e abbassarla troppo fa entrare i
# tetti blu della citta'. 70 e' il valore che li prende tutti e due senza
# raccogliere l'abitato: verificato contando i falsi positivi sulla citta'.
DIFFERENZA_MINIMA = 70


def azzurro(rgb, differenza: int = DIFFERENZA_MINIMA) -> bool:
    r, g, b = rgb[:3]
    return b > 170 and g > 120 and r < 140 and b - r > differenza


def trova(im: Image.Image, passo: int = 6, minimo_pieno: float = 0.40,
          minimo_cella: float = 0.5) -> List[Pulsante]:
    """Tutti i pulsanti azzurri della schermata."""
    px = im.convert("RGB").load()
    L, A = im.size
    celle = set()
    for cy in range(0, A - passo, passo):
        for cx in range(0, L - passo, passo):
            n = sum(1 for y in range(cy, cy + passo, 2) for x in range(cx, cx + passo, 2)
                    if azzurro(px[x, y]))
            # Le icone rotonde hanno un disegno scuro dentro, quindi l'azzurro
            # e' spezzato: pretendere una cella quasi tutta piena le perde.
            if n >= (passo // 2) ** 2 * minimo_cella:
                celle.add((cx // passo, cy // passo))

    gruppi: List[List[Tuple[int, int]]] = []
    viste = set()
    for c in celle:
        if c in viste:
            continue
        coda, g = [c], []
        viste.add(c)
        while coda:
            cx, cy = coda.pop()
            g.append((cx, cy))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    v = (cx + dx, cy + dy)
                    if v in celle and v not in viste:
                        viste.add(v)
                        coda.append(v)
        gruppi.append(g)

    fuori: List[Pulsante] = []
    for g in gruppi:
        xs = [c[0] for c in g]
        ys = [c[1] for c in g]
        x1, y1 = min(xs) * passo, min(ys) * passo
        x2, y2 = (max(xs) + 1) * passo, (max(ys) + 1) * passo
        w, h = x2 - x1, y2 - y1
        if w < 45 or h < 22 or w > L * 0.6 or h > A * 0.35:
            continue
        if len(g) / max(1, (w // passo) * (h // passo)) < minimo_pieno:
            continue          # forma non piena: e' un bordo o un riflesso
        fuori.append(Pulsante((x1, y1, x2, y2)))
    return sorted(fuori, key=lambda p: (p.riquadro[1], p.riquadro[0]))


def leggi_etichette(im: Image.Image, ps: List[Pulsante], scala: int = 5) -> List[Pulsante]:
    """Legge il testo dentro ogni pulsante.

    Si legge SOLO il ritaglio del pulsante, ingrandito: e' la differenza fra
    riuscire e non riuscire su testo bianco stilizzato su fondo saturo.
    """
    for p in ps:
        x1, y1, x2, y2 = p.riquadro
        m = 3
        p.etichetta = ocr.leggi(im.crop((x1 + m, y1 + m, x2 - m, y2 - m)),
                                riga_singola=True, scala=scala)
        if len(p.etichetta.strip()) >= 3:
            continue
        # Le icone rotonde portano l'etichetta SOTTO, non dentro: dentro c'e'
        # solo il disegno. Se il ritaglio interno non da' niente si guarda la
        # striscia subito sotto.
        sotto = im.crop((x1 - 30, y2, x2 + 30, min(im.height, y2 + 46)))
        if sotto.height > 8:
            p.etichetta = ocr.leggi(sotto, riga_singola=False, scala=scala)
    return ps


def trova_pulsante(im: Image.Image, testo: str, soglia: float = 0.7) -> Optional[Pulsante]:
    """Il pulsante la cui etichetta somiglia di piu' al testo cercato.

    A differenza della ricerca sul testo a schermo intero, qui si guarda solo
    dentro i pulsanti: la parola trovata in mezzo a una frase non puo' essere
    scambiata per un bottone.
    """
    migliore, punteggio = None, 0.0
    for p in leggi_etichette(im, trova(im)):
        r = ocr._somiglianza(p.etichetta, testo)
        if r > punteggio:
            migliore, punteggio = p, r
    return migliore if punteggio >= soglia else None


# ------------------------------------------------------------------ prova
CASI = [
    ("test_pc/a03.png", ["TALENTI", "ABILITÀ"]),
    ("test_pc/a04.png", ["CODICE", "RICICLA"]),
    ("test_pc/a05.png", ["FONTE"]),
    ("test_pc/a01.png", ["POTENZIA", "RICICLA"]),
    ("test_pc/disc.png", ["CONFERMA"]),
]


def prova() -> int:
    tot_ok = tot = 0
    for f, attesi in CASI:
        p = Path(f)
        if not p.exists():
            print(f"[--- ] {f}: manca")
            continue
        im = Image.open(p)
        ps = leggi_etichette(im, trova(im))
        letti = [q.etichetta for q in ps]
        ok = []
        for a in attesi:
            if any(ocr._somiglianza(l, a) >= 0.7 for l in letti):
                ok.append(a)
        tot_ok += len(ok)
        tot += len(attesi)
        print(f"[{'OK ' if len(ok) == len(attesi) else 'ERR'}] {p.name}: "
              f"{len(ok)}/{len(attesi)} attesi, {len(ps)} pulsanti trovati")
        for q in ps:
            print(f"       {q.dimensioni[0]:3}x{q.dimensioni[1]:2} in {q.centro} -> {q.etichetta!r}")
    print(f"\npulsanti: {tot_ok}/{tot} riconosciuti")
    return 0 if tot_ok == tot else 1


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--prova" in argv:
        return prova()
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
