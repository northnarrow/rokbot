"""Primo passo di autonomia: raccogliere la produzione pronta in citta'.

E' la piu' sicura delle azioni che migliorano il villaggio: non spende
niente, non consuma materiali, e ha una proprieta' verificabile - le risorse
possono solo salire. Tutto il resto (costruire, ricercare, addestrare) viene
dopo, quando questa parte e' rodata.

Ogni azione passa da ``MilitaryAdvisor.gate()``: e' lo stesso blocco che
rifiuta gemme, scudi, attacchi ai giocatori e la finestra di verifica
anti-plugin.

    python -m military_advisor.autonomia              prova a vuoto, non clicca
    python -m military_advisor.autonomia --esegui     raccoglie davvero

Regole fisse, scritte qui perche' non si perdano:

1. Prima di ogni clic si verifica di essere nella vista citta'. Se si e'
   aperta una finestra, il bot NON prova a chiuderla: si ferma e lo dice.
   Chiudere finestre alla cieca e' il modo piu' rapido per premere qualcosa
   di costoso.
2. C'e' un tetto ai clic per sessione. Un ciclo impazzito su un'interfaccia
   che non risponde e' il rischio peggiore di un bot lasciato solo.
3. Se la finestra del gioco cambia dimensione o non e' piu' in primo piano,
   pc_tools si ferma da solo.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image

from . import pc_tools as P
from .advisor import MilitaryAdvisor

DEST = Path("test_pc/autonomia")

# Sonda della vista citta': i pulsanti tondi in basso a destra sono azzurri
# solo qui. Sulla schermata comandanti sono grigi, nel Codice quasi neri.
SONDA_CITTA = (1500, 963, 1545, 1010)

# Zona in cui cercare le bolle di raccolta: si esclude l'interfaccia in alto
# (barra risorse, eventi) e in basso (chat, pulsanti), dove ci sono altri
# elementi chiari che non sono raccolte.
ZONA = (200, 150, 1700, 820)

TETTO_CLIC = 40


def _media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def e_vista_citta(im: Image.Image) -> bool:
    r, g, b = _media(im, SONDA_CITTA)
    return b > 150 and b > r + 60


def bolle(im: Image.Image, passo: int = 10, minimo: int = 14) -> List[Tuple[int, int]]:
    """Trova le bolle bianche di raccolta sopra gli edifici.

    Sono riquadri chiari e piccoli su uno sfondo di citta' che chiaro non e'.
    Si campiona a griglia grossa invece di esaminare ogni pixel: basta per
    localizzarle e costa poco.
    """
    px = im.convert("RGB").load()
    x0, y0, x1, y1 = ZONA
    celle = set()
    for cy in range(y0, y1, passo):
        for cx in range(x0, x1, passo):
            chiari = 0
            for y in range(cy, min(cy + passo, y1), 3):
                for x in range(cx, min(cx + passo, x1), 3):
                    r, g, b = px[x, y]
                    if min(r, g, b) > 215:
                        chiari += 1
            if chiari >= minimo // 3:
                celle.add((cx // passo, cy // passo))

    # unisce le celle adiacenti in gruppi
    gruppi: List[List[Tuple[int, int]]] = []
    viste = set()
    for c in celle:
        if c in viste:
            continue
        coda, gruppo = [c], []
        viste.add(c)
        while coda:
            cx, cy = coda.pop()
            gruppo.append((cx, cy))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    v = (cx + dx, cy + dy)
                    if v in celle and v not in viste:
                        viste.add(v)
                        coda.append(v)
        gruppi.append(gruppo)

    # Filtro di forma. La bolla di raccolta e' un riquadro bianco compatto e
    # quasi quadrato, circa 40-50 px. I falsi positivi della prima versione
    # erano decorazioni, cime di edifici e icone evento: piu' grandi, oppure
    # allungate, oppure sparse. Senza questo filtro su 30 candidati un terzo
    # non erano raccolte, e cliccarli apre finestre invece di raccogliere.
    punti = []
    for g in gruppi:
        xs = [c[0] for c in g]
        ys = [c[1] for c in g]
        larghezza = (max(xs) - min(xs) + 1) * passo
        altezza = (max(ys) - min(ys) + 1) * passo
        if not (25 <= larghezza <= 70 and 25 <= altezza <= 70):
            continue
        if max(larghezza, altezza) > 1.6 * min(larghezza, altezza):
            continue
        celle_possibili = (larghezza // passo) * (altezza // passo)
        if celle_possibili and len(g) / celle_possibili < 0.5:
            continue                      # gruppo sparso: non e' un riquadro pieno
        mx = sum(xs) / len(g) * passo + passo // 2
        my = sum(ys) / len(g) * passo + passo // 2
        punti.append((int(mx), int(my)))
    return sorted(punti, key=lambda p: (p[1], p[0]))


def segna(im: Image.Image, punti: List[Tuple[int, int]], dest: Path) -> Path:
    from PIL import ImageDraw

    out = im.convert("RGB").copy()
    d = ImageDraw.Draw(out)
    for i, (x, y) in enumerate(punti, 1):
        d.ellipse([x - 22, y - 22, x + 22, y + 22], outline=(255, 60, 60), width=3)
        d.text((x - 6, y - 34), str(i), fill=(255, 255, 0))
    out.save(dest)
    return dest


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    esegui = "--esegui" in argv
    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1
    DEST.mkdir(parents=True, exist_ok=True)

    adv = MilitaryAdvisor()
    verdetto = adv.gate({"kind": "collect", "target": "city_production", "consumes": []})
    if not verdetto["allowed"]:
        print(f"[ERR] il blocco di sicurezza rifiuta: {verdetto['reason']}")
        return 1
    if verdetto["requires_confirmation"]:
        print(f"[ERR] serve conferma: {verdetto['reason']}")
        return 1
    print(f"[OK ] blocco di sicurezza: {verdetto['reason']}")

    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra")
        return 1
    P.fissa_dimensioni(w)

    im = Image.open(P.screenshot_window(w, DEST / "_citta.png"))
    if not e_vista_citta(im):
        print(f"[ERR] non siamo nella vista citta' (sonda {_media(im, SONDA_CITTA)}). Mi fermo.")
        return 1
    print("[OK ] vista citta' riconosciuta")

    punti = bolle(im)
    print(f"trovate {len(punti)} possibili raccolte")
    segna(im, punti, DEST / "trovate.png")
    print("mappa delle posizioni:", DEST / "trovate.png")

    if not esegui:
        print("prova a vuoto: non ho cliccato niente. Rilancia con --esegui per raccogliere.")
        return 0

    if len(punti) > TETTO_CLIC:
        print(f"[ERR] {len(punti)} candidati, oltre il tetto di {TETTO_CLIC}: "
              "probabile riconoscimento sbagliato. Mi fermo senza cliccare.")
        return 1

    raccolte = 0
    rimaste = len(punti)
    for i, (x, y) in enumerate(punti, 1):
        P.click(w, x, y, 1.0)
        dopo = Image.open(P.screenshot_window(w, DEST / "_dopo.png"))
        if not e_vista_citta(dopo):
            dopo.save(DEST / "_finestra_inattesa.png")
            print(f"  clic {i} in ({x}, {y}): si e' aperta una finestra. "
                  "NON la chiudo da solo: mi fermo qui.")
            print(f"  schermata salvata in {DEST / '_finestra_inattesa.png'}")
            break

        # Una raccolta riuscita fa sparire la sua bolla. Se il conteggio non
        # scende, quel clic ha colpito altro: un edificio o una decorazione,
        # che aprono un menu a raggiera senza cambiare schermata - e quel menu
        # contiene pulsanti come "riponi" o "addestra". La sonda sulla vista
        # citta' non basta a vederlo, perche' i pulsanti in basso a destra
        # restano visibili. Successo il 28/09/2026 con un Albero di Sakura.
        ora = len(bolle(dopo))
        if ora >= rimaste:
            dopo.save(DEST / "_clic_a_vuoto.png")
            print(f"  clic {i} in ({x}, {y}): nessuna bolla e' sparita "
                  f"({rimaste} -> {ora}). Ho colpito qualcosa che non e' una "
                  "raccolta: mi fermo.")
            break
        rimaste = ora
        raccolte += 1
        print(f"  {i}/{len(punti)} raccolto in ({x}, {y}), ne restano {rimaste}")

    print(f"fatto: {raccolte} raccolte su {len(punti)} candidati")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
