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

from . import ocr, pc_tools as P, pulsanti
from .advisor import MilitaryAdvisor

DEST = Path("test_pc/autonomia")

# Sonda della vista citta': i pulsanti tondi in basso a destra sono azzurri
# solo qui. Sulla schermata comandanti sono grigi, nel Codice quasi neri.
SONDA_CITTA = (1500, 963, 1545, 1010)

# Zona in cui cercare le nuvolette, e i rettangoli di interfaccia da saltare.
# La prima versione tagliava a y=820 "per stare larghi sull'interfaccia" e
# cosi' perdeva tutte le nuvolette di cibo in fondo al villaggio, piu' una di
# monete in alto. Meglio una zona ampia con esclusioni precise che un
# rettangolo prudente: le esclusioni si vedono e si correggono, un ritaglio
# troppo stretto toglie roba in silenzio.
ZONA = (120, 90, 1700, 1010)

ESCLUSIONI = [
    (0, 0, 300, 330),        # avatar, potenza, VIP, pergamena missioni
    (1180, 0, 1796, 175),    # barra risorse ed eventi
    (1670, 170, 1796, 560),  # pannello delle marce in corso
    (0, 800, 335, 1040),     # comando rapido e chat
    (1190, 900, 1796, 1040), # pulsanti in basso a destra
    (1680, 820, 1796, 915),  # pulsante costruisci
]


def _fuori(x: int, y: int) -> bool:
    return any(a <= x < c and b <= y < d for a, b, c, d in ESCLUSIONI)


TETTO_CLIC = 40
INDIETRO = (47, 69)   # freccia in alto a sinistra delle schermate a tutto schermo


def _media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def e_vista_citta(im: Image.Image) -> bool:
    r, g, b = _media(im, SONDA_CITTA)
    return b > 150 and b > r + 60


def _nuvoletta(rgb) -> bool:
    """Il fondo di una nuvoletta di raccolta, nei suoi DUE colori.

    Misurati sul client il 29/09/2026:
      - bianco  (240, 242, 230): monete e pietra, produzione normale;
      - beige   (231, 202, 136): legno e cibo, e il beige vuol dire che il
        giacimento e' PIENO.

    La prima versione cercava solo il bianco e quindi saltava proprio le
    miniere piene, cioe' quelle che urgeva svuotare. Cercare una sola tinta
    perche' e' quella che si era vista per prima e' un errore facile da fare
    e difficile da notare: il bot raccoglieva, solo non tutto.
    """
    r, g, b = rgb[:3]
    bianco = min(r, g, b) > 210 and abs(r - b) < 25
    beige = r > 200 and 175 < g < 225 and 100 < b < 170 and r - b > 65
    return bianco or beige


def _cornice(px, cx: int, cy: int, rx: int = 18, ry: int = 14) -> float:
    """Quanta parte del bordo di una nuvoletta, centrata qui, ha il suo colore.

    Si guarda la CORNICE e non il pieno. La nuvoletta ha al centro l'icona
    della risorsa - tronco, pannocchia, moneta - che del colore di fondo non
    e' nulla: pretendere una macchia piena la spezza in frammenti da 20x40,
    che il filtro di forma poi scarta. Misurato il 29/09/2026: cercando macchie
    piene si trovavano 15 nuvolette su 16, e quelle perse erano proprio le
    piene, cioe' quelle che urge svuotare.
    """
    punti = []
    for dx in (-rx, -rx // 2, 0, rx // 2, rx):
        punti += [(cx + dx, cy - ry), (cx + dx, cy + ry)]
    for dy in (-ry, 0, ry):
        punti += [(cx - rx, cy + dy), (cx + rx, cy + dy)]
    dentro = [(x, y) for x, y in punti
              if ZONA[0] <= x < ZONA[2] and ZONA[1] <= y < ZONA[3]]
    if len(dentro) < len(punti) * 0.8:
        return 0.0
    return sum(1 for q in dentro if _nuvoletta(px[q])) / len(dentro)


def bolle(im: Image.Image, passo: int = 8, soglia: float = 0.72,
          distanza_minima: int = 34) -> List[Tuple[int, int]]:
    """Trova le nuvolette di raccolta sopra gli edifici.

    Due passate. La prima scandisce la citta' a griglia larga con una soglia
    bassa; la seconda affina ogni candidato guardandogli intorno e tiene solo
    chi supera la soglia vera.

    L'affinamento serve davvero: il punteggio ha un picco stretto, e una
    nuvoletta il cui centro cade fra due punti della griglia dava 0.69 contro
    lo 0.94 del suo centro esatto: sotto soglia, quindi persa. Abbassare la
    soglia avrebbe fatto entrare falsi positivi; cercare meglio no.
    """
    px = im.convert("RGB").load()
    x0, y0, x1, y1 = ZONA
    grezzi = []
    for cy in range(y0 + 20, y1 - 20, passo):
        for cx in range(x0 + 20, x1 - 20, passo):
            if _fuori(cx, cy):
                continue
            if _cornice(px, cx, cy) >= soglia - 0.18:
                grezzi.append((cx, cy))

    affinati = []
    for cx, cy in grezzi:
        migliore = (0.0, cx, cy)
        for dy in range(-4, 5, 2):
            for dx in range(-4, 5, 2):
                p = _cornice(px, cx + dx, cy + dy)
                if p > migliore[0]:
                    migliore = (p, cx + dx, cy + dy)
        if migliore[0] >= soglia:
            affinati.append(migliore)

    affinati.sort(reverse=True)
    scelti: List[Tuple[int, int]] = []
    for _, cx, cy in affinati:
        if all(abs(cx - a) + abs(cy - b) > distanza_minima for a, b in scelti):
            scelti.append((cx, cy))
    return sorted(scelti, key=lambda p: (p[1], p[0]))


def segna(im: Image.Image, punti: List[Tuple[int, int]], dest: Path) -> Path:
    from PIL import ImageDraw

    out = im.convert("RGB").copy()
    d = ImageDraw.Draw(out)
    for i, (x, y) in enumerate(punti, 1):
        d.ellipse([x - 22, y - 22, x + 22, y + 22], outline=(255, 60, 60), width=3)
        d.text((x - 6, y - 34), str(i), fill=(255, 255, 0))
    out.save(dest)
    return dest


def riconnetti(w, guarda) -> bool:
    """Se c'e' la finestra "RETE DISCONNESSA", preme Conferma e torna True.

    E' l'unica finestra che il bot chiude da solo, e solo perche' la sa
    IDENTIFICARE: legge il testo e trova il pulsante. La regola generale resta
    che una finestra sconosciuta ferma tutto, perche' chiudere alla cieca e' il
    modo piu' rapido per premere qualcosa di costoso.

    Serve davvero: il 29/09/2026 la connessione e' caduta tre volte in una
    mattina, e ogni volta bloccava il lavoro in corso.
    """
    im = guarda()
    if not ocr.trova_testo(im, "connessione persa", 0.75):
        return False
    b = pulsanti.trova_pulsante(im, "CONFERMA", 0.7)
    if not b:
        print("  rete caduta ma non trovo il pulsante Conferma: mi fermo")
        return False
    print("  rete caduta: premo Conferma e riprendo")
    P.click(w, *b.centro, 6.0)
    return e_vista_citta(guarda())


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

    def guarda() -> Image.Image:
        P.bring_to_front(w)
        return Image.open(P.screenshot_window(w, DEST / "_citta.png"))

    im = guarda()
    if not e_vista_citta(im) and riconnetti(w, guarda):
        im = guarda()
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

    def guarda_ora() -> Image.Image:
        P.bring_to_front(w)
        return Image.open(P.screenshot_window(w, DEST / "_dopo.png"))

    raccolte = 0
    for i, (x, y) in enumerate(punti, 1):
        P.click(w, x, y, 1.0)
        dopo = Image.open(P.screenshot_window(w, DEST / "_dopo.png"))
        if not e_vista_citta(dopo):
            # Non tutte le nuvolette sono raccolte: alcune sono indicatori di
            # edifici. Il 29/09/2026 una ha aperto il MUSEO. Si esce con la
            # freccia indietro, che e' navigazione e non un'azione, si verifica
            # di essere tornati in citta' e si tira dritto: fermare tutto per
            # una casella sbagliata su diciassette sarebbe sproporzionato.
            # Se il ritorno NON avviene, li' ci si ferma davvero.
            dopo.save(DEST / "_finestra_inattesa.png")
            print(f"  clic {i} in ({x}, {y}): non era una raccolta, si e' aperta "
                  "una schermata. Esco e proseguo.")
            P.click(w, *INDIETRO, 2.5)
            if not e_vista_citta(guarda_ora()):
                print("  non sono tornato in citta': mi fermo qui.")
                break
            continue

        # Una raccolta riuscita fa sparire LA SUA nuvoletta. Si ricontrolla
        # quel punto, non il totale: il totale balla da solo perche' le
        # nuvolette ondeggiano e ne ricompaiono di nuove, e infatti al primo
        # tentativo passava da 17 a 13 dopo una sola raccolta, fermando tutto.
        # Se la nuvoletta e' ancora li', il clic ha colpito altro - un edificio
        # o una decorazione, che aprono un menu a raggiera senza cambiare
        # schermata, e quel menu contiene voci come "riponi" o "addestra".
        resta = _cornice(dopo.convert("RGB").load(), x, y)
        if resta >= 0.72:
            dopo.save(DEST / "_clic_a_vuoto.png")
            print(f"  clic {i} in ({x}, {y}): la nuvoletta e' ancora li' "
                  f"(cornice {resta:.2f}). Ho colpito qualcosa che non e' una "
                  "raccolta: mi fermo.")
            break
        raccolte += 1
        print(f"  {i}/{len(punti)} raccolto in ({x}, {y})")

    print(f"fatto: {raccolte} raccolte su {len(punti)} candidati")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
