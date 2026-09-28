"""Controllo di coerenza della knowledge base (nessuna rete).

Segnala, senza correggere, i record che meritano una verifica:
campi mancanti, specialità incoerenti, coppie verso comandanti sconosciuti,
rating illeggibili, fonti senza url o data, civiltà fuori elenco.
Le correzioni vanno fatte solo con una fonte (vedi verifica su seconda fonte).
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from typing import Any, Dict, List

from .kb import KnowledgeBase, normalize_name, tier_to_score

TROOPS = {"infantry", "cavalry", "archer", "leadership", "integration", "engineering"}
# Civiltà giocabili note + valori neutri usati dalle fonti per i comandanti
# senza civiltà. Un valore fuori elenco non è per forza un errore: va controllato.
KNOWN_CIVS = {
    "rome", "germany", "britain", "france", "spain", "china", "japan", "korea", "arabia",
    "ottoman", "byzantium", "vikings", "egypt", "greece", "maya", "other", "others", "none",
}


def lint(kb: KnowledgeBase) -> Dict[str, Any]:
    issues: Dict[str, List[str]] = defaultdict(list)
    names = {normalize_name(c.get("name", "")) for c in kb.commanders}
    rarity_by_name: Dict[str, set] = defaultdict(set)

    for c in kb.commanders:
        n = c.get("name") or "?"
        rarity_by_name[normalize_name(n)].add(c.get("rarity"))
        if not c.get("rarity"):
            issues["rarità mancante"].append(n)
        specs = [str(s).lower() for s in (c.get("specialties") or [])]
        if len(specs) != 3:
            issues["specialità non sono 3"].append(f"{n}: {c.get('specialties')}")
        tt = str(c.get("troop_type") or "").lower()
        if tt and tt not in TROOPS:
            issues["troop_type sconosciuto"].append(f"{n}: {tt}")
        if tt and specs and tt in TROOPS and specs[0] != tt and tt not in specs:
            issues["troop_type diverso dalle specialità"].append(f"{n}: troop_type={tt}, specialità={c.get('specialties')}")
        is_prime_name = "prime" in normalize_name(n).split()
        if bool(c.get("is_prime")) != is_prime_name:
            issues["is_prime incoerente col nome"].append(f"{n}: is_prime={c.get('is_prime')}")
        skills = c.get("skills") or []
        if not (4 <= len(skills) <= 6):
            issues["numero di skill insolito (atteso 4-5)"].append(f"{n}: {len(skills)}")
        for s in skills:
            if not s.get("name") or not s.get("effect"):
                issues["skill senza nome o effetto"].append(f"{n}: slot {s.get('slot')}")
                break
        src = c.get("sources") or []
        if not src:
            issues["record senza fonti"].append(n)
        elif any(not (s.get("url") or s.get("source_url")) or not s.get("retrieved") for s in src):
            issues["fonte senza url o data di lettura"].append(n)
        civ = normalize_name(str(c.get("civilization") or "none"))
        if civ and civ not in KNOWN_CIVS:
            issues["civiltà fuori elenco (da controllare)"].append(f"{n}: {c.get('civilization')}")
        unk = []
        for p in c.get("pairings") or []:
            partner = str(p.get("partner") or "")
            if partner and kb.find(partner) is None:
                unk.append(partner)
        if unk:
            issues["coppie verso comandanti non in KB"].append(f"{n}: {', '.join(sorted(set(unk)))[:160]}")
        bad = 0
        for r in c.get("ratings") or []:
            for k in ("overall", "open_field", "rally", "garrison", "canyon"):
                v = r.get(k)
                if v not in (None, "", "n/a") and tier_to_score(v) is None:
                    bad += 1
        if bad:
            issues["rating non convertibili in punteggio"].append(f"{n}: {bad}")
        if not c.get("talent_builds"):
            issues["nessuna build talenti"].append(n)

    for k, rs in rarity_by_name.items():
        if len(rs) > 1:
            issues["stesso nome in più rarità (ok solo se sono davvero due comandanti)"].append(f"{k}: {sorted(map(str, rs))}")

    counts = Counter({k: len(v) for k, v in issues.items()})
    return {"commanders": len(kb.commanders), "summary": dict(counts.most_common()), "issues": dict(issues)}


if __name__ == "__main__":
    print(json.dumps(lint(KnowledgeBase()), ensure_ascii=False, indent=2))
