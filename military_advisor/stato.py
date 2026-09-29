"""Legge il "Sommario delle code" e dice cosa nel villaggio e' fermo.

E' il pannello che si apre dall'icona a righe in alto a sinistra della citta'.
Vale piu' di qualunque riconoscimento a pixel: e' testo strutturato su fondo
chiaro, elenca TUTTE le code in un posto solo, e dice "Inattivo" a chiare
lettere invece di farlo dedurre da un'immagine.

Il principio di fondo del gioco e' che il tempo e' l'unica risorsa che non
torna: una coda ferma e' perdita secca. Questo modulo serve a vederle.

    python -m military_advisor.stato

SOLA LETTURA: apre il pannello, scorre, legge, e lo richiude.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional

from PIL import Image

from . import ocr, pc_tools as P

DEST = Path("test_pc/stato")
APRI_LISTA = (40, 222)          # icona a righe in alto a sinistra
PANNELLO = (10, 130, 325, 975)
ROTELLA = (165, 700)
SCORRIMENTI = (0, -6, -8)       # posizioni successive dell'elenco

FERMO = ("inattivo", "in attesa")


def leggi_pannello(w, guarda) -> List[List[str]]:
    """Apre il sommario, lo scorre e restituisce le righe di OGNI schermata.

    Si tengono separate invece di fonderle: le voci ferme si chiamano tutte
    "Inattivo" o "In attesa", quindi unendo e togliendo i doppioni sei code
    ferme diventano due, e il riassunto mente sui numeri.
    """
    P.click(w, *APRI_LISTA, 2.5)
    # Il pannello RICORDA dove era stato lasciato: riaprendolo riparte da
    # meta' elenco e le prime voci non si vedono. Si torna in cima.
    P.scroll(w, ROTELLA[0], ROTELLA[1], 15)
    schermate: List[List[str]] = []
    for tacche in SCORRIMENTI:
        if tacche:
            P.scroll(w, ROTELLA[0], ROTELLA[1], tacche)
        im = guarda().crop(PANNELLO)
        righe = [" ".join(r.split()) for r in ocr.righe(ocr.parole(im))]
        schermate.append([r for r in righe if len(r) > 2])
    return schermate


def _chiave(riga: str) -> tuple:
    """Chiave di confronto insensibile all'ordine delle parole.

    L'OCR restituisce le parole di una riga in ordine variabile, quindi la
    stessa coda letta in due scorrimenti diventa "edifici Coda gli 1 per" e
    "Coda gli edifici 1 per": due stringhe diverse per la stessa cosa, e il
    conteggio delle code ferme saliva da 6 a 9.

    Si tengono anche i token di un carattere solo: sembrano rumore ma sono
    quelli che distinguono "Coda 1" da "Coda 2" e Scout A da Scout B.
    Scartandoli sei code ferme diventavano tre.
    """
    parole = [p.strip(r".,:;|\/-_").lower() for p in riga.split()]
    return tuple(sorted(p for p in parole if p.isalnum()))


def _voci_ferme(schermate: List[List[str]]) -> List[str]:
    """Abbina ogni "Inattivo"/"In attesa" alla voce che lo precede.

    Cosi' una coda ferma si riconosce dal suo nome e non dalla parola di
    stato, e la stessa coda vista in due scorrimenti diversi conta una volta.
    """
    trovate: List[str] = []
    viste = set()
    for righe in schermate:
        etichetta = ""
        for r in righe:
            b = r.lower()
            if any(f == b or f in b for f in FERMO) and len(b) < 20:
                k = _chiave(etichetta)
                if etichetta and k and k not in viste:
                    viste.add(k)
                    trovate.append(etichetta)
            elif len(r) > 3:
                etichetta = r
    return trovate


def riassumi(schermate: List[List[str]]) -> List[str]:
    """Da righe lette a cose da fare, in ordine di quanto costa lasciarle stare."""
    piatte: List[str] = []
    for righe in schermate:
        for r in righe:
            if r not in piatte:
                piatte.append(r)
    testo = " | ".join(piatte).lower()
    avvisi: List[str] = []

    if "un'alleanza" in testo and "non" in testo:
        avvisi.append("NON SEI IN UN'ALLEANZA: perdi aiuti alle code, tecnologie, "
                      "negozio e centri risorse. E' la voce che pesa di piu'.")

    ferme = _voci_ferme(schermate)
    if ferme:
        avvisi.append(f"{len(ferme)} voci ferme: " + "; ".join(ferme))

    visti = set()
    for r in piatte:
        b = r.lower()
        if "viaggi" in b and "/" in r and "viaggi" not in visti:
            visti.add("viaggi")
            avvisi.append(f"Viaggi armamenti non usati ({r}): costano solo PA")
        if "rimanenti" in b and "/" in r and "spedisci" not in visti:
            visti.add("spedisci")
            avvisi.append(f"Spedizioni non usate ({r})")
        if "producibile" in b and "materiali" not in visti:
            visti.add("materiali")
            avvisi.append(f"Produzione materiali ({r})")
    return avvisi


def main(argv: Optional[List[str]] = None) -> int:
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
        P.bring_to_front(w)
        return Image.open(P.screenshot_window(w, DEST / "_ultimo.png"))

    schermate = leggi_pannello(w, guarda)
    P.click(w, *APRI_LISTA, 1.5)          # richiude

    totale = sum(len(s) for s in schermate)
    print(f"sommario delle code: {len(schermate)} schermate, {totale} righe" + chr(10))
    avvisi = riassumi(schermate)
    print("\ncosa e' fermo:")
    for a in avvisi:
        print("  -", a)
    if not avvisi:
        print("  niente di fermo: il villaggio sta lavorando su tutto")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
