"""Mappa della città del giocatore, imparata e verificata dal bot.

In Rise of Kingdoms gli edifici si possono spostare e cambiano aspetto con
l'era e il livello: coordinate fisse non funzionano. Questo modulo tiene la
logica, indipendente da PC o telefono:

1. le posizioni sono salvate in coordinate RELATIVE allo schermo (0-1), valide
   solo con la telecamera nella posizione standard (città centrata);
2. prima di usare una posizione il bot tocca, legge il nome dell'edificio
   nella finestra che si apre (OCR) e lo confronta con quello atteso;
3. se non combacia, l'edificio è "da ritrovare": il bot lo cerca di nuovo
   e aggiorna la mappa;
4. dopo troppe verifiche fallite il bot si ferma e avvisa, invece di cliccare
   a caso.

I nomi letti possono essere in italiano (client del proprietario) o in
inglese: ``ALIASES`` li riconduce allo stesso edificio.
"""

from __future__ import annotations

import datetime as _dt
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .kb import normalize_name

# nome canonico inglese -> varianti (italiano confermato dal proprietario o da
# verificare durante i test: aggiungere qui i nomi letti sullo schermo)
ALIASES: Dict[str, List[str]] = {
    "Trading Post": ["Mercato", "Trading Post"],
    "City Hall": ["Municipio", "City Hall"],
    "Academy": ["Accademia", "Academy"],
    "Barracks": ["Caserma", "Barracks"],
    "Stable": ["Stalla", "Scuderia", "Stable"],
    "Archery Range": ["Poligono di tiro", "Tiro con l'arco", "Archery Range"],
    "Siege Workshop": ["Officina d'assedio", "Laboratorio d'assedio", "Siege Workshop"],
    "Hospital": ["Ospedale", "Hospital"],
    "Tavern": ["Taverna", "Tavern"],
    "Blacksmith": ["Fabbro", "Blacksmith"],
    "Alliance Center": ["Centro dell'alleanza", "Alliance Center"],
    "Scout Camp": ["Accampamento esploratori", "Campo esploratori", "Scout Camp"],
    "Storehouse": ["Magazzino", "Storehouse"],
    "Wall": ["Mura", "Wall"],
    "Watchtower": ["Torre di guardia", "Watchtower"],
    "Courier Station": ["Stazione dei corrieri", "Courier Station"],
    "State Forum": ["Foro", "State Forum"],
    "Castle": ["Castello", "Castle"],
    "Monument": ["Monumento", "Monument"],
    "Farm": ["Fattoria", "Farm"],
    "Lumber Mill": ["Segheria", "Lumber Mill"],
    "Quarry": ["Cava", "Quarry"],
    "Goldmine": ["Miniera d'oro", "Goldmine"],
}

_LOOKUP = {normalize_name(a): canon for canon, al in ALIASES.items() for a in al}

MAX_FAILURES = 3  # verifiche fallite di fila prima di fermarsi e avvisare


def canonical_building(ocr_text: str) -> Optional[str]:
    """Dal testo letto nella finestra dell'edificio al nome canonico.
    Tollera livello e rumore: "Mercato Lv.12" -> "Trading Post"."""
    t = normalize_name(ocr_text)
    if not t:
        return None
    if t in _LOOKUP:
        return _LOOKUP[t]
    # il più lungo alias contenuto nel testo vince ("miniera d oro" prima di "oro")
    best = None
    for alias, canon in _LOOKUP.items():
        if alias and alias in t and (best is None or len(alias) > len(best[0])):
            best = (alias, canon)
    return best[1] if best else None


@dataclass
class BuildingSpot:
    name: str                      # nome canonico
    x: float                       # coordinate relative 0-1 con telecamera standard
    y: float
    index: int = 0                 # per edifici multipli (4 Farm, 4 Hospital...)
    last_seen: str = ""
    failures: int = 0


@dataclass
class CityMap:
    screen_size: Tuple[int, int] = (0, 0)
    spots: List[BuildingSpot] = field(default_factory=list)
    updated: str = ""

    # ---- persistenza -----------------------------------------------------
    @classmethod
    def load(cls, path: Path) -> "CityMap":
        p = Path(path)
        if not p.exists():
            return cls()
        d = json.loads(p.read_text(encoding="utf-8"))
        return cls(screen_size=tuple(d.get("screen_size") or (0, 0)),
                   spots=[BuildingSpot(**s) for s in d.get("spots") or []],
                   updated=d.get("updated", ""))

    def save(self, path: Path) -> None:
        self.updated = _dt.datetime.now().isoformat(timespec="seconds")
        Path(path).write_text(json.dumps({"screen_size": list(self.screen_size), "updated": self.updated,
                                          "spots": [asdict(s) for s in self.spots]},
                                         ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- uso -------------------------------------------------------------
    def find(self, name: str, index: int = 0) -> Optional[BuildingSpot]:
        canon = canonical_building(name) or name
        for s in self.spots:
            if s.name == canon and s.index == index:
                return s
        return None

    def to_pixels(self, spot: BuildingSpot, screen_size: Tuple[int, int]) -> Tuple[int, int]:
        w, h = screen_size
        return int(round(spot.x * w)), int(round(spot.y * h))

    def learn(self, ocr_text: str, px: int, py: int, screen_size: Tuple[int, int], index: int = 0) -> Optional[BuildingSpot]:
        """Registra dove si trova un edificio, dal tocco in (px, py) e dal
        nome letto nella finestra che si è aperta."""
        canon = canonical_building(ocr_text)
        if not canon:
            return None
        w, h = screen_size
        self.screen_size = screen_size
        spot = self.find(canon, index)
        now = _dt.datetime.now().isoformat(timespec="seconds")
        if spot is None:
            spot = BuildingSpot(canon, px / w, py / h, index, now, 0)
            self.spots.append(spot)
        else:
            spot.x, spot.y, spot.last_seen, spot.failures = px / w, py / h, now, 0
        return spot

    def verify(self, expected: str, ocr_text: str, index: int = 0) -> Dict[str, object]:
        """Dopo aver toccato la posizione salvata di ``expected``: il nome
        letto combacia? Restituisce cosa fare dopo."""
        spot = self.find(expected, index)
        seen = canonical_building(ocr_text)
        want = canonical_building(expected) or expected
        if spot is None:
            return {"ok": False, "action": "relearn", "reason": f"{want} non è ancora nella mappa"}
        if seen == want:
            spot.failures = 0
            spot.last_seen = _dt.datetime.now().isoformat(timespec="seconds")
            return {"ok": True, "action": "proceed", "reason": "edificio confermato"}
        spot.failures += 1
        if spot.failures >= MAX_FAILURES:
            return {"ok": False, "action": "stop_and_notify",
                    "reason": f"{want} non trovato dopo {spot.failures} tentativi: fermarsi e avvisare il proprietario"}
        return {"ok": False, "action": "relearn",
                "reason": f"atteso {want}, letto '{ocr_text}' ({seen or 'sconosciuto'}): edificio spostato o camera fuori posizione"}
