"""Registra i tocchi fatti a mano sul telefono, per imparare dove sono le cose.

L'idea e' del proprietario ed e' buona: invece di cercare le coordinate a
tentoni sugli screenshot, gliele si fa mostrare una volta sola. ADB legge il
touchscreen con ``getevent``, quindi una sequenza fatta a mano si puo'
registrare e poi rieseguire.

## Come va usata, e come no

Registrare e ripetere alla cieca e' la trappola. Una macro riprodotta non
guarda lo schermo: se compare un popup, se una coda e' in un altro stato, se
il gioco si disconnette - ed e' successo tre volte in una mattina - i tocchi
partono lo stesso, addosso a qualunque cosa ci sia sotto. E' esattamente il
guasto che il 28/09/2026 ha mandato 90 tocchi a caso sulla schermata
sbagliata.

Quindi qui la registrazione fa il MAESTRO, non l'esecutore:

  1. la sequenza la fai tu a mano, una volta;
  2. si estraggono coordinate e ordine dei passi;
  3. da quelle si genera uno scheletro dove OGNI passo e' precedutoo da una
     verifica, e il bot si ferma se non riconosce dove si trova.

Cosi' si prende il vantaggio della macro - non devo indovinare le coordinate
- senza il suo difetto, che e' agire alla cieca.

    python -m military_advisor.registratore --nome apri_vip --registra 20
    python -m military_advisor.registratore --mostra apri_vip
    python -m military_advisor.registratore --genera apri_vip

## Nota tecnica

Le coordinate di ``getevent`` stanno nello spazio del TOUCHSCREEN, che di
solito ha una risoluzione diversa dallo schermo: vanno riscalate sui massimi
dichiarati da ``getevent -p``. Qui si riscalano sulle dimensioni dello
screenshot, che sono anche quelle in cui lavora ``input tap``.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional, Tuple

from . import adb_tools as A

DEST = Path("test_telefono/macro")

SOGLIA_TAP = 25          # spostamento sotto il quale e' un tocco, non una trascinata
PAUSA_MINIMA = 0.25      # pause piu' corte non si riportano: sono rumore


@dataclass
class Gesto:
    tipo: str                  # "tocca" oppure "trascina"
    x: int
    y: int
    x2: Optional[int] = None
    y2: Optional[int] = None
    durata_ms: int = 0
    attesa_dopo: float = 0.0

    def __str__(self) -> str:
        if self.tipo == "tocca":
            return f"tocca ({self.x}, {self.y})  pausa dopo {self.attesa_dopo}s"
        return (f"trascina ({self.x}, {self.y}) -> ({self.x2}, {self.y2})  "
                f"{self.durata_ms}ms  pausa dopo {self.attesa_dopo}s")


def trova_touchscreen(serial: str) -> Tuple[str, int, int]:
    """Nome del device di input del touchscreen e massimi dei suoi assi."""
    testo = A.shell("getevent -p", serial)
    device = maxx = maxy = None
    corrente = None
    for riga in testo.splitlines():
        m = re.search(r"add device \d+: (\S+)", riga)
        if m:
            corrente = m.group(1)
        m = re.search(r"0035\s*:.*max\s+(\d+)", riga)      # ABS_MT_POSITION_X
        if m and corrente:
            device, maxx = corrente, int(m.group(1))
        m = re.search(r"0036\s*:.*max\s+(\d+)", riga)      # ABS_MT_POSITION_Y
        if m and corrente == device:
            maxy = int(m.group(1))
    if not (device and maxx and maxy):
        raise RuntimeError("touchscreen non trovato fra i device di 'getevent -p'")
    return device, maxx, maxy


def registra(serial: str, secondi: int) -> List[Gesto]:
    """Ascolta il touchscreen per N secondi e restituisce i gesti fatti."""
    device, maxx, maxy = trova_touchscreen(serial)
    DEST.mkdir(parents=True, exist_ok=True)
    largh, alt = A.png_size(A.screenshot(serial, DEST / "_registra.png")) or (1560, 720)
    print(f"  touchscreen {device}, assi {maxx}x{maxy}; schermo {largh}x{alt}")
    print(f"  registro per {secondi} secondi: fai la sequenza sul telefono adesso")

    cmd = [A.adb_path(), "-s", serial, "shell", f"getevent -lt {device}"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    time.sleep(secondi)
    proc.terminate()
    grezzo = proc.stdout.read().decode(errors="replace") if proc.stdout else ""
    (DEST / "_grezzo.txt").write_text(grezzo, encoding="utf-8")

    gesti: List[Gesto] = []
    t0 = px = py = None
    primo_x = primo_y = None
    ultimo_fine = None
    for riga in grezzo.splitlines():
        m = re.match(r"\[\s*([\d.]+)\]\s+\S+\s+(\S+)\s+(\S+)", riga)
        if not m:
            continue
        t, codice, valore = float(m.group(1)), m.group(2), m.group(3)
        if codice == "ABS_MT_POSITION_X":
            px = int(valore, 16) * largh // maxx
        elif codice == "ABS_MT_POSITION_Y":
            py = int(valore, 16) * alt // maxy
        elif codice == "ABS_MT_TRACKING_ID":
            if valore.lower() not in ("ffffffff", "-1"):          # dito giu'
                t0, primo_x, primo_y = t, px, py
            elif t0 is not None and primo_x is not None:          # dito su
                attesa = 0.0
                if ultimo_fine is not None and t - ultimo_fine > PAUSA_MINIMA:
                    attesa = round(t - ultimo_fine, 2)
                fx, fy = (px if px is not None else primo_x), (py if py is not None else primo_y)
                if abs(fx - primo_x) + abs(fy - primo_y) < SOGLIA_TAP:
                    gesti.append(Gesto("tocca", primo_x, primo_y, attesa_dopo=attesa))
                else:
                    gesti.append(Gesto("trascina", primo_x, primo_y, fx, fy,
                                       int((t - t0) * 1000), attesa))
                ultimo_fine = t
                t0 = None
    return gesti


def salva(nome: str, gesti: List[Gesto]) -> Path:
    DEST.mkdir(parents=True, exist_ok=True)
    p = DEST / f"{nome}.json"
    p.write_text(json.dumps([asdict(g) for g in gesti], ensure_ascii=False, indent=2),
                 encoding="utf-8")
    return p


def carica(nome: str) -> List[Gesto]:
    return [Gesto(**d) for d in
            json.loads((DEST / f"{nome}.json").read_text(encoding="utf-8"))]


def genera_script(nome: str, gesti: List[Gesto]) -> str:
    """Scheletro con una verifica PRIMA di ogni passo.

    Le verifiche restano da riempire apposta: sono il punto in cui si decide
    che cosa il bot deve riconoscere per avere il diritto di toccare.
    Lasciarle vuote farebbe una macro cieca, cioe' proprio la cosa da evitare.
    """
    r = [
        f'"""Sequenza imparata dai tocchi: {nome}.',
        "",
        "Generato da registratore.py. Ogni passo ha una verifica DA RIEMPIRE:",
        "finche' restano vuote questa e' una macro cieca e non va lanciata.",
        '"""',
        "",
        "from pathlib import Path",
        "",
        "",
        f"def {nome}(disp, guarda):",
    ]
    for i, g in enumerate(gesti, 1):
        r.append(f"    # passo {i}: verifica di essere dove ci si aspetta, poi agisci")
        r.append("    # if not riconosci(guarda()): return False")
        if g.tipo == "tocca":
            r.append(f"    disp.tocca({g.x}, {g.y}, {max(g.attesa_dopo, 0.8)})")
        else:
            r.append(f"    disp.trascina({g.x}, {g.y}, {g.x2}, {g.y2}, {g.durata_ms})")
        r.append("")
    r.append("    return True")
    return "\n".join(r) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    def opzione(nome: str, default: Optional[str] = None) -> Optional[str]:
        if nome in argv and argv.index(nome) + 1 < len(argv):
            return argv[argv.index(nome) + 1]
        return default

    nome = opzione("--nome", "macro") or "macro"

    if "--registra" in argv:
        serial = A.pick_device()
        gesti = registra(serial, int(opzione("--registra", "15") or 15))
        p = salva(nome, gesti)
        print(f"  {len(gesti)} gesti registrati -> {p}")
        for g in gesti:
            print("   ", g)
        return 0
    if "--mostra" in argv:
        for g in carica(opzione("--mostra", nome) or nome):
            print("   ", g)
        return 0
    if "--genera" in argv:
        n = opzione("--genera", nome) or nome
        p = DEST / f"{n}.py"
        p.write_text(genera_script(n, carica(n)), encoding="utf-8")
        print(f"scheletro scritto in {p}; le verifiche sono da riempire")
        return 0

    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
