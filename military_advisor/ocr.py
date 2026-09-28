"""Lettura del testo dalle schermate del gioco.

Finche' non c'e' questo, il bot e' cieco: sa confrontare colori e forme, ma
non sa dire *cosa* c'e' scritto. Serve soprattutto a ``city_map``, che dopo
aver toccato un edificio deve leggere il nome nella finestra per confermare
di aver aperto quello giusto.

Richiede Tesseract con la lingua italiana:
    winget install --id tesseract-ocr.tesseract
    pip install pytesseract

Autoverifica su schermate reali di cui si conosce il contenuto:
    python -m military_advisor.ocr --prova
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image, ImageOps

PERCORSI_NOTI = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
)


def percorso_tesseract() -> str:
    p = os.environ.get("TESSERACT_PATH") or shutil.which("tesseract")
    if p:
        return p
    for c in PERCORSI_NOTI:
        if Path(c).exists():
            return c
    raise RuntimeError(
        "Tesseract non trovato. Installalo con "
        "'winget install --id tesseract-ocr.tesseract' oppure imposta TESSERACT_PATH."
    )


def _pytesseract():
    try:
        import pytesseract
    except ImportError as exc:
        raise RuntimeError("manca pytesseract: esegui  pip install pytesseract") from exc
    pytesseract.pytesseract.tesseract_cmd = percorso_tesseract()
    return pytesseract


def _prepara(im: Image.Image, scala: int, inverti: bool) -> Image.Image:
    g = im.convert("L")
    g = g.resize((g.width * scala, g.height * scala), Image.LANCZOS)
    g = ImageOps.autocontrast(g)
    if inverti:
        g = ImageOps.invert(g)
    return g


def leggi(im: Image.Image, box: Optional[Tuple[int, int, int, int]] = None,
          lingua: str = "ita", riga_singola: bool = False, scala: int = 4,
          lista_bianca: Optional[str] = None) -> str:
    """Legge il testo da un'immagine, o da un suo riquadro.

    Il testo del gioco a volte e' chiaro su fondo scuro e a volte il
    contrario, e non si sa in anticipo quale dei due: si prova in entrambe le
    polarita' e si tiene il risultato piu' sostanzioso. Costa il doppio ma
    evita di dover indovinare riquadro per riquadro.
    """
    pt = _pytesseract()
    ritaglio = im.crop(box) if box else im
    psm = "7" if riga_singola else "6"
    config = f"--psm {psm}"
    if lista_bianca:
        config += f" -c tessedit_char_whitelist={lista_bianca}"
    risultati: List[str] = []
    for inverti in (False, True):
        try:
            t = pt.image_to_string(_prepara(ritaglio, scala, inverti), lang=lingua, config=config)
        except Exception:  # noqa: BLE001
            t = ""
        risultati.append(" ".join(t.split()))
    return max(risultati, key=lambda s: (len(s.replace(" ", "")), s.count(" ")))


def leggi_numero(im: Image.Image, box=None, scala: int = 4) -> Optional[int]:
    """Legge un numero intero, tollerando i separatori delle migliaia.

    Nel client italiano il punto separa le migliaia: '29.756' e' 29756.
    """
    testo = leggi(im, box, lingua="ita", riga_singola=True, scala=scala)
    cifre = "".join(c for c in testo if c.isdigit())
    return int(cifre) if cifre else None


# ------------------------------------------------------------------- risorse
# Riquadri della barra risorse del client PC a 1796x1040. Partono DOPO
# l'icona: includendola, l'OCR la legge come punteggiatura e restituisce
# cose come "è 15.5M i".
RISORSE_PC = {
    # La larghezza del riquadro non ha un verso "giusto": allargarlo ha
    # risolto le gemme e peggiorato il cibo. Questi valori sono quelli che
    # danno il risultato migliore misurato, non una regola generale.
    "cibo":   (1232, 38, 1302, 70),
    "legno":  (1352, 38, 1422, 70),
    "pietra": (1462, 38, 1548, 70),
    "oro":    (1583, 38, 1663, 70),
    # Riquadro piu' largo: stretto, i tre ingrandimenti concordavano tutti su
    # 29.156 mentre il valore vero e' 29.756, cioe' un numero sbagliato dato
    # per certo. Largo, non concordano e il valore esce come "non sicuro":
    # meno comodo ma non bugiardo.
    "gemme":  (1694, 34, 1786, 74),
}


def valore(testo: str) -> Optional[int]:
    """Converte quello che mostra il gioco in un numero.

    Il punto ha due significati diversi a seconda del contesto: in '9.5M' e'
    decimale, in '29.756' separa le migliaia. Il discriminante e' il suffisso.
    """
    t = "".join(c for c in testo if c.isdigit() or c in ".,MKmk").replace(",", ".")
    if not t:
        return None
    molt = 1
    if t[-1] in "Mm":
        molt, t = 1_000_000, t[:-1]
    elif t[-1] in "Kk":
        molt, t = 1_000, t[:-1]
    t = t.strip(".")
    if not t:
        return None
    try:
        if molt > 1:
            return int(float(t) * molt)
        return int(t.replace(".", ""))
    except ValueError:
        return None


CIFRE = "0123456789.MK"

# Scala 5, non di piu'. Misurato il 29/09/2026 sul valore del legno: a scala 5
# con lista bianca esce "9.7M", a scala 8 e 12 il punto decimale sparisce e
# diventa "97M", cioe' dieci volte tanto. Ingrandire non e' sempre meglio.
SCALA_NUMERI = 5


SCALE_CONTROLLO = (4, 5, 6)


def numero_stabile(im: Image.Image, box) -> Optional[int]:
    """Legge un numero a piu' ingrandimenti e lo restituisce solo se
    coincidono TUTTI.

    Si chiede l'unanimita', non la maggioranza. Sul contatore delle gemme le
    letture erano 29.156 (tre volte) e 29.756 (una volta), e quella giusta
    era la seconda: un voto a maggioranza avrebbe restituito con sicurezza il
    numero sbagliato. Meglio che il bot dica "non lo so" e chieda, piuttosto
    che decidere su un numero inventato.
    """
    letture = {valore(leggi(im, box, riga_singola=True, scala=s, lista_bianca=CIFRE))
               for s in SCALE_CONTROLLO}
    if len(letture) == 1:
        return letture.pop()
    return None


def leggi_risorse(im: Image.Image, riquadri=None) -> dict:
    """Legge la barra risorse. Ritorna {'cibo': int|None, ...}.

    ``None`` significa "non sono sicuro", non "zero": chi chiama deve
    trattarlo come dato mancante.
    """
    riquadri = riquadri or RISORSE_PC
    return {k: numero_stabile(im, b) for k, b in riquadri.items()}


# ---------------------------------------------------------------- autoverifica
# Schermate reali gia' salvate, con quello che c'e' scritto davvero. Serve a
# misurare l'OCR invece di fidarsi dell'impressione che "sembra funzionare".
# Il riquadro va tenuto largo: tagliare la prima lettera costa un carattere
# ("Scipione" letto "icipione"), e l'icona che precede l'epiteto viene letta
# come segni di punteggiatura, quindi va lasciata fuori.
CASI = [
    ("test_pc/a03.png", (1386, 282, 1748, 334), "Scipione l'Africano", False, 4),
    ("test_pc/a03.png", (1412, 250, 1548, 285), "Eroe di Zama", True, 6),
    ("test_pc/a04.png", (1448, 218, 1790, 262), "Formazione a cuneo", True, 4),
    ("test_pc/b04.png", (1232, 440, 1570, 484), "Pergamena del nord", True, 4),
    ("test_pc/b04.png", (1232, 486, 1570, 514), "Per Formazione ad arco", True, 4),
    ("test_pc/a01.png", (1240, 440, 1570, 484), "Pergamena del nord", True, 4),
]


def _somiglianza(a: str, b: str) -> float:
    a, b = a.lower(), b.lower()
    if not b:
        return 0.0
    comuni = sum(1 for c in set(b) if c in a)
    import difflib
    return difflib.SequenceMatcher(None, a, b).ratio()


# Barra risorse di test_pc/live3.png, con i valori veri letti a occhio.
# Serve a sorvegliare anche i numeri, non solo il testo: sui numeri gli
# errori sono peggiori, perche' un punto decimale perso vale dieci volte.
CASI_NUMERI = ("test_pc/live3.png", {
    "cibo": 9_500_000, "legno": 9_700_000, "pietra": 15_500_000,
    "oro": 18_300_000, "gemme": 29_756,
})


def prova_numeri() -> Tuple[int, int]:
    f, attesi = CASI_NUMERI
    p = Path(f)
    if not p.exists():
        print(f"[--- ] {f}: manca")
        return 0, 0
    letti = leggi_risorse(Image.open(p))
    ok = 0
    for k, atteso in attesi.items():
        v = letti.get(k)
        if v == atteso:
            ok += 1
            print(f"[OK ] {k:7} {v:,}".replace(",", "."))
        elif v is None:
            print(f"[?  ] {k:7} non sicuro (vero {atteso:,})".replace(",", "."))
        else:
            print(f"[ERR] {k:7} letto {v:,}, vero {atteso:,}".replace(",", "."))
    return ok, len(attesi)


def prova() -> int:
    print(f"tesseract: {percorso_tesseract()}")
    ok = 0
    for f, box, atteso, riga, scala in CASI:
        p = Path(f)
        if not p.exists():
            print(f"[--- ] {f}: manca")
            continue
        letto = leggi(Image.open(p), box, riga_singola=riga, scala=scala)
        r = _somiglianza(letto, atteso)
        buono = r >= 0.75
        ok += buono
        print(f"[{'OK ' if buono else 'ERR'}] atteso {atteso!r}")
        print(f"       letto  {letto!r}  (somiglianza {r:.2f})")
    print(f"\ntesto: {ok}/{len(CASI)} riquadri corretti")
    print("\nnumeri della barra risorse:")
    nok, ntot = prova_numeri()
    print(f"\nnumeri: {nok}/{ntot} corretti "
          f"(quelli marcati '?' il bot li dichiara non sicuri, non li inventa)")
    return 0 if ok == len(CASI) else 1


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--prova" in argv:
        return prova()
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
