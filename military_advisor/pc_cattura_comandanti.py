"""Cattura la scheda di ogni comandante dal client PC.

SOLA LETTURA. Seleziona le caselle dell'elenco e scorre: non preme Talenti,
Abilita', Richiama ne' altro. Tutti i clic restano dentro il pannello di
sinistra.

Da lanciare con la schermata Comandanti gia' aperta (tasto P in citta'):

    python -m military_advisor.pc_cattura_comandanti            cattura
    python -m military_advisor.pc_cattura_comandanti --rimonta  solo rimontaggio

Come per la versione telefono, si salva OGNI casella visitata e i doppioni si
tolgono dopo, su file: la soglia di somiglianza e' delicata da tarare e non
vale la pena rifare il giro sul gioco per cambiarla.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional

from PIL import Image

from . import pc_tools as P

DEST = Path("test_pc/comandanti")

# Caselle dell'elenco: due colonne, sei righe.
COLONNE = (79, 197)
RIGHE = (235, 368, 502, 635, 768, 900)

# Ritagli del pannello di destra.
TESTA = (1290, 250, 1796, 530)     # epiteto, nome, specialita', stelle, livello, capacita'
ABILITA = (1390, 630, 1770, 712)   # i cinque riquadri abilita'
POTERE = (690, 932, 1060, 982)     # "Potere del comandante"

# Sonde. Sulla schermata comandanti i due pulsanti in basso a destra sono
# azzurro pieno; sul Codice la sola zona di ABILITA' e' azzurrina ma non
# passa la soglia, e TALENTI no. Servono entrambi per non confondersi.
SONDA_TALENTI = (1410, 745, 1550, 800)
SONDA_ABILITA = (1600, 745, 1745, 800)

PUNTO_ROTELLA = (140, 600)

# Soglia di somiglianza sotto la quale due schede sono lo stesso comandante.
# Tarata il 28/09/2026 contro un riferimento indipendente: l'intestazione
# dell'elenco dichiara 78 comandanti posseduti, e 2.4 e' il valore che
# restituisce esattamente 78 su 228 schede catturate (2.2 ne da' 80, 2.6 ne
# da' 75). Va ritarata se cambia la dimensione della finestra o il ritaglio.
SOGLIA_UGUALI = 2.4


def _media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def _azzurro(rgb) -> bool:
    r, g, b = rgb
    return b > 200 and g > 140 and r < 60


def e_posseduto(im: Image.Image) -> bool:
    """Vero se il comandante mostrato e' posseduto.

    L'elenco non finisce ai posseduti: prosegue con tutti gli altri del gioco,
    che al posto di Talenti e Abilita' hanno il pulsante Richiama.
    """
    return _azzurro(_media(im, SONDA_TALENTI)) and _azzurro(_media(im, SONDA_ABILITA))


def _firma(im: Image.Image) -> List[int]:
    return list(im.convert("L").resize((64, 24), Image.LANCZOS).tobytes())


def _distanza(a: List[int], b: List[int]) -> float:
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def scheda(im: Image.Image) -> Image.Image:
    testa, ab, pot = im.crop(TESTA), im.crop(ABILITA), im.crop(POTERE)
    pezzi = []
    for p in (ab, pot):
        pezzi.append(p.resize((testa.width, int(p.height * testa.width / p.width)), Image.LANCZOS))
    out = Image.new("RGB", (testa.width, testa.height + sum(p.height for p in pezzi)), (12, 12, 12))
    out.paste(testa, (0, 0))
    y = testa.height
    for p in pezzi:
        out.paste(p, (0, y))
        y += p.height
    return out


def conta_unici(dest: Path, soglia: float) -> int:
    firme: List[List[int]] = []
    for p in sorted(dest.glob("scheda_*.png")):
        f = _firma(Image.open(p).crop((0, 0, TESTA[2] - TESTA[0], TESTA[3] - TESTA[1])))
        if not any(_distanza(f, g) < soglia for g in firme):
            firme.append(f)
    return len(firme)


def rimonta(dest: Path, soglia: float = SOGLIA_UGUALI, per_foglio: int = 6) -> List[Path]:
    for p in dest.glob("*.doppione"):
        p.rename(p.with_suffix(".png"))
    schede = sorted(dest.glob("scheda_*.png"))
    firme: List[List[int]] = []
    unici: List[Path] = []
    for p in schede:
        f = _firma(Image.open(p).crop((0, 0, TESTA[2] - TESTA[0], TESTA[3] - TESTA[1])))
        if any(_distanza(f, g) < soglia for g in firme):
            p.rename(p.with_suffix(".doppione"))
            continue
        firme.append(f)
        unici.append(p)
    print(f"schede: {len(schede)} lette, {len(unici)} uniche, {len(schede)-len(unici)} doppioni (soglia {soglia})")

    fogli = []
    for n in range(0, len(unici), per_foglio):
        gruppo = [Image.open(p) for p in unici[n:n + per_foglio]]
        w, h = gruppo[0].width, gruppo[0].height
        righe = (len(gruppo) + 1) // 2
        f = Image.new("RGB", (w * 2, h * righe), (12, 12, 12))
        for i, im in enumerate(gruppo):
            f.paste(im, ((i % 2) * w, (i // 2) * h))
        p = dest.parent / f"comandanti_{n // per_foglio + 1:02d}.png"
        f.save(p)
        fogli.append(p)
    return fogli


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    DEST.mkdir(parents=True, exist_ok=True)

    if "--rimonta" in argv:
        for f in rimonta(DEST):
            print("foglio:", f)
        return 0

    if sys.platform != "win32":
        print("[ERR] serve Windows con il client PC aperto")
        return 1

    w = P.find_game_window()
    if not P.bring_to_front(w):
        print("[ERR] non riesco a portare davanti la finestra del gioco")
        return 1
    d = P.fissa_dimensioni(w)
    print(f"[OK ] finestra {d[0]}x{d[1]}: se cambia dimensione i clic si fermano")

    def guarda() -> Image.Image:
        return Image.open(P.screenshot_window(w, DEST / "_ultimo.png"))

    im = guarda()
    if not e_posseduto(im):
        print(f"[ERR] non siamo sulla schermata Comandanti "
              f"(sonde {_media(im, SONDA_TALENTI)}, {_media(im, SONDA_ABILITA)}).")
        print("      In citta' premi P, oppure aprila a mano, e rilancia.")
        return 1
    print("[OK ] schermata Comandanti riconosciuta")

    P.scroll(w, PUNTO_ROTELLA[0], PUNTO_ROTELLA[1], 30)   # torna in cima

    schede: List[Path] = []
    for pagina in range(1, 20):
        for y in RIGHE:
            for x in COLONNE:
                P.click(w, x, y, 0.7)
                im = guarda()
                if not e_posseduto(im):
                    im.save(DEST / "_primo_non_posseduto.png")
                    print("  raggiunti i comandanti non posseduti: fine dell'elenco")
                    print(f"catturate {len(schede)} schede")
                    return 0
                p = DEST / f"scheda_{len(schede):03d}.png"
                scheda(im).save(p)
                schede.append(p)
                print(f"  {len(schede):3d} catturato")
        P.scroll(w, PUNTO_ROTELLA[0], PUNTO_ROTELLA[1], -5)

    print(f"catturate {len(schede)} schede")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
