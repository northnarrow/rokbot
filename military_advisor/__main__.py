"""CLI del consigliere militare.

  python -m military_advisor build-kb                 # unisce data/fragments -> data/*.json
  python -m military_advisor kb-stats                 # quanti comandanti/fonti ha la KB
  python -m military_advisor commander "Sun Tzu"      # scheda con fonti
  python -m military_advisor report --profile p.json  # raccomandazioni + piano (testo it)
  python -m military_advisor report --profile p.json --json out.json
  python -m military_advisor validate --profile p.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .advisor import MilitaryAdvisor
from .kb import KnowledgeBase
from .account_reader import validate_profile


def main(argv=None) -> int:
    # Windows: con output reindirizzato su file la codifica di default è cp1252
    # e nomi come "Šárka" farebbero fallire la stampa.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="military_advisor")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build-kb")
    sub.add_parser("kb-stats")
    sub.add_parser("rules")
    sub.add_parser("heads", help="come ottenere le sculture di ogni comandante, senza gemme")
    sub.add_parser("daily")
    pc = sub.add_parser("phone-check", help="controllo del telefono via ADB, sola lettura")
    pc.add_argument("--out", default="test_telefono")
    pcc = sub.add_parser("pc-check", help="controllo del client PC di Rise of Kingdoms, sola lettura")
    pcc.add_argument("--out", default="test_pc")
    c = sub.add_parser("commander"); c.add_argument("name")
    r = sub.add_parser("report"); r.add_argument("--profile", required=True); r.add_argument("--json")
    v = sub.add_parser("validate"); v.add_argument("--profile", required=True)
    args = ap.parse_args(argv)

    if args.cmd == "build-kb":
        from .merge_kb import merge
        idx = merge()
        print(json.dumps({k: idx[k] for k in ("commanders", "with_skills", "with_pairings", "with_ratings", "conflicts_total", "topics")}, ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "kb-stats":
        from .strategies import StrategyBook
        out = KnowledgeBase().stats()
        out["strategies"] = StrategyBook().stats()
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "heads":
        kb = KnowledgeBase()
        order = {"si": 0, "lento": 1, "no": 2}
        rows = []
        for c in kb.commanders:
            a = c.get("acquisition") or {}
            if not a:
                continue
            free = [o.get("source") for o in (a.get("obtain") or []) if o.get("free")]
            rows.append((order.get(str(a.get("f2p_viable")), 3), c.get("rarity") or "", c["name"], a, free))
        rows.sort(key=lambda r: (r[0], r[1] != "Legendary", r[2]))
        for _, rar, name, a, free in rows:
            uni = {True: "universali sì", False: "universali NO"}.get(a.get("universal_sculptures_ok"), "universali ?")
            print(f"[{a.get('f2p_viable') or '?':5}] {name} ({rar}, {uni}) - gratis: {', '.join(map(str, free)) or 'nessuna fonte gratuita'}")
            if a.get("best_free_path"):
                print(f"         percorso senza gemme: {a['best_free_path'][:220]}")
        return 0
    if args.cmd == "pc-check":
        from .pc_tools import pc_report
        rep = pc_report(Path(args.out))
        for s in rep["steps"]:
            print(f"[{'OK ' if s['ok'] else 'ERR'}] {s['step']}: {s.get('value') if s['ok'] else s.get('error')}")
        return 0 if rep.get("ok") else 1
    if args.cmd == "phone-check":
        from .adb_tools import phone_report
        rep = phone_report(Path(args.out))
        for s in rep["steps"]:
            mark = "OK " if s["ok"] else "ERR"
            print(f"[{mark}] {s['step']}: {s.get('value') if s['ok'] else s.get('error')}")
        ok = rep.get("rok_in_foreground")
        print(f"Rise of Kingdoms visibile e pronto ai tocchi: {'SI' if ok else 'NO'}"
              + (f" ({rep['motivo']})" if not ok and rep.get("motivo") else ""))
        return 0 if all(s["ok"] for s in rep["steps"]) else 1
    if args.cmd in ("rules", "daily"):
        from .strategies import StrategyBook
        sb = StrategyBook()
        print(json.dumps(sb.bot_rules() if args.cmd == "rules" else sb.daily_checklist(), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "commander":
        kb = KnowledgeBase()
        cmd = kb.find(args.name)
        if not cmd:
            print(f"Non trovato: {args.name}", file=sys.stderr)
            return 1
        print(json.dumps(cmd, ensure_ascii=False, indent=2))
        return 0
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if args.cmd == "validate":
        problems = validate_profile(profile)
        print("\n".join(problems) if problems else "OK")
        return 1 if problems else 0
    adv = MilitaryAdvisor()
    result = adv.recommend(profile)
    if args.json:
        Path(args.json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(adv.render_report(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
