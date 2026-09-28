"""Consigliere militare per Rise of Kingdoms.

Uso rapido:

    from military_advisor import MilitaryAdvisor
    adv = MilitaryAdvisor()                       # carica data/*.json
    profile = json.load(open("account_profile.json"))
    result = adv.recommend(profile)               # dict con raccomandazioni e piano
    print(adv.render_report(result))              # testo in italiano

Il modulo NON tocca il telefono: legge un profilo account (vedi
account_profile.example.json) prodotto dalla parte del bot che fa OCR/ADB
(interfaccia in account_reader.py) e produce raccomandazioni + un piano di
addestramento che il bot può eseguire. Vincoli fissi: mai gemme; conferma
esplicita prima di attaccare giocatori o consumare materiali rari.
"""

from .advisor import MilitaryAdvisor, RARE_MATERIALS_DEFAULT  # noqa: F401
from .kb import KnowledgeBase, normalize_name  # noqa: F401

__all__ = ["MilitaryAdvisor", "KnowledgeBase", "normalize_name", "RARE_MATERIALS_DEFAULT"]
__version__ = "0.1.0"
