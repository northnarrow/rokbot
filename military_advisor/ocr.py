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

import difflib
import os
import shutil
import sys
from dataclasses import dataclass
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


# --------------------------------------------------- lettura dell'intera schermata
# I riquadri predefiniti non scalano: per coprire tutto il gioco servirebbero
# centinaia di caselle scritte a mano, e un aggiornamento le romperebbe tutte.
# Qui invece si legge quello che c'e', con posizione e confidenza, e poi si
# cerca il testo che interessa. Sapere DOVE e' scritto "Caserma" significa
# anche sapere dove cliccare: e' la stessa cosa che serve alla mappa citta'.

@dataclass
class Parola:
    testo: str
    riquadro: Tuple[int, int, int, int]   # x1, y1, x2, y2
    confidenza: int

    @property
    def centro(self) -> Tuple[int, int]:
        x1, y1, x2, y2 = self.riquadro
        return (x1 + x2) // 2, (y1 + y2) // 2


def parole(im: Image.Image, lingua: str = "ita", confidenza_minima: int = 55,
           scala: int = 3, riquadri: int = 1) -> List[Parola]:
    """Tutte le parole leggibili nella schermata, con posizione e confidenza.

    Due accorgimenti, entrambi misurati:

    Si legge in ENTRAMBE LE POLARITA': l'interfaccia mescola testo chiaro su
    fondo scuro e viceversa nella stessa schermata, e una sola passata ne
    perde sempre meta'.

    ``riquadri`` > 1 elabora l'immagine a zone separate, ognuna con il proprio
    autocontrasto. Aiuta dove il testo sta sopra un'illustrazione, ma NON e'
    l'impostazione predefinita: misurato il 29/09/2026, a 3x3 riquadri si
    leggono piu' parole (115 contro 48 sulla schermata citta') ma la copertura
    delle etichette SCENDE dal 64% al 60%, perche' le etichette di piu' parole
    finiscono a cavallo fra due zone e non si ricompongono. Leggere di piu'
    non vuol dire capire di piu'.
    """
    pt = _pytesseract()
    trovate: List[Parola] = []
    visti = set()
    L, A = im.width, im.height
    passo_x, passo_y = L // riquadri, A // riquadri
    bordo = 40  # sovrapposizione, per non tagliare le parole sul confine

    zone = [(max(0, cx * passo_x - bordo), max(0, cy * passo_y - bordo),
             min(L, (cx + 1) * passo_x + bordo), min(A, (cy + 1) * passo_y + bordo))
            for cy in range(riquadri) for cx in range(riquadri)]

    for zx1, zy1, zx2, zy2 in zone:
        zona = im.crop((zx1, zy1, zx2, zy2))
        for inverti in (False, True):
            try:
                d = pt.image_to_data(_prepara(zona, scala, inverti), lang=lingua,
                                     config="--psm 11", output_type=pt.Output.DICT)
            except Exception:  # noqa: BLE001
                continue
            for i, testo in enumerate(d["text"]):
                t = testo.strip()
                if not t:
                    continue
                try:
                    conf = int(float(d["conf"][i]))
                except (ValueError, TypeError):
                    continue
                if conf < confidenza_minima:
                    continue
                x = zx1 + d["left"][i] // scala
                y = zy1 + d["top"][i] // scala
                w, h = d["width"][i] // scala, d["height"][i] // scala
                chiave = (t.lower(), x // 10, y // 10)
                if chiave in visti:
                    continue
                visti.add(chiave)
                trovate.append(Parola(t, (x, y, x + w, y + h), conf))
    return sorted(trovate, key=lambda p: (p.riquadro[1], p.riquadro[0]))


def righe(ps: List[Parola], tolleranza: int = 12) -> List[str]:
    """Rimette insieme le parole che stanno sulla stessa riga."""
    out: List[str] = []
    corrente: List[Parola] = []
    for p in ps:
        if corrente and abs(p.riquadro[1] - corrente[-1].riquadro[1]) > tolleranza:
            out.append(" ".join(q.testo for q in corrente))
            corrente = []
        corrente.append(p)
    if corrente:
        out.append(" ".join(q.testo for q in corrente))
    return out


def gruppi(ps: List[Parola], massimo: int = 5, tolleranza: int = 14) -> List[Parola]:
    """Parole singole piu' le sequenze di parole vicine sulla stessa riga.

    Serve perche' quasi nessuna etichetta del gioco e' una parola sola:
    "Punteggio condotta", "Scipione l'Africano", "Formazione a cuneo".
    Cercandole fra le singole parole non si trovano mai, anche quando l'OCR
    le ha lette benissimo - erano solo spezzate in due.
    """
    out = list(ps)
    for i, p in enumerate(ps):
        testo = p.testo
        x1, y1, x2, y2 = p.riquadro
        for q in ps[i + 1:i + massimo]:
            if abs(q.riquadro[1] - p.riquadro[1]) > tolleranza:
                break
            if q.riquadro[0] < x2 - 5 or q.riquadro[0] - x2 > 60:
                break
            testo += " " + q.testo
            x2 = max(x2, q.riquadro[2])
            y1, y2 = min(y1, q.riquadro[1]), max(y2, q.riquadro[3])
            out.append(Parola(testo, (x1, y1, x2, y2),
                              min(p.confidenza, q.confidenza)))
    return out


def trova_testo(im: Optional[Image.Image], cercato: str, soglia: float = 0.8,
                ps: Optional[List[Parola]] = None) -> Optional[Parola]:
    """Cerca un testo nella schermata e ne restituisce posizione e centro.

    E' il mattone che serve per cliccare "quel pulsante li'" senza conoscerne
    le coordinate in anticipo.
    """
    ps = ps if ps is not None else parole(im)
    migliore, punteggio = None, 0.0
    for p in gruppi(ps):
        r = _somiglianza(p.testo, cercato)
        if r > punteggio:
            migliore, punteggio = p, r
    return migliore if punteggio >= soglia else None


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
    if not b:
        return 0.0
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


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


# Copertura su schermate diverse del gioco: per ognuna, etichette che si
# sanno esserci. Misura quanto il bot "vede" davvero, invece di fidarsi di
# qualche riquadro scelto bene.
COPERTURA = [
    ("test_telefono/schermate/08_impostazioni.png", "impostazioni (telefono)",
     ["Notifiche", "Account", "Lingua", "Emoji", "Punteggio condotta", "Personaggi",
      "Comunità", "Termini di servizio"]),
    ("test_pc/a03.png", "comandanti (PC)",
     ["Scipione l'Africano", "Eroe di Zama", "TALENTI", "Livello", "Fanteria",
      "Versatilità", "Supporto"]),
    ("test_pc/a04.png", "formazione (PC)",
     ["FORMAZIONE", "Formazione a cuneo", "CODICE", "RICICLA", "Info armamento",
      "Attacco della fanteria"]),
    ("test_pc/a05.png", "codice armamenti (PC)",
     ["Leggendario", "Epico", "FONTE", "Pergamena del nord", "Inscrizione",
      "Formazione a cuneo"]),
    ("test_pc/b02.png", "inventario + filtri (PC)",
     ["ARMAMENTI", "Qualità", "RESET", "Leggendario", "Pergamena", "Bandiera",
      "Emblema", "Formazione", "Generazione"]),
    ("test_pc/b01.png", "citta (PC)",
     ["Costruisci", "Comando", "feudale"]),
    ("test_telefono/schermate/01_profilo.png", "profilo (telefono)",
     ["Governatore", "Potenza", "Classifica", "Truppe", "Impostazioni"]),
    ("test_telefono/schermate/13_ricerca_mappa.png", "ricerca mappa (telefono)",
     ["Barbari", "CERCA", "Livello"]),
]


def copertura() -> int:
    print(f"tesseract: {percorso_tesseract()}\n")
    tot_ok = tot = 0
    for f, nome, attese in COPERTURA:
        p = Path(f)
        if not p.exists():
            print(f"[--- ] {nome}: manca {f}")
            continue
        ps = parole(Image.open(p))
        trovate = [e for e in attese if trova_testo(None, e, 0.8, ps) is not None]
        tot_ok += len(trovate)
        tot += len(attese)
        mancanti = [e for e in attese if e not in trovate]
        stato = "OK " if not mancanti else "ERR"
        print(f"[{stato}] {nome}: {len(trovate)}/{len(attese)} "
              f"({len(ps)} parole lette)")
        if mancanti:
            print(f"       non trovate: {', '.join(mancanti)}")
    pct = 100 * tot_ok / tot if tot else 0
    print(f"\ncopertura: {tot_ok}/{tot} etichette trovate ({pct:.0f}%)")
    return 0 if tot_ok == tot else 1


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--copertura" in argv:
        return copertura()
    if "--prova" in argv:
        return prova()
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
