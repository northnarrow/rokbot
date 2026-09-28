"""Interfaccia che la parte "telefono" del bot deve implementare.

Questo modulo NON contiene codice ADB/OCR: quello vive nel bot sul PC, dove
il telefono è collegato. Qui c'è solo il contratto: quali schermate leggere
e con quale struttura restituire i dati, così che ``MilitaryAdvisor`` possa
ragionarci sopra. L'implementazione concreta va agganciata registrando una
classe che eredita da ``AccountReader``.

Schermate da leggere (client in inglese; tra parentesi il nome italiano):
  1. Commanders (Comandanti) -> lista: nome, livello, stelle, potenza.
  2. Dettaglio comandante -> Skills (Abilità) livelli 1-5 + expertise;
     Talents (Talenti) punti spesi per albero; Equipment (Equipaggiamento)
     8 slot; Formation (Formazione) nome + livello + 4 armamenti con
     3 attributi e iscrizione; Troops (Truppe) preset di marcia se presente.
  3. City Hall -> Troops (Truppe): conteggio per tipo e tier + feriti.
  4. Barracks/Stable/Archery Range/Siege Workshop -> tier sbloccato, code.
  5. Items (Oggetti) -> materiali rari (vedi RARE_MATERIALS_DEFAULT).
  6. Formation/Armament screen (Officina armamenti): Travel/Dispatch
     disponibili, monete, pietre di trasmutazione/conversione.
"""

from __future__ import annotations

import abc
import json
import datetime as _dt
from pathlib import Path
from typing import Any, Dict, List

PROFILE_VERSION = 1


class AccountReader(abc.ABC):
    """Contratto. Ogni metodo restituisce dati già normalizzati (numeri, non
    stringhe OCR grezze). Se un dato non è leggibile, restituire None e
    aggiungere un messaggio in ``self.notes``."""

    def __init__(self) -> None:
        self.notes: List[str] = []

    @abc.abstractmethod
    def read_player(self) -> Dict[str, Any]:
        """{'name', 'city_hall', 'vip', 'power', 'civilization'}"""

    @abc.abstractmethod
    def read_commanders(self) -> List[Dict[str, Any]]:
        """Lista di comandanti nel formato di account_profile.example.json."""

    @abc.abstractmethod
    def read_troops(self) -> Dict[str, Any]:
        """{'infantry': {'T1':n,...,'T5':n}, 'cavalry':..., 'archer':..., 'siege':..., 'wounded': {...}}"""

    @abc.abstractmethod
    def read_troop_tiers_unlocked(self) -> Dict[str, int]:
        """{'infantry': 4, 'cavalry': 4, 'archer': 3, 'siege': 1}"""

    @abc.abstractmethod
    def read_march(self) -> Dict[str, Any]:
        """{'capacity': n, 'max_marches': n, 'rally_capacity': n}"""

    def read_resources(self) -> Dict[str, Any]:
        return {}

    def read_inventory(self) -> Dict[str, Any]:
        """{'rare_materials': {'Sage\\'s Testimony': 3, ...}, 'speedups_training_min': n}"""
        return {}

    def read_armament_workshop(self) -> Dict[str, Any]:
        """Stato della schermata armamenti: {'travel_left': n, 'dispatch_left': n,
        'gold_coins': n, 'silver_coins': n, 'transmutation_stones': n, ...}"""
        return {}

    # ---- assemblaggio -------------------------------------------------------
    def build_profile(self) -> Dict[str, Any]:
        profile = {
            "profile_version": PROFILE_VERSION,
            "read_at": _dt.datetime.now().isoformat(timespec="seconds"),
            "player": self.read_player(),
            "commanders": self.read_commanders(),
            "troops": self.read_troops(),
            "troop_tiers_unlocked": self.read_troop_tiers_unlocked(),
            "march": self.read_march(),
            "resources": self.read_resources(),
            "inventory": self.read_inventory(),
            "armament_workshop": self.read_armament_workshop(),
            "reader_notes": list(self.notes),
        }
        return profile

    def save_profile(self, path: str | Path) -> Dict[str, Any]:
        profile = self.build_profile()
        Path(path).write_text(json.dumps(profile, ensure_ascii=False, indent=2), encoding="utf-8")
        return profile


class NotConnectedReader(AccountReader):
    """Segnaposto usato quando il telefono non è raggiungibile (es. sessione
    cloud). Ogni lettura solleva un errore chiaro invece di inventare dati."""

    def _fail(self):
        raise RuntimeError(
            "Telefono non raggiungibile da questa sessione: implementa AccountReader "
            "nel bot sul PC (ADB + OCR) e passa il profilo JSON al consigliere."
        )

    def read_player(self):  # pragma: no cover
        self._fail()

    def read_commanders(self):  # pragma: no cover
        self._fail()

    def read_troops(self):  # pragma: no cover
        self._fail()

    def read_troop_tiers_unlocked(self):  # pragma: no cover
        self._fail()

    def read_march(self):  # pragma: no cover
        self._fail()


def validate_profile(profile: Dict[str, Any]) -> List[str]:
    """Controlli minimi sul profilo: ritorna la lista dei problemi (vuota = ok)."""
    problems: List[str] = []
    if not isinstance(profile.get("commanders"), list) or not profile["commanders"]:
        problems.append("commanders: lista vuota o assente")
    for i, c in enumerate(profile.get("commanders") or []):
        if not c.get("name"):
            problems.append(f"commanders[{i}]: manca name")
        sk = c.get("skills")
        if sk is not None and (not isinstance(sk, list) or len(sk) not in (4, 5) or any((not isinstance(x, int)) or x < 0 or x > 5 for x in sk)):
            problems.append(f"commanders[{i}] ({c.get('name')}): skills deve essere una lista di 4-5 interi 0..5")
        lv = c.get("level")
        if lv is not None and not (0 <= int(lv) <= 60):
            problems.append(f"commanders[{i}] ({c.get('name')}): level fuori range 0..60")
    troops = profile.get("troops") or {}
    for tt, tiers in troops.items():
        if tt == "wounded":
            continue
        if not isinstance(tiers, dict):
            problems.append(f"troops.{tt}: deve essere un dict T1..T5")
    march = profile.get("march") or {}
    if not march.get("capacity"):
        problems.append("march.capacity assente: il piano di addestramento non può calcolare i conteggi")
    return problems
