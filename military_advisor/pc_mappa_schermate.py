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

from . import ocr, pc_tools as P

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
    return {
        "schermata": nome,
        "finestra": [im.width, im.height],
        "_nota": "Riquadri in coordinate della finestra, come li produce "
                 "pc_tools.screenshot_window(). Generati leggendo la schermata, "
                 "non misurati a mano.",
        "etichette": sorted(migliori.values(), key=lambda v: (v["riquadro"][1], v["riquadro"][0])),
    }


def salva(nome: str, im: Image.Image) -> Path:
    MAPPE.mkdir(parents=True, exist_ok=True)
    SCATTI.mkdir(parents=True, exist_ok=True)
    im.save(SCATTI / f"{nome}.png")
    d = mappa_schermata(nome, im)
    p = MAPPE / f"{nome}.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK ] {nome}: {len(d['etichette'])} etichette -> {p}")
    for v in d["etichette"][:12]:
        print(f"       {v['testo']!r} in {tuple(v['centro'])}")
    if len(d["etichette"]) > 12:
        print(f"       ... e altre {len(d['etichette']) - 12}")
    return p


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
