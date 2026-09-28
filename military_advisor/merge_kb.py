"""Unisce i frammenti di ricerca (data/fragments/*.verified.json, con
fallback ai *.json non verificati) nei file finali della KB:

  data/commanders.json        -> {"generated": ..., "commanders": [...]}
  data/armamenti.json         -> copia del frammento verificato
  data/equipaggiamento.json   -> idem
  data/truppe_pve.json        -> idem
  data/kb_index.json          -> statistiche, gruppi, conflitti, gap

Regole di merge per i comandanti (chiave = nome normalizzato):
  * il frammento verificato vince su quello non verificato;
  * a parità, vince il record con più campi valorizzati;
  * le liste sources/conflicts/gaps si uniscono senza duplicati.
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

from .kb import DATA_DIR, normalize_name

TOPIC_FILES = {
    "armamenti": "armamenti.json", "equipaggiamento": "equipaggiamento.json", "truppe_pve": "truppe_pve.json",
    "strategia_difesa": "strategia_difesa.json", "strategia_attacco": "strategia_attacco.json",
    "strategia_routine": "strategia_routine.json", "talenti": "talenti.json", "eventi_pve": "eventi_pve.json",
    "meccaniche": "meccaniche.json", "kvk_alleanza": "kvk_alleanza.json", "automazione": "automazione.json",
    "segreti_pro": "segreti_pro.json", "sculture_stelle": "sculture_stelle.json",
}


def _load(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"[merge_kb] file non valido, ignorato: {path} ({exc})", file=sys.stderr)
        return None


def _filled(rec: Dict[str, Any]) -> int:
    n = 0
    for k, v in rec.items():
        if v in (None, "", [], {}):
            continue
        n += 1 + (len(v) if isinstance(v, (list, dict)) else 0)
    return n


def _merge_lists(a: List[Any], b: List[Any]) -> List[Any]:
    out: List[Any] = []
    seen = set()
    for item in (a or []) + (b or []):
        key = json.dumps(item, sort_keys=True, ensure_ascii=False) if isinstance(item, (dict, list)) else str(item)
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def _merge_records(base: Dict[str, Any], other: Dict[str, Any]) -> Dict[str, Any]:
    """base ha priorità; other riempie i buchi e aggiunge fonti/conflitti."""
    out = dict(base)
    for k, v in other.items():
        if k in ("sources", "conflicts", "gaps", "aliases", "ratings", "pairings"):
            out[k] = _merge_lists(out.get(k) or [], v or [])
        elif out.get(k) in (None, "", [], {}):
            out[k] = v
    return out


def merge(fragments_dir: Path | None = None, data_dir: Path | None = None) -> Dict[str, Any]:
    data_dir = Path(data_dir or DATA_DIR)
    fragments_dir = Path(fragments_dir or (data_dir / "fragments"))
    index: Dict[str, Any] = {"generated": _dt.datetime.now().isoformat(timespec="seconds"), "groups": {}, "topics": {}}
    commanders: Dict[str, Dict[str, Any]] = {}

    acquisition_files: List[Any] = []
    files = sorted(fragments_dir.glob("*.json")) if fragments_dir.exists() else []
    # prima i verificati, così vincono nel merge
    files.sort(key=lambda p: (0 if p.name.endswith(".verified.json") else 1, p.name))
    for path in files:
        if path.name.startswith("_"):
            continue
        data = _load(path)
        if not isinstance(data, dict):
            continue
        group = path.name.replace(".verified.json", "").replace(".json", "")
        verified = path.name.endswith(".verified.json")
        if group.startswith("ottenimento_"):
            # come si ottengono le sculture: si aggancia ai comandanti dopo il merge
            acquisition_files.append((path.name, data))
            continue
        if group not in TOPIC_FILES and "commanders" not in data:
            TOPIC_FILES[group] = f"{group}.json"  # argomento non previsto: copiato con il suo nome
        if group in TOPIC_FILES:
            if group not in index["topics"] or verified:
                (data_dir / TOPIC_FILES[group]).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
                index["topics"][group] = {"file": TOPIC_FILES[group], "from": path.name, "verified": verified,
                                          "conflicts": len(data.get("conflicts") or []), "gaps": len(data.get("gaps") or [])}
            continue
        recs = data.get("commanders") or []
        n_new = 0
        for rec in recs:
            if not isinstance(rec, dict) or not rec.get("name"):
                continue
            # Legendary e non-Legendary con lo stesso nome sono comandanti
            # diversi (es. Pelagius Epic e Pelagius Legendary del 2026).
            tier = "L" if str(rec.get("rarity") or "").lower() == "legendary" else "N"
            key = f"{normalize_name(rec['name'])}|{tier}"
            rec = dict(rec)
            rec.setdefault("_group", group)
            rec["_verified_file"] = verified
            if key not in commanders:
                commanders[key] = rec
                n_new += 1
            else:
                cur = commanders[key]
                if (rec.get("_verified_file"), _filled(rec)) > (cur.get("_verified_file"), _filled(cur)):
                    commanders[key] = _merge_records(rec, cur)
                else:
                    commanders[key] = _merge_records(cur, rec)
        index["groups"][path.name] = {"records": len(recs), "new": n_new, "verified": verified,
                                      "unreachable": data.get("unreachable") or []}

    # sculture: come ottenerle (campo "acquisition" su ogni comandante) e stelle per rarità
    attached, missing = 0, []
    stars: Dict[str, Any] = {}
    for fname, data in acquisition_files:
        if data.get("stars_by_rarity"):
            stars = {"stars_by_rarity": data.get("stars_by_rarity"), "xp_table": data.get("xp_table"),
                     "sources": data.get("sources") or [], "from": fname}
        for rec in data.get("commanders") or []:
            if not isinstance(rec, dict) or not rec.get("name"):
                continue
            tier = "L" if str(rec.get("rarity") or "").lower() == "legendary" else "N"
            key = f"{normalize_name(rec['name'])}|{tier}"
            target = commanders.get(key)
            if target is None:
                missing.append(rec["name"])
                continue
            target["acquisition"] = {k: rec.get(k) for k in (
                "obtain", "universal_sculptures_ok", "best_free_path", "f2p_viable", "notes",
                "sources", "gaps", "conflicts") if rec.get(k) not in (None, [], "")}
            target["acquisition"]["from"] = fname
            attached += 1
    if stars:
        (data_dir / "stelle_per_classe.json").write_text(json.dumps(stars, ensure_ascii=False, indent=2), encoding="utf-8")
    index["acquisition"] = {"attached": attached, "not_matched": missing, "stars_file": bool(stars)}

    out_list = sorted(commanders.values(), key=lambda c: (c.get("rarity") != "Legendary", c.get("name", "")))
    (data_dir / "commanders.json").write_text(
        json.dumps({"generated": index["generated"], "count": len(out_list), "commanders": out_list}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    gaps = _load(fragments_dir / "_gaps.json") if (fragments_dir / "_gaps.json").exists() else None
    index["gaps_report"] = gaps
    index["commanders"] = len(out_list)
    index["with_skills"] = sum(1 for c in out_list if c.get("skills"))
    index["with_pairings"] = sum(1 for c in out_list if c.get("pairings"))
    index["with_ratings"] = sum(1 for c in out_list if c.get("ratings"))
    index["conflicts_total"] = sum(len(c.get("conflicts") or []) for c in out_list)
    (data_dir / "kb_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return index


if __name__ == "__main__":
    print(json.dumps(merge(), ensure_ascii=False, indent=2))
