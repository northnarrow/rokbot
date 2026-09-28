"""Caricamento e interrogazione della knowledge base (data/*.json).

Ogni dato della KB porta un elenco ``sources`` con url, page_date e retrieved.
Questo modulo non fa rete: legge solo i file JSON generati da ``merge_kb.py``.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

DATA_DIR = Path(__file__).resolve().parent / "data"

TIER_SCORE = {
    "Z": 10.5, "S+": 10.0, "S": 9.0, "A+": 8.0, "A": 7.0, "B+": 6.0, "B": 5.0,
    "C+": 4.0, "C": 3.0, "D+": 2.0, "D": 1.0, "F": 0.0, "G": 9.0,
}

TROOP_TYPES = ("infantry", "cavalry", "archer", "siege")


def normalize_name(name: str) -> str:
    """'Yi Seong-Gye (Prime)' -> 'yi seong gye prime'. Serve per confrontare
    i nomi letti via OCR con quelli della KB."""
    if not name:
        return ""
    s = unicodedata.normalize("NFKD", str(name))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


_TIER_TOKEN = re.compile(r"(?<![A-Z0-9])(S\+|A\+|B\+|C\+|D\+|Z|S|A|B|C|D|F|G)(?![A-Z0-9+])")


def tier_to_score(value: Any) -> Optional[float]:
    """Converte un rating in punteggio 0-10. Formati gestiti (dalle fonti):
    "A", "B+", "Tier A", "A-tier", "B (colonna Defense)", "4/5", "4/5 stelle",
    "4.4/5 (11 voti)", "5 stelle", "KvK1 A / KvK2 A / SoC B" (media),
    "Z" (tier sopra S+ di meta-rok). Placeholder e giudizi ironici -> None."""
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    low = s.lower()
    if not s or any(w in low for w in ("placeholder", "ironic", "in attesa", "non valutat")):
        return None
    compact = s.upper().replace(" ", "")
    if compact in TIER_SCORE:
        return TIER_SCORE[compact]
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*/\s*(\d+)", s)  # "4.4/5 (11 voti)"
    if m and float(m.group(2)) > 0:
        return float(m.group(1).replace(",", ".")) / float(m.group(2)) * 10.0
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:stell|star)", low)  # "5 stelle"
    if m:
        return float(m.group(1).replace(",", ".")) / 5.0 * 10.0
    tokens = _TIER_TOKEN.findall(s.upper())
    scores = [TIER_SCORE[t] for t in tokens if t in TIER_SCORE]
    if scores:
        return sum(scores) / len(scores)
    return None


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


class KnowledgeBase:
    """Accesso in sola lettura alla KB. Tollera file mancanti (KB parziale)."""

    def __init__(self, data_dir: Path | str = DATA_DIR):
        self.data_dir = Path(data_dir)
        self.sources = (_load_json(self.data_dir / "sources.json") or {}).get("sources", {})
        raw = _load_json(self.data_dir / "commanders.json") or {}
        self.commanders: List[Dict[str, Any]] = raw.get("commanders", []) if isinstance(raw, dict) else raw
        self.armaments = _load_json(self.data_dir / "armamenti.json") or {}
        self.equipment = _load_json(self.data_dir / "equipaggiamento.json") or {}
        self.troops = _load_json(self.data_dir / "truppe_pve.json") or {}
        # chiave -> lista di record: lo stesso nome può esistere in due rarità
        # (es. Pelagius Epic e Pelagius Legendary, uscito nel 2026).
        # Prima i nomi ufficiali, poi gli alias: un alias non oscura mai il
        # nome di un altro comandante.
        self._index: Dict[str, List[Dict[str, Any]]] = {}
        for c in self.commanders:
            k = normalize_name(c.get("name", ""))
            if k:
                self._index.setdefault(k, []).append(c)
        for c in self.commanders:
            for a in c.get("aliases") or []:
                k = normalize_name(a)
                if k and k not in self._index:
                    self._index[k] = [c]

    # ---- lookup -----------------------------------------------------------
    @staticmethod
    def _pick(records: List[Dict[str, Any]], rarity: Optional[str]) -> Dict[str, Any]:
        if rarity and len(records) > 1:
            r = str(rarity).strip().lower()
            for c in records:
                if str(c.get("rarity") or "").lower() == r:
                    return c
        return records[0]

    def find(self, name: str, rarity: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Cerca un comandante per nome (tollerante a maiuscole, accenti,
        trattini). ``rarity`` (dal profilo letto sul telefono) risolve i nomi
        che esistono in più rarità."""
        key = normalize_name(name)
        if key in self._index:
            return self._pick(self._index[key], rarity)
        # match parziale: 'sun tzu' vs 'sun tzu prime' -> preferisci uguaglianza
        # esatta, poi contenimento della stringa più lunga.
        # Un comandante "Prime" è un comandante DIVERSO dalla versione base
        # (es. Sun Tzu Epic vs Sun Tzu Prime Legendary): mai confonderli.
        is_prime = "prime" in key.split()
        candidates = [c for k, recs in self._index.items() for c in recs
                      if key and (key in k or k in key)
                      and (("prime" in normalize_name(c.get("name", "")).split()) == is_prime)]
        if not candidates:
            return None
        candidates.sort(key=lambda c: abs(len(normalize_name(c.get("name", ""))) - len(key)))
        best_len = abs(len(normalize_name(candidates[0].get("name", ""))) - len(key))
        tied = [c for c in candidates if abs(len(normalize_name(c.get("name", ""))) - len(key)) == best_len]
        return self._pick(tied, rarity)

    def names(self) -> List[str]:
        return [c.get("name", "") for c in self.commanders]

    # ---- attributi derivati -------------------------------------------------
    @staticmethod
    def troop_type(cmd: Dict[str, Any]) -> str:
        tt = (cmd.get("troop_type") or "").lower()
        if tt:
            return tt
        specs = [str(s).lower() for s in (cmd.get("specialties") or [])]
        for s in specs:
            if s in ("infantry", "cavalry", "archer"):
                return s
        if "leadership" in specs:
            return "leadership"
        if "integration" in specs:
            return "integration"
        if "engineering" in specs:
            return "engineering"
        return "unknown"

    @staticmethod
    def specialties(cmd: Dict[str, Any]) -> List[str]:
        return [str(s).lower() for s in (cmd.get("specialties") or [])]

    @staticmethod
    def rating(cmd: Dict[str, Any], key: str) -> Optional[float]:
        """Media dei rating disponibili per una chiave (open_field, rally,
        garrison, canyon, barbarians, gathering, overall)."""
        vals = []
        for r in cmd.get("ratings") or []:
            s = tier_to_score(r.get(key))
            if s is not None:
                vals.append(s)
        if not vals:
            return None
        return sum(vals) / len(vals)

    @staticmethod
    def skill_text(cmd: Dict[str, Any]) -> str:
        parts = []
        for s in cmd.get("skills") or []:
            parts.append(str(s.get("name") or ""))
            parts.append(str(s.get("effect") or ""))
        return " ".join(parts).lower()

    def barbarian_bonus_pct(self, cmd: Dict[str, Any]) -> float:
        """Estrae il bonus % 'damage to barbarians' dalle skill, se presente."""
        best = 0.0
        for s in cmd.get("skills") or []:
            eff = str(s.get("effect") or "").lower()
            if "barbarian" in eff or "neutral" in eff:
                for m in re.finditer(r"(\d{1,3})\s*%", eff):
                    best = max(best, float(m.group(1)))
        return best

    def gathering_bonus(self, cmd: Dict[str, Any]) -> float:
        best = 0.0
        for s in cmd.get("skills") or []:
            eff = str(s.get("effect") or "").lower()
            if "gather" in eff or "load" in eff:
                for m in re.finditer(r"(\d{1,3})\s*%", eff):
                    best = max(best, float(m.group(1)))
        return best

    def pairings_for(self, cmd: Dict[str, Any]) -> List[Dict[str, Any]]:
        return list(cmd.get("pairings") or [])

    def talent_build(self, cmd: Dict[str, Any], purpose: str, strict: bool = False) -> Optional[Dict[str, Any]]:
        """Build dei talenti del comandante per uno scopo. Con strict=True
        restituisce None se la guida non ha una build per quello scopo
        (invece di ripiegare sulla prima build disponibile)."""
        builds = cmd.get("talent_builds") or []
        purpose = purpose.lower()
        synonyms = {
            "attack": ("open_field", "field", "pvp", "open field"),
            "open_field": ("open_field", "field", "pvp", "open field"),
            "rally": ("rally",),
            "defense": ("garrison", "defense", "defence"),
            "garrison": ("garrison", "defense", "defence"),
            "barbarians": ("barbarian", "peacekeeping", "pve", "fort", "nuke"),
            "gathering": ("gather", "farming"),
        }
        wanted = synonyms.get(purpose, (purpose,))
        for b in builds:
            p = str(b.get("purpose") or "").lower()
            if any(w in p for w in wanted):
                return b
        if strict:
            return None
        return builds[0] if builds else None

    # ---- formazioni ----------------------------------------------------------
    def formations(self) -> List[Dict[str, Any]]:
        return list(self.armaments.get("formations") or [])

    def formation_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """'Wedge', 'wedge formation', 'Wedge Formation' -> stessa scheda.
        'Wedge II' resta distinta da 'Wedge'."""
        def k(s: str) -> str:
            return re.sub(r"\s+", " ", re.sub(r"\bformation\b", "", normalize_name(s))).strip()
        key = k(name)
        for f in self.formations():
            if k(f.get("name", "")) == key:
                return f
        return None

    # ---- fonti -----------------------------------------------------------------
    @staticmethod
    def sources_of(obj: Dict[str, Any]) -> List[Dict[str, Any]]:
        return list(obj.get("sources") or [])

    def cite(self, obj: Dict[str, Any], max_n: int = 3) -> str:
        cites = []
        for s in self.sources_of(obj)[:max_n]:
            url = s.get("url") or s.get("source_url") or "?"
            d = s.get("page_date") or "data n/d"
            cites.append(f"{url} ({d}, letto {s.get('retrieved', '?')})")
        return "; ".join(cites)

    def stats(self) -> Dict[str, Any]:
        n = len(self.commanders)
        with_skills = sum(1 for c in self.commanders if c.get("skills"))
        with_pairs = sum(1 for c in self.commanders if c.get("pairings"))
        with_ratings = sum(1 for c in self.commanders if c.get("ratings"))
        verified = sum(1 for c in self.commanders if (c.get("verification") or {}).get("status") in ("verified", "partially_verified"))
        return {
            "commanders": n,
            "with_skills": with_skills,
            "with_pairings": with_pairs,
            "with_ratings": with_ratings,
            "verified": verified,
            "formations": len(self.formations()),
            "equipment_items": len(self.equipment.get("items") or []),
            "has_troops": bool(self.troops),
        }


def iter_owned(profile: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    for c in profile.get("commanders") or []:
        if c.get("name"):
            yield c
