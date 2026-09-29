"""Mappa una schermata del gioco: ogni etichetta leggibile con la sua posizione.

I riquadri non si misurano a mano. L'OCR a schermo intero restituisce gia'
testo E posizione, quindi la mappa di una schermata si genera leggendola.
Quello che ne esce serve a due cose: leggere un campo preciso con un ritaglio
mirato (molto piu' affidabile della passata a schermo intero) e cliccare
"quel pulsante li'" conoscendone il nome invece delle coordinate.

    python -m military_advisor.pc_mappa_schermate citta
    python -m military_advisor.pc_mappa_schermate --elenco

Le mappe finiscono in riferimenti_ui/schermate/<nome>.json, gli screenshot in
test_pc/schermate/ (che git ignora).

SOLA LETTURA: fa uno screenshot e legge. Non clicca niente: alla schermata
che vuoi mappare ci arrivi tu, o ci arriva chi chiama questo modulo.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List, Optional

from PIL import Image

from . import ocr, pulsanti, pc_tools as P

MAPPE = Path("military_advisor/riferimenti_ui/schermate")
SCATTI = Path("test_pc/schermate")

# Testi che non vanno salvati come riferimenti: cambiano a ogni istante e
# domani sarebbero rumore.
VOLATILI = ("utc", "duke", "[al08]", "/2.000")


def _volatile(t: str) -> bool:
    b = t.lower()
    if any(v in b for v in VOLATILI):
        return True
    cifre = sum(c.isdigit() for c in t)
    return cifre and cifre >= len(t.replace(".", "").replace(":", "")) - 1


def mappa_schermata(nome: str, im: Image.Image) -> dict:
    ps = ocr.parole(im)
    voci = []
    for p in ocr.gruppi(ps):
        t = p.testo.strip()
        if len(t) < 3 or _volatile(t):
            continue
        voci.append({"testo": t, "riquadro": list(p.riquadro),
                     "centro": list(p.centro), "confidenza": p.confidenza})
    # a parita' di testo tiene la lettura piu' sicura
    migliori = {}
    for v in voci:
        k = v["testo"].lower()
        if k not in migliori or v["confidenza"] > migliori[k]["confidenza"]:
            migliori[k] = v

    # Tiene solo le frasi intere. La ricostruzione delle sequenze produce
    # anche tutti i pezzi ("Rise", "Rise of", "Rise of Kingdoms"): utili per
    # cercare, inutili in una mappa, dove diventano rumore.
    lista = list(migliori.values())
    finali = []
    for v in lista:
        t = v["testo"].lower()
        contenuto_in_altro = any(
            v is not a and t in a["testo"].lower()
            and abs(a["riquadro"][1] - v["riquadro"][1]) < 10
            for a in lista)
        if not contenuto_in_altro:
            finali.append(v)
    migliori = {v["testo"].lower(): v for v in finali}

    # I pulsanti si riconoscono per colore, non per testo: l'OCR a schermo
    # intero proprio su quelli fallisce. Senza questa parte la mappa avrebbe
    # le etichette e non i bottoni, cioe' mancherebbe quello che serve per
    # cliccare.
    bot = []
    for b in pulsanti.leggi_etichette(im, pulsanti.trova(im)):
        bot.append({"etichetta": b.etichetta.strip(), "riquadro": list(b.riquadro),
                    "centro": list(b.centro),
                    "dimensioni": list(b.dimensioni)})
    return {
        "schermata": nome,
        "finestra": [im.width, im.height],
        "_nota": "Riquadri in coordinate della finestra, come li produce "
                 "pc_tools.screenshot_window(). Generati leggendo la schermata, "
                 "non misurati a mano.",
        "etichette": sorted(migliori.values(), key=lambda v: (v["riquadro"][1], v["riquadro"][0])),
        "pulsanti": bot,
    }


def salva(nome: str, im: Image.Image) -> Path:
    MAPPE.mkdir(parents=True, exist_ok=True)
    SCATTI.mkdir(parents=True, exist_ok=True)
    im.save(SCATTI / f"{nome}.png")
    d = mappa_schermata(nome, im)
    p = MAPPE / f"{nome}.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK ] {nome}: {len(d['etichette'])} etichette, "
          f"{len(d['pulsanti'])} pulsanti -> {p}")
    for b in d["pulsanti"]:
        print(f"       pulsante {b['etichetta']!r} in {tuple(b['centro'])}")
    return p


# ------------------------------------------------------------------- il giro
# Punti di ingresso dalla citta'. Si apre, si mappa, si torna indietro e si
# verifica di essere di nuovo in citta' prima del passo successivo: mai due
# spostamenti a stima di fila.
CITTA_SONDA = (1500, 963, 1545, 1010)
TAPPE = [
    ("articoli",   (1350, 987), (1545, 181)),
    ("comandanti", (1521, 987), (47, 69)),
    ("alleanza",   (1436, 987), (47, 69)),
    ("campagna",   (1264, 987), (47, 69)),
    # La posta non ha la freccia indietro in alto a sinistra: li' ci sono le
    # schede, e cliccarle non chiude niente. Si esce dalla X.
    ("posta",      (1606, 987), (1470, 71)),
]


def _in_citta(im: Image.Image) -> bool:
    b = im.convert("RGB").crop(CITTA_SONDA).tobytes()
    n = len(b) // 3
    r, g, bl = (round(sum(b[i::3]) / n) for i in range(3))
    return bl > 150 and bl > r + 60


def giro() -> int:
    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra")
        return 1
    P.fissa_dimensioni(w)
    SCATTI.mkdir(parents=True, exist_ok=True)

    def guarda() -> Image.Image:
        return Image.open(P.screenshot_window(w, SCATTI / "_ultimo.png"))

    im = guarda()
    if not _in_citta(im):
        print("[ERR] non siamo in citta': il giro parte da li'. Mi fermo.")
        return 1
    salva("citta", im)

    for nome, ingresso, uscita in TAPPE:
        P.click(w, *ingresso, 2.5)
        im = guarda()
        if _in_citta(im):
            print(f"[ERR] {nome}: la schermata non si e' aperta. Salto.")
            continue
        salva(nome, im)
        P.click(w, *uscita, 2.5)
        if not _in_citta(guarda()):
            print(f"[ERR] dopo {nome} non sono tornato in citta'. Mi fermo qui "
                  "invece di continuare a cliccare alla cieca.")
            return 1
    print("giro completato")
    return elenco()


def elenco() -> int:
    if not MAPPE.exists():
        print("nessuna schermata mappata")
        return 0
    tot = 0
    for f in sorted(MAPPE.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        n = len(d.get("etichette") or [])
        tot += n
        print(f"  {f.stem:28} {n:4} etichette")
    print(f"\n{len(list(MAPPE.glob('*.json')))} schermate, {tot} etichette in totale")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--elenco" in argv:
        return elenco()
    if "--giro" in argv:
        if sys.platform != "win32":
            print("[ERR] serve Windows con il client PC aperto")
            return 1
        return giro()
    if not argv:
        print("uso: python -m military_advisor.pc_mappa_schermate <nome>")
        return 1
    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1
    nome = argv[0]
    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra")
        return 1
    P.fissa_dimensioni(w)
    im = Image.open(P.screenshot_window(w, SCATTI / "_ultimo.png"))
    salva(nome, im)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
