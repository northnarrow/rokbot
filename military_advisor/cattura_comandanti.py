"""Cattura l'elenco completo dei comandanti dal telefono, in sola lettura.

Tocca solo le caselle dell'elenco per selezionarle e fa screenshot: non preme
nessun pulsante che spenda o cambi qualcosa. Da lanciare con la schermata
Comandanti gia' aperta sul telefono.

    python -m military_advisor.cattura_comandanti

Ogni comandante divento una "scheda" PNG in test_telefono/comandanti/schede/,
e alla fine vengono montati fogli da 12 schede da leggere a colpo d'occhio.
Lo script e' riprendibile: le schede gia' salvate non vengono rifatte.

Coordinate: riferimenti_ui/layout_1560x720.json.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import List, Optional

from PIL import Image

from . import adb_tools as A

# Caselle visibili dell'elenco, due per riga, quattro righe.
CASELLE = [(118, 190), (240, 190), (118, 330), (240, 330),
           (118, 470), (240, 470), (118, 610), (240, 610)]

# Ritagli del pannello di destra, nello spazio 1560x720.
TESTA = (1020, 85, 1560, 280)    # epiteto, nome, specialita', stelle, livello
ABILITA = (1090, 465, 1510, 550)  # i cinque riquadri abilita'
NOME = (1020, 85, 1560, 150)      # solo epiteto + nome, per riconoscere i doppioni

# Trascinata lenta e corta: niente inerzia, cosi' lo scorrimento e' prevedibile.
SCORRI_GIU = "input swipe 180 500 180 220 1200"
SCORRI_SU = "input swipe 180 220 180 500 1200"
RIGHE_PER_SCORRIMENTO = 2


SOGLIA_UGUALI = 7.0  # differenza media per pixel sotto la quale due nomi sono lo stesso

# Riconoscimento della schermata. Sapere che il gioco e' visibile NON basta:
# se parte la cattura sulla schermata sbagliata, i tocchi finiscono a caso.
# E' successo il 28/09/2026: il primo tocco in (118, 190) ha centrato l'icona
# della pergamena missioni nell'HUD, si e' aperta la finestra Missioni e gli
# 89 tocchi seguenti sono caduti fuori da quella finestra, senza effetto solo
# per fortuna. Due sonde bastano a distinguerla: il pulsante ABILITA' in basso
# a destra (azzurro acceso) e la freccia indietro in alto a sinistra (chiara).
# Due sonde, perche' la schermata ha due varianti: per i comandanti posseduti
# in basso a destra c'e' il pulsante ABILITA', per quelli non posseduti c'e'
# RICHIAMA. Entrambi sono azzurro acceso, ma in posizioni diverse.
SONDA_ABILITA = (1350, 592, 1440, 628)
SONDA_RICHIAMA = (1210, 615, 1360, 660)
SONDA_INDIETRO = (70, 20, 110, 58)


def _media(im: Image.Image, box) -> tuple:
    b = im.convert("RGB").crop(box).tobytes()
    n = len(b) // 3
    return tuple(round(sum(b[i::3]) / n) for i in range(3))


def _azzurro(rgb) -> bool:
    r, g, b = rgb
    return b > 200 and g > 140 and r < 60


def e_posseduto(im: Image.Image) -> bool:
    """Vero se il comandante mostrato e' posseduto (c'e' ABILITA').

    Serve come condizione di arresto: l'elenco NON finisce ai comandanti
    posseduti, prosegue con tutti gli altri del gioco, che hanno il pulsante
    RICHIAMA e il contatore sculture 0/10 al posto di livello e abilita'.
    """
    return _azzurro(_media(im, SONDA_ABILITA))


def e_schermata_comandanti(im: Image.Image) -> bool:
    return e_posseduto(im) or _azzurro(_media(im, SONDA_RICHIAMA))


# Il menu in basso a destra: chiuso si vede il terreno (verde), aperto i
# pulsanti tondi (azzurri). Misurato sul telefono di test.
SONDA_MENU = (1235, 645, 1295, 690)
BOTTONE_MENU = (1464, 668)
BOTTONE_COMANDANTE = (1263, 670)


def menu_aperto(im: Image.Image) -> bool:
    r, g, b = _media(im, SONDA_MENU)
    return b > 130 and b > r


def vai_a_comandanti(serial: str, dest: Path) -> bool:
    """Apre la schermata Comandanti un passo alla volta, controllando dopo
    ognuno. Niente catene di tocchi a stima: se un passo non da' il risultato
    atteso ci si ferma li', senza mandare il tocco successivo."""
    def guarda() -> Image.Image:
        return Image.open(A.screenshot(serial, dest / "_nav.png"))

    im = guarda()
    if e_schermata_comandanti(im):
        return True

    if not menu_aperto(im):
        A.shell(f"input tap {BOTTONE_MENU[0]} {BOTTONE_MENU[1]}", serial)
        time.sleep(2.0)
        im = guarda()
        if not menu_aperto(im):
            print(f"[ERR] il menu non si e' aperto (sonda {_media(im, SONDA_MENU)}). Mi fermo.")
            return False
    print("[OK ] menu aperto")

    A.shell(f"input tap {BOTTONE_COMANDANTE[0]} {BOTTONE_COMANDANTE[1]}", serial)
    time.sleep(3.5)
    im = guarda()
    if not e_schermata_comandanti(im):
        print(f"[ERR] il tocco su Comandante non ha aperto l'elenco "
              f"(sonde {_media(im, SONDA_ABILITA)}, {_media(im, SONDA_INDIETRO)}). Mi fermo.")
        return False
    return True


def _firma(im: Image.Image) -> List[int]:
    """Firma della testa della scheda, robusta allo sfondo animato.

    Hashare i pixel non funziona: dietro al testo scorre l'arte del comandante,
    quindi lo stesso comandante cambia impronta a ogni screenshot. Nemmeno una
    maschera a soglia funziona, perche' il nome e' scritto scuro su sfondi di
    luminosita' molto diversa. Si riduce invece il riquadro a una miniatura in
    grigi e si confronta per differenza media.

    Si usa tutta la testa della scheda, non solo il nome: con la sola striscia
    del nome due nomi corti e simili come "Guan Yu" e "Sun Tzu" collassano
    nella stessa miniatura e uno dei due sparisce. Epiteto, specialita',
    stelle e livello aggiungono abbastanza differenze da separarli.
    """
    return list(im.convert("L").resize((64, 24), Image.LANCZOS).tobytes())


def _distanza(a: List[int], b: List[int]) -> float:
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def _testa_scheda(p: Path) -> Image.Image:
    im = Image.open(p)
    return im.crop((0, 0, im.width, TESTA[3] - TESTA[1]))


def conta_unici(dest: Path, soglia: float) -> int:
    firme: List[List[int]] = []
    for p in sorted(dest.glob("scheda_*.png")):
        f = _firma(_testa_scheda(p))
        if not any(_distanza(f, g) < soglia for g in firme):
            firme.append(f)
    return len(firme)


def rimonta_unici(dest: Path, soglia: float = SOGLIA_UGUALI) -> List[Path]:
    """Ripassa le schede gia' salvate, scarta i doppioni e rifa' i fogli."""
    for p in dest.glob("*.doppione"):       # ripristina una passata precedente
        p.rename(p.with_suffix(".png"))
    schede = sorted(dest.glob("scheda_*.png"))
    firme: List[List[int]] = []
    unici: List[Path] = []
    for p in schede:
        f = _firma(_testa_scheda(p))
        if any(_distanza(f, g) < soglia for g in firme):
            p.rename(p.with_suffix(".doppione"))
            continue
        firme.append(f)
        unici.append(p)
    print(f"schede: {len(schede)} lette, {len(unici)} uniche, "
          f"{len(schede) - len(unici)} doppioni (soglia {soglia})")
    return unici


def scheda(im: Image.Image) -> Image.Image:
    """Unisce testa e abilita' in una scheda compatta."""
    testa, ab = im.crop(TESTA), im.crop(ABILITA)
    ab = ab.resize((testa.width, int(ab.height * testa.width / ab.width)), Image.LANCZOS)
    out = Image.new("RGB", (testa.width, testa.height + ab.height), (15, 15, 15))
    out.paste(testa, (0, 0))
    out.paste(ab, (0, testa.height))
    return out


def vai_in_cima(serial: str, tentativi: int = 30) -> None:
    for _ in range(tentativi):
        A.shell(SCORRI_SU, serial)
    time.sleep(1.0)


def cattura(serial: str, dest: Path, massimo: int = 200) -> List[Path]:
    """Scorre l'elenco e salva una scheda per comandante. Si ferma da solo
    quando una pagina intera non porta piu' nomi nuovi."""
    dest.mkdir(parents=True, exist_ok=True)
    schede: List[Path] = []

    # Si salva OGNI casella visitata, senza scartare niente qui. Il confronto
    # fra schede e' delicato da tarare e va fatto dopo, su file, dove si puo'
    # provare piu' di una soglia senza rifare il giro sul telefono.
    while len(schede) < massimo:
        for x, y in CASELLE:
            A.shell(f"input tap {x} {y}", serial)
            time.sleep(1.6)
            im = Image.open(A.screenshot(serial, dest / "_ultimo.png"))
            if not e_posseduto(im):
                print("  raggiunti i comandanti non posseduti: fine dell'elenco")
                return schede
            p = dest / f"scheda_{len(schede):03d}.png"
            scheda(im).save(p)
            schede.append(p)
            print(f"  {len(schede):3d} catturato")
            if len(schede) >= massimo:
                return schede
        for _ in range(len(CASELLE) // 2 // RIGHE_PER_SCORRIMENTO):
            A.shell(SCORRI_GIU, serial)
        time.sleep(0.8)
    return schede


def monta(schede: List[Path], dest: Path, per_foglio: int = 12, colonne: int = 3) -> List[Path]:
    fogli = []
    for n in range(0, len(schede), per_foglio):
        gruppo = [Image.open(p) for p in schede[n:n + per_foglio]]
        w, h = gruppo[0].width, gruppo[0].height
        righe = (len(gruppo) + colonne - 1) // colonne
        foglio = Image.new("RGB", (w * colonne, h * righe), (15, 15, 15))
        for i, im in enumerate(gruppo):
            foglio.paste(im, ((i % colonne) * w, (i // colonne) * h))
        p = dest / f"foglio_{n // per_foglio + 1:02d}.png"
        foglio.save(p)
        fogli.append(p)
    return fogli


def main(argv: Optional[List[str]] = None) -> int:
    import sys
    argv = sys.argv[1:] if argv is None else argv
    dest = Path("test_telefono/comandanti/schede")

    if "--rimonta" in argv:
        unici = rimonta_unici(dest)
        for f in monta(unici, dest.parent):
            print("foglio:", f)
        return 0

    serial = A.pick_device()
    stato = A.game_visible(serial, Path("test_telefono"))
    if not stato["ok"]:
        print(f"[ERR] {stato['motivo']}")
        return 1
    print(f"[OK ] {stato['motivo']}, telefono {serial}")

    if not vai_a_comandanti(serial, Path("test_telefono")):
        print("      Apri a mano Menu -> Comandante sul telefono e rilancia.")
        return 1
    print("[OK ] schermata Comandanti riconosciuta")

    print("torno in cima all'elenco...")
    vai_in_cima(serial)

    print("cattura in corso:")
    schede = cattura(serial, dest)
    print(f"catturati {len(schede)} comandanti")

    fogli = monta(schede, dest.parent)
    for f in fogli:
        print("foglio:", f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
