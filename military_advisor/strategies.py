"""Libro delle strategie: carica i frammenti "strategia_*", "talenti",
"eventi_pve", "meccaniche", "kvk_alleanza", "automazione" e li espone al
consigliere e al bot.

Ogni frammento è stato prodotto dalla ricerca con fonte+data per dato e,
dove esiste, viene preferita la versione ``.verified.json``. Le regole per il
bot (``bot_rules``) hanno la forma
    {"id", "when", "then", "why", "requires_confirmation", "sources"}
e vengono raccolte da tutti i file in un'unica lista, con il file d'origine.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .kb import DATA_DIR, normalize_name

STRATEGY_TOPICS = (
    "strategia_difesa", "strategia_attacco", "strategia_routine", "talenti",
    "eventi_pve", "meccaniche", "kvk_alleanza", "automazione",
    "segreti_pro", "sculture_stelle", "sculture_quantita",
    "calendario_eventi", "quest_lucerna", "mappa_edifici",
)


def _load_topic(data_dir: Path, topic: str) -> Optional[Dict[str, Any]]:
    """La versione verificata vince sempre; altrimenti la più recente tra
    data/<topic>.json (copia fatta da build-kb) e fragments/<topic>.json
    (scritto dalla ricerca). Così una copia vecchia non oscura un frammento
    aggiornato dopo l'ultimo build-kb."""
    verified = data_dir / "fragments" / f"{topic}.verified.json"
    others = [p for p in (data_dir / f"{topic}.json", data_dir / "fragments" / f"{topic}.json") if p.exists()]
    others.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    for p in ([verified] if verified.exists() else []) + others:
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
    return None


import re as _re

# Regole decise dal proprietario: valgono sopra qualsiasi regola ricercata.
USER_POLICY = {
    "never_activate_shield": {
        "date": "2026-09-28",
        "text": "Il proprietario ha vietato di attivare scudi (Peace Shield): mai attivarli, "
                "nemmeno se posseduti. In caso di pericolo avvisare subito il proprietario "
                "e proporre solo alternative senza scudo (cambio guarnigione, rinforzi, richiamo marce).",
    },
}
_SHIELD = _re.compile(r"(scud|shield)", _re.I)
_SHIELD_USE = _re.compile(r"(attiva\w*|attivazione|propor\w*|proponi|consumare|usa\w*)[^.;]{0,60}(scud|shield)"
                          r"|(scud\w*|shield)[^.;]{0,20}(possedut|da inventario|in inventario)", _re.I)


def apply_user_policy(rule: Dict[str, Any]) -> Dict[str, Any]:
    """Riscrive le regole che attiverebbero o proporrebbero uno scudo."""
    then = str(rule.get("then") or "")
    if USER_POLICY.get("never_activate_shield") and _SHIELD.search(then) and _SHIELD_USE.search(then) \
            and not _re.search(r"non consumare scudi", then, _re.I):
        rule = dict(rule)
        rule["then_original"] = then
        rule["then"] = ("MAI attivare scudi (divieto del proprietario). Avvisare subito il proprietario. "
                        "Parte ancora valida della regola originale, senza scudi: " + then)
        rule["user_policy"] = "never_activate_shield"
    return rule


class StrategyBook:
    def __init__(self, data_dir: Path | str = DATA_DIR):
        self.data_dir = Path(data_dir)
        self.topics: Dict[str, Dict[str, Any]] = {}
        for t in STRATEGY_TOPICS:
            d = _load_topic(self.data_dir, t)
            if d:
                self.topics[t] = d

    # ---- regole per il bot -----------------------------------------------
    def bot_rules(self) -> List[Dict[str, Any]]:
        return [apply_user_policy(r) for r in self._raw_bot_rules()]

    def _raw_bot_rules(self) -> List[Dict[str, Any]]:
        rules: List[Dict[str, Any]] = []
        for topic, d in self.topics.items():
            for r in d.get("bot_rules") or []:
                if isinstance(r, dict):
                    rr = dict(r)
                    rr.setdefault("requires_confirmation", False)
                    rr["topic"] = topic
                    rules.append(rr)
            # eventi_pve: regole annidate per modalità
            for mode in d.get("modes") or []:
                for r in (mode.get("bot_rules") or []) if isinstance(mode, dict) else []:
                    if isinstance(r, dict):
                        rr = dict(r)
                        rr.setdefault("requires_confirmation", False)
                        rr["topic"] = f"{topic}:{mode.get('name')}"
                        rules.append(rr)
            # routine: la checklist porta la sua regola
            for item in d.get("daily_checklist") or []:
                if isinstance(item, dict) and item.get("bot_rule"):
                    rules.append({
                        "id": f"daily:{item.get('order', '?')}:{normalize_name(str(item.get('task', '')))[:40]}",
                        "when": f"routine giornaliera ({item.get('reset') or 'reset n/d'})",
                        "then": item["bot_rule"],
                        "why": item.get("value"),
                        "requires_confirmation": bool(item.get("requires_confirmation")),
                        "confirmation_when": item.get("confirmation_when"),
                        "sources": item.get("sources") or [],
                        "topic": topic,
                    })
        return rules

    @staticmethod
    def conditional_confirmation(item: Dict[str, Any]) -> Optional[str]:
        """Testo della conferma condizionale, se la voce ne ha una vera
        (le voci che iniziano con "no" sono solo lettura/riscossione)."""
        cw = str(item.get("confirmation_when") or "").strip()
        if not cw or cw.lower().startswith(("no ", "no(", "no,", "no;", "no.", "nessun")) or cw.lower() == "no":
            return None
        return cw

    def daily_checklist(self) -> List[Dict[str, Any]]:
        d = self.topics.get("strategia_routine") or {}
        items = [i for i in (d.get("daily_checklist") or []) if isinstance(i, dict)]
        return sorted(items, key=lambda i: (i.get("order") is None, i.get("order") or 0))

    def weekly_checklist(self) -> List[Dict[str, Any]]:
        d = self.topics.get("strategia_routine") or {}
        return [i for i in (d.get("weekly_checklist") or []) if isinstance(i, dict)]

    # ---- coppie ---------------------------------------------------------------
    def garrison_pairs(self) -> List[Dict[str, Any]]:
        d = self.topics.get("strategia_difesa") or {}
        return [p for p in (d.get("garrison_pairs") or []) if isinstance(p, dict)]

    def meta_pairs(self, mode: Optional[str] = None) -> List[Dict[str, Any]]:
        d = self.topics.get("strategia_attacco") or {}
        pairs = [p for p in (d.get("meta_pairs") or []) if isinstance(p, dict)]
        if mode:
            m = mode.lower()
            pairs = [p for p in pairs if m in str(p.get("mode") or "").lower()]
        return pairs

    @staticmethod
    def owned_pairs(pairs: List[Dict[str, Any]], owned_names: List[str]) -> List[Dict[str, Any]]:
        """Filtra le coppie documentate a quelle in cui possiedi entrambi."""
        owned = {normalize_name(n) for n in owned_names}
        out = []
        for p in pairs:
            a, b = normalize_name(str(p.get("primary") or "")), normalize_name(str(p.get("secondary") or ""))
            if a in owned and b in owned:
                out.append(p)
        return out

    # ---- altro ------------------------------------------------------------------
    def talent_role_build(self, role: str) -> Optional[Dict[str, Any]]:
        d = self.topics.get("talenti") or {}
        role = role.lower()
        synonyms = {
            "attack": ("open_field", "field", "nuke", "pvp"), "defense": ("garrison", "defense"),
            "barbarians": ("barbar", "peacekeep", "pve"), "gathering": ("gather", "raccolta"),
        }.get(role, (role,))
        for b in d.get("role_builds") or []:
            r = str(b.get("role") or "").lower()
            if any(s in r for s in synonyms):
                return b
        return None

    def event_modes(self) -> List[Dict[str, Any]]:
        d = self.topics.get("eventi_pve") or {}
        return [m for m in (d.get("modes") or []) if isinstance(m, dict)]

    def mechanics(self) -> Dict[str, Any]:
        return self.topics.get("meccaniche") or {}

    def stats(self) -> Dict[str, Any]:
        return {
            "topics_loaded": sorted(self.topics.keys()),
            "bot_rules": len(self.bot_rules()),
            "daily_checklist": len(self.daily_checklist()),
            "garrison_pairs": len(self.garrison_pairs()),
            "meta_pairs": len(self.meta_pairs()),
            "event_modes": len(self.event_modes()),
        }
