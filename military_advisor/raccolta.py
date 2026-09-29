"""Marce di raccolta: cerca i giacimenti sulla mappa e ci manda le truppe.

E' l'azione con il rendimento piu' alto del gioco e insieme una delle piu'
sicure: non spende niente, non tocca altri giocatori, e le truppe tornano da
sole. Senza materie prime il villaggio non cresce, e truppe ferme in citta'
non producono nulla.

    python -m military_advisor.raccolta --prova      dice cosa farebbe
    python -m military_advisor.raccolta --tutte      manda una marcia per risorsa
    python -m military_advisor.raccolta --risorsa oro

Da lanciare con il gioco sulla MAPPA DEL REGNO (tasto Spazio dalla citta').

Tutto quello che c'e' qui e' stato misurato sul client il 29/09/2026, non
dedotto.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Optional

from PIL import Image

from . import ocr, pulsanti, pc_tools as P
from .advisor import MilitaryAdvisor

DEST = Path("test_pc/raccolta")

# Categorie in fondo al pannello di ricerca, a y=950.
CATEGORIE: Dict[str, int] = {
    "barbari": 527, "cibo": 710, "legno": 894, "pietra": 1079, "oro": 1265,
}

# Il pannello si CENTRA SOPRA la categoria scelta, quindi i suoi pulsanti si
# spostano con lei. Scostamenti misurati rispetto alla x della categoria.
DX_PIU = 137
DX_CERCA = 2
Y_PIU, Y_CERCA = 741, 808
Y_LIVELLO = (700, 730)

LENTE = (1735, 866)          # apre la ricerca sulla mappa, scorciatoia F
NUOVE_TRUPPE = (1527, 320)   # testo su due righe: il riconoscimento non lo vede
MARCIA = (1176, 795)         # arancione, non azzurro: fuori dal rilevatore
CODA = (1660, 175, 1790, 205)
PANNELLO_NODO = (1100, 410, 1400, 540)
COMPOSIZIONE = (860, 660, 1320, 720)

LIVELLO_MASSIMO = 8


def _numero(testo: str) -> Optional[int]:
    cifre = "".join(c for c in testo if c.isdigit() or c == ".")
    cifre = cifre.replace(".", "")
    return int(cifre) if cifre else None


def livello_attuale(im: Image.Image, cat_x: int) -> Optional[int]:
    t = ocr.leggi(im, (cat_x + 40, Y_LIVELLO[0], cat_x + 220, Y_LIVELLO[1]),
                  riga_singola=True, scala=5)
    for pezzo in t.replace(":", " ").split():
        if pezzo.isdigit():
            return int(pezzo)
    return None


def imposta_livello(w, cat_x: int, obiettivo: int, guarda) -> bool:
    """Porta il cursore del livello al valore voluto.

    Il gioco RICORDA il livello fra una ricerca e l'altra, quindi spesso non
    c'e' niente da fare: misurato il 29/09/2026, cercando l'oro dopo la pietra
    il cursore era gia' su 8.
    """
    for _ in range(12):
        lv = livello_attuale(guarda(), cat_x)
        if lv is None:
            print("      livello non leggibile: non tocco il cursore")
            return False
        if lv >= obiettivo:
            return True
        P.click(w, cat_x + DX_PIU, Y_PIU, 0.4)
    return False


def manda(w, risorsa: str, guarda, esegui: bool) -> bool:
    cat_x = CATEGORIE[risorsa]
    print(f"  {risorsa}:")
    P.click(w, *LENTE, 2.5)
    P.click(w, cat_x, 950, 2.0)
    if not imposta_livello(w, cat_x, LIVELLO_MASSIMO, guarda):
        print("      non sono riuscito a impostare il livello: salto")
        return False

    P.click(w, cat_x + DX_CERCA, Y_CERCA, 4.0)
    im = guarda()
    testo = ocr.leggi(im, PANNELLO_NODO, scala=4)
    print(f"      {testo}")
    riserve = None
    if "Riserve" in testo:
        dopo = testo.split("Riserve", 1)[1].split()
        riserve = _numero(dopo[0]) if dopo else None
    if "Nessuno" not in testo:
        print("      il giacimento risulta occupato: lo lascio stare")
        return False

    bottone = pulsanti.trova_pulsante(im, "RACCOGLI", 0.7)
    if not bottone:
        print("      pulsante RACCOGLI non trovato: mi fermo")
        return False

    if not esegui:
        print(f"      (prova a vuoto) manderei una marcia qui, riserve {riserve}")
        return True

    P.click(w, *bottone.centro, 3.5)
    P.click(w, *NUOVE_TRUPPE, 4.0)
    comp = ocr.leggi(guarda(), COMPOSIZIONE, scala=4)
    print(f"      {comp}")

    # Non si preme MAX se la capacita' copre gia' le riserve del nodo:
    # non entrerebbe una risorsa in piu' e resterebbero impegnate truppe
    # utili per le altre marce. Misurato su tutti e quattro i giacimenti.
    capacita = None
    if "Capacit" in comp:
        capacita = _numero(comp.split("Capacit", 1)[1].split()[1]
                           if len(comp.split("Capacit", 1)[1].split()) > 1 else "")
    if capacita and riserve and capacita < riserve:
        print(f"      capacita' {capacita} sotto le riserve {riserve}: "
              "converrebbe riempire la marcia")

    P.click(w, *MARCIA, 4.0)
    coda = ocr.leggi(guarda(), CODA, riga_singola=True, scala=5)
    print(f"      inviata. Coda: {coda.strip()}")
    return True


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1
    esegui = "--tutte" in argv or "--risorsa" in argv
    risorse = ["cibo", "legno", "pietra", "oro"]
    if "--risorsa" in argv:
        i = argv.index("--risorsa")
        if i + 1 < len(argv):
            risorse = [argv[i + 1]]

    adv = MilitaryAdvisor()
    v = adv.gate({"kind": "gather", "target": "resource_node", "consumes": []})
    if not v["allowed"] or v["requires_confirmation"]:
        print(f"[ERR] blocco di sicurezza: {v['reason']}")
        return 1
    print(f"[OK ] blocco di sicurezza: {v['reason']}")

    DEST.mkdir(parents=True, exist_ok=True)
    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra")
        return 1
    P.fissa_dimensioni(w)

    def guarda() -> Image.Image:
        P.bring_to_front(w)
        return Image.open(P.screenshot_window(w, DEST / "_ultimo.png"))

    for r in risorse:
        if r not in CATEGORIE:
            print(f"  {r}: categoria sconosciuta")
            continue
        manda(w, r, guarda, esegui)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
