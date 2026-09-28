"""Motore del consigliere militare.

Input: KnowledgeBase + profilo account (vedi account_profile.example.json).
Output: raccomandazioni per raccolta, barbari, difesa, attacco e un piano di
addestramento eseguibile dal bot. Obiettivo: massimo danno con le minori
perdite, quindi: tier più alto sbloccato per il combattimento, T1 assedio
per la raccolta, coppie con sinergia documentata, formazione coerente con
il tipo di danno (skill/smite/combo) del comandante primario.

Vincoli non negoziabili, codificati qui e non nel prompt:
  * mai spendere gemme (``no_gems`` sempre True nel piano);
  * ogni azione che attacca giocatori o consuma materiali rari esce con
    ``requires_confirmation=True`` e il bot deve fermarsi e chiedere.
"""

from __future__ import annotations

import datetime as _dt
from typing import Any, Dict, List, Optional, Tuple

from .kb import KnowledgeBase, TROOP_TYPES, normalize_name, iter_owned
from .strategies import StrategyBook

ROLES = ("gathering", "barbarians", "defense", "attack")

# Materiali/valute rari: ogni consumo richiede conferma. La lista può essere
# estesa dalla KB (armamenti.rare_materials, equipaggiamento.rare_materials).
RARE_MATERIALS_DEFAULT = [
    "gems", "gemme",
    "sage's testimony", "autarch testimony", "conquest coins",
    "transmutation stone", "transmutation crystal", "conversion stone",
    "gold coin", "silver coin",
    "legendary material", "legendary blueprint", "gold head", "gold key", "golden key",
    "universal legendary sculpture", "legendary sculpture", "epic sculpture",
    "book of covenant", "arch of triumph", "commander sculpture",
]

# Formazione di default per ruolo, se la KB non ne indica una migliore.
DEFAULT_FORMATION = {
    "gathering": ("Line", "+10% velocità di raccolta"),
    "barbarians": ("Wedge", "+5% danno skill: quasi tutti i nuke per barbari sono skill"),
    "defense": ("Hollow Square", "riduzione danno; Tercio se difendi la città con truppe miste"),
    "attack": ("Wedge", "+5% danno skill; Arch se il primario fa danno normale"),
}


def _dev_score(owned: Dict[str, Any]) -> float:
    """Sviluppo del comandante posseduto: livello, skill, expertise, stelle."""
    level = float(owned.get("level") or 0)
    skills = owned.get("skills") or []
    skill_sum = sum(int(s) for s in skills if s is not None)
    expertise = 1.0 if owned.get("expertise") else 0.0
    stars = float(owned.get("stars") or 0)
    return (level / 60.0) * 3.0 + (skill_sum / 20.0) * 4.0 + expertise + (stars / 5.0) * 1.0


def _highest_tier(profile: Dict[str, Any], troop_type: str) -> int:
    unl = profile.get("troop_tiers_unlocked") or {}
    if troop_type in unl and unl[troop_type]:
        return int(unl[troop_type])
    troops = (profile.get("troops") or {}).get(troop_type) or {}
    tiers = [int(k[1:]) for k, v in troops.items() if k.upper().startswith("T") and (v or 0) > 0]
    return max(tiers) if tiers else 1


def _troop_count(profile: Dict[str, Any], troop_type: str, tier: int) -> int:
    troops = (profile.get("troops") or {}).get(troop_type) or {}
    return int(troops.get(f"T{tier}") or troops.get(f"t{tier}") or 0)


def _equipment_matches(owned: Dict[str, Any], troop_type: str) -> float:
    eq = owned.get("equipment") or {}
    text = " ".join(str(v) for v in eq.values() if v).lower()
    if not text:
        return 0.0
    hits = 0
    for key in (troop_type, {"infantry": "hope cloak", "cavalry": "khan", "archer": "revival"}.get(troop_type, "")):
        if key and key in text:
            hits += 1
    return min(1.0, hits * 0.5)


class MilitaryAdvisor:
    def __init__(self, kb: Optional[KnowledgeBase] = None, data_dir=None, strategies: Optional[StrategyBook] = None):
        if kb is None:
            kb = KnowledgeBase(data_dir) if data_dir else KnowledgeBase()
        self.kb = kb
        self.strategies = strategies or StrategyBook(self.kb.data_dir)
        self.rare_materials = set(m.lower() for m in RARE_MATERIALS_DEFAULT)
        for src in (self.kb.armaments, self.kb.equipment):
            for m in src.get("rare_materials") or []:
                name = m.get("name") if isinstance(m, dict) else m
                if name:
                    self.rare_materials.add(str(name).lower())

    # ------------------------------------------------------------------ util
    def is_rare_material(self, name: str) -> bool:
        n = (name or "").lower()
        return any(r in n for r in self.rare_materials)

    def _owned_with_kb(self, profile: Dict[str, Any]) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
        out = []
        for owned in iter_owned(profile):
            kb = self.kb.find(owned["name"], owned.get("rarity"))
            if kb is None:
                kb = {"name": owned["name"], "specialties": owned.get("specialties") or [], "_unknown": True}
            out.append((owned, kb))
        return out

    # --------------------------------------------------------------- scoring
    def score(self, owned: Dict[str, Any], kb: Dict[str, Any], role: str, profile: Dict[str, Any]) -> Tuple[float, List[str]]:
        why: List[str] = []
        specs = KnowledgeBase.specialties(kb)
        tt = KnowledgeBase.troop_type(kb)
        base = 0.0

        if role == "gathering":
            r = KnowledgeBase.rating(kb, "gathering")
            if "gathering" in specs:
                base = max(base, 9.0); why.append("specialità Gathering")
            if r is not None:
                base = max(base, r)
            gb = self.kb.gathering_bonus(kb)
            if gb:
                base += min(gb, 50) / 25.0; why.append(f"bonus raccolta/carico fino a {gb:.0f}% nelle skill")
            if "gathering" not in specs and gb == 0:
                base -= 4.0  # un combattente che raccoglie spreca un comandante
        elif role == "barbarians":
            r = KnowledgeBase.rating(kb, "barbarians")
            if r is not None:
                base = max(base, r)
            if "peacekeeping" in specs:
                base = max(base, 8.0); why.append("specialità Peacekeeping (meno AP, più danno ai barbari)")
            bb = self.kb.barbarian_bonus_pct(kb)
            if bb:
                base += min(bb, 50) / 12.5; why.append(f"+{bb:.0f}% danno ai barbari nelle skill")
            # i nuke AoE circolari (es. YSG) sono ottimi per catene di barbari
            of = KnowledgeBase.rating(kb, "open_field") or 0.0
            base += of * 0.35
            if r is not None:
                why.append(f"rating barbari {r:.1f}/10")
            if of:
                why.append(f"rating campo aperto {of:.1f}/10")
            if "gathering" in specs:
                base -= 6.0
        elif role == "defense":
            r = KnowledgeBase.rating(kb, "garrison")
            if r is not None:
                base = max(base, r)
                why.append(f"rating guarnigione {r:.1f}/10 (media delle fonti)")
            if "garrison" in specs:
                base = max(base, 7.5); why.append("specialità Garrison")
            if "gathering" in specs:
                base -= 6.0
        else:  # attack
            of = KnowledgeBase.rating(kb, "open_field")
            ra = KnowledgeBase.rating(kb, "rally")
            vals = [v for v in (of, ra) if v is not None]
            if vals:
                base = max(vals) * 0.7 + (sum(vals) / len(vals)) * 0.3
                why.append("rating " + ", ".join(
                    f"{lbl} {v:.1f}/10" for lbl, v in (("campo aperto", of), ("rally", ra)) if v is not None)
                    + " (media delle fonti)")
            if "conquering" in specs or "versatility" in specs:
                base += 0.5
            if "gathering" in specs:
                base -= 8.0
            if kb.get("_unknown"):
                base = 3.0; why.append("comandante non in KB: punteggio prudenziale")

        dev = _dev_score(owned)
        why.append(f"sviluppo {dev:.1f}/9 (lv {owned.get('level', '?')}, skill {''.join(str(s) for s in owned.get('skills') or []) or '?'})")

        # truppe disponibili del tipo giusto: senza truppe il comandante non serve
        tier_bonus = 0.0
        if tt in TROOP_TYPES:
            tier = _highest_tier(profile, tt)
            tier_bonus = tier * 0.4
            if role != "gathering":
                why.append(f"{tt} T{tier} disponibili")
        eqb = _equipment_matches(owned, tt)
        if eqb:
            why.append("equipaggiamento coerente col tipo di truppa")

        total = base + dev + tier_bonus + eqb
        return total, why

    # ------------------------------------------------------------- pairings
    def best_pair(self, role: str, ranked: List[Tuple[float, Dict[str, Any], Dict[str, Any], List[str]]]) -> Optional[Dict[str, Any]]:
        if not ranked:
            return None
        by_norm = {normalize_name(kb.get("name", "")): (sc, ow, kb) for sc, ow, kb, _ in ranked}
        best = None
        purpose_words = {
            "gathering": ("gather", "farm"),
            "barbarians": ("barbar", "fort", "pve", "peacekeep", "nuke"),
            "defense": ("garrison", "defen", "city"),
            "attack": ("field", "open", "rally", "pvp", "kvk", "canyon"),
        }[role]
        for sc, ow, kb, why in ranked[:6]:
            for p in self.kb.pairings_for(kb):
                partner = self.kb.find(str(p.get("partner") or ""))
                if partner is None:
                    continue
                pn = normalize_name(partner.get("name", ""))
                if pn not in by_norm or pn == normalize_name(kb.get("name", "")):
                    continue
                psc, pow_, pkb = by_norm[pn]
                purpose = str(p.get("purpose") or "").lower()
                purpose_match = any(w in purpose for w in purpose_words)
                synergy = 1.5 if purpose_match else 0.5
                same_troops = KnowledgeBase.troop_type(kb) == KnowledgeBase.troop_type(pkb)
                flexible = {KnowledgeBase.troop_type(kb), KnowledgeBase.troop_type(pkb)} & {"leadership", "integration"}
                if not purpose_match and not same_troops and not flexible and role != "gathering":
                    continue  # documentata per un altro scopo e con truppe miste: non vale qui
                if same_troops or flexible:
                    synergy += 1.0
                elif role != "gathering":
                    # due specialisti di tipi diversi: i bonus passivi del secondo vanno persi
                    synergy -= 4.0
                total = sc + 0.6 * psc + synergy
                this_as = str(p.get("this_as") or "either").lower()
                source_order = this_as
                if not purpose_match:
                    this_as = "either"  # l'ordine indicato valeva per un altro scopo
                if this_as == "primary":
                    primary, secondary = kb, pkb
                elif this_as == "secondary":
                    primary, secondary = pkb, kb
                else:
                    # "either": i talenti contano solo per il primario, quindi
                    # primario = chi ha il punteggio più alto per questo ruolo
                    primary, secondary = (kb, pkb) if sc >= psc else (pkb, kb)
                note = p.get("note") or ""
                src_primary = kb if source_order == "primary" else (pkb if source_order == "secondary" else None)
                if src_primary is not None and src_primary is not primary:
                    note += (f" [Ordine scelto per punteggio in questo ruolo: la fonte indica "
                             f"{src_primary.get('name')} primario per '{p.get('purpose') or 'altro scopo'}'.]")
                cand = {
                    "primary": primary.get("name"), "secondary": secondary.get("name"),
                    "score": round(total, 2), "documented": True,
                    "note": note.strip(), "sources": KnowledgeBase.sources_of(kb)[:2],
                }
                if best is None or cand["score"] > best["score"]:
                    best = cand
        # Coppia euristica: il migliore per il ruolo + il migliore compatibile
        # come tipo di truppa. Compete alla pari con quella documentata, così
        # una coppia citata dalle guide per un altro scopo non vince per forza.
        sc, ow, kb, _ = ranked[0]
        tt = KnowledgeBase.troop_type(kb)
        mate, msc = None, 0.0
        for sc2, ow2, kb2, _ in ranked[1:]:
            tt2 = KnowledgeBase.troop_type(kb2)
            if role != "gathering" and "gathering" in KnowledgeBase.specialties(kb2):
                continue  # un raccoglitore in una marcia da combattimento spreca il posto
            if tt2 == tt or {tt, tt2} & {"leadership", "integration"} or role == "gathering":
                mate, msc = kb2, sc2
                break
        heuristic = {
            "primary": kb.get("name"), "secondary": mate.get("name") if mate else None,
            "score": round(sc + 0.6 * msc + (1.0 if mate else 0.0), 2), "documented": False,
            "note": "coppia non documentata nelle fonti: scelta per punteggio e tipo di truppa compatibile", "sources": [],
        }
        if best is None or heuristic["score"] > best["score"]:
            return heuristic
        return best

    # ------------------------------------------------------------ formation
    def formation_for(self, role: str, primary_kb: Dict[str, Any]) -> Dict[str, Any]:
        rec = primary_kb.get("recommended_formation")
        specs = KnowledgeBase.specialties(primary_kb)
        name, reason = DEFAULT_FORMATION[role]
        if role in ("attack", "barbarians"):
            if "combo" in specs:
                name, reason = "Delta", "+10% danno Combo (specialità del primario)"
            elif "smite" in specs:
                name, reason = "Pincer", "+10% danno Smite (specialità del primario)"
            elif "attack" in specs and "skill" not in specs:
                name, reason = "Arch", "+5% danno da attacco: il primario scala sul danno normale"
        if rec and role != "gathering":
            rec_s = str(rec)
            low = rec_s.lower()
            pve_words = ("barbar", "farm", "fort", "pve", "gather")
            def_words = ("garrison", "defen", "guarnig")
            is_pve = any(w in low for w in pve_words)
            is_def = any(w in low for w in def_words)
            fits = (role == "barbarians" and is_pve) or (role == "defense" and is_def) or \
                   (role == "attack" and not is_pve and not is_def)
            found = self._formation_in_text(rec_s) if fits else None
            if found:
                name, reason = found, f"consigliata dalla guida del comandante ({rec_s[:120]})"
        f = self.kb.formation_by_name(name)
        return {"name": name, "reason": reason, "kb": f}

    def _formation_in_text(self, text: str) -> Optional[str]:
        """Estrae il nome di una formazione da un testo libero della guida
        (es. "allclash: Arch (le alternative sono PRO)" -> "Arch").
        Preferisce il nome più lungo: "Triple Line" prima di "Line"."""
        names = {str(f.get("name")) for f in self.kb.formations() if f.get("name")}
        names |= {"Arch", "Wedge", "Wedge II", "V", "Echelon", "Hollow Square", "Line", "Double Line",
                  "Triple Line", "Testudo", "Circle", "Staggered", "Delta", "Tercio", "Pincer"}
        low = f" {normalize_name(text)} "
        best = None
        for n in sorted(names, key=len, reverse=True):
            key = normalize_name(n.replace("Formation", ""))
            if key and len(key) > 1 and f" {key} " in low:
                best = n.replace(" Formation", "").strip()
                break
        return best

    # ----------------------------------------------------------------- troops
    def troops_for(self, role: str, primary_kb: Dict[str, Any], profile: Dict[str, Any],
                   secondary_kb: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        tt = KnowledgeBase.troop_type(primary_kb)
        cap = int((profile.get("march") or {}).get("capacity") or 0)
        if role == "gathering":
            return {"troop_type": "siege", "tier": 1, "count": cap,
                    "reason": "T1 assedio: carico ~4x, costo e tempo minimi, perdite irrilevanti"}
        if tt in TROOP_TYPES:
            tier = _highest_tier(profile, tt)
            return {"troop_type": tt, "tier": tier, "count": cap,
                    "reason": f"marcia piena di {tt} T{tier}: il tier più alto riduce le perdite a parità di danno"}
        # primario flessibile (Leadership/Integration) con secondario specialista:
        # le passive del secondario valgono solo per il suo tipo di truppa
        st = KnowledgeBase.troop_type(secondary_kb) if secondary_kb else ""
        if st in ("infantry", "cavalry", "archer"):
            tier = _highest_tier(profile, st)
            return {"troop_type": st, "tier": tier, "count": cap,
                    "reason": f"primario flessibile, secondario specialista {st}: marcia piena di {st} T{tier} "
                              "così le passive del secondario si applicano a tutta la marcia"}
        # leadership / integration: usa il tipo con il tier più alto e più truppe
        best_tt, best_tier, best_n = "infantry", 1, -1
        for t in ("infantry", "cavalry", "archer"):
            tier = _highest_tier(profile, t)
            n = _troop_count(profile, t, tier)
            if (tier, n) > (best_tier, best_n):
                best_tt, best_tier, best_n = t, tier, n
        return {"troop_type": best_tt, "tier": best_tier, "count": cap,
                "reason": "primario Leadership/Integration: usa il tipo con il tier più alto che possiedi; "
                          "truppe miste solo se la skill lo richiede (es. Aethelflaed 3 tipi)"}

    # ------------------------------------------------------------- main API
    def recommend(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        pairs = self._owned_with_kb(profile)
        unknown = [ow["name"] for ow, kb in pairs if kb.get("_unknown")]
        result: Dict[str, Any] = {
            "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
            "kb_stats": self.kb.stats(),
            "unknown_commanders": unknown,
            "roles": {},
            "constraints": {"no_gems": True, "confirm_before_attacking_players": True,
                            "confirm_before_consuming_rare_materials": True},
        }
        # i record KB dei comandanti POSSEDUTI, per nome: così un nome che esiste
        # in due rarità si risolve sempre sulla versione che hai davvero
        self._owned_kb = {normalize_name(kb.get("name", "")): kb for ow, kb in pairs}
        all_ranked: Dict[str, list] = {}
        for role in ROLES:
            ranked = []
            for ow, kb in pairs:
                sc, why = self.score(ow, kb, role, profile)
                ranked.append((sc, ow, kb, why))
            ranked.sort(key=lambda r: r[0], reverse=True)
            all_ranked[role] = ranked
            pair = self.best_pair(role, ranked)
            primary_kb = self._lookup_owned(pair.get("primary")) if pair else None
            primary_kb = primary_kb or (ranked[0][2] if ranked else {})
            secondary_kb = self._lookup_owned(pair.get("secondary")) if pair else None
            role_out = {
                "pair": pair,
                "ranking": [{"name": kb.get("name"), "score": round(sc, 2), "why": why} for sc, ow, kb, why in ranked[:5]],
                "talent_build": self.talents_for(role, primary_kb) if primary_kb else None,
                "formation": self.formation_for(role, primary_kb) if primary_kb else None,
                "troops": self.troops_for(role, primary_kb, profile, secondary_kb) if primary_kb else None,
                "sources": KnowledgeBase.sources_of(primary_kb)[:3] if primary_kb else [],
            }
            result["roles"][role] = role_out
        self._apply_strategy_pairs(profile, result)
        result["gathering_marches"] = self.gathering_marches(profile, all_ranked.get("gathering") or [], result)
        result["training_plan"] = self.training_plan(profile, result["roles"])
        result["daily_checklist"] = self.strategies.daily_checklist()
        result["bot_rules"] = self.strategies.bot_rules()
        result["strategy_stats"] = self.strategies.stats()
        result["warnings"] = self._warnings(profile, result)
        return result

    def talents_for(self, role: str, cmd: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Build dei talenti per il primario in questo ruolo.
        1) la build specifica del comandante per questo scopo, se la guida ce l'ha;
        2) altrimenti la build standard del ruolo (talenti.json), scelta in base
           alle specialità del primario, con l'elenco degli alberi che ha davvero:
           un comandante può spendere punti solo nei suoi 3 alberi."""
        own = self.kb.talent_build(cmd, role, strict=True)
        if own:
            out = dict(own)
            out["_origin"] = "build del comandante dalla sua guida"
            return out
        specs = KnowledgeBase.specialties(cmd)
        key = role
        if role == "attack":
            if "combo" in specs:
                key = "combo"
            elif "smite" in specs:
                key = "smite"
            elif "defense" in specs and "skill" not in specs:
                key = "open_field_tank"
            else:
                key = "open_field_nuke"
        gb = self.strategies.talent_role_build(key)
        if not gb:
            return self.kb.talent_build(cmd, role)  # meglio di niente, ma per altro scopo
        trees = [str(t) for t in (gb.get("trees") or [])]
        usable = [t for t in trees if t.lower() in specs]
        missing = [t for t in trees if t.lower() not in specs]
        note = ""
        if missing:
            note = (f"{cmd.get('name')} non ha gli alberi {', '.join(missing)}: "
                    f"usa solo {', '.join(usable) if usable else 'i suoi alberi'} "
                    f"({', '.join(s.title() for s in specs) or 'specialità ignote'}).")
        return {
            "purpose": gb.get("role"),
            "trees": trees,
            "usable_trees": usable,
            "key_talents": [f"{t.get('name')} {t.get('points') or ''}".strip() for t in (gb.get("talents_in_order") or [])],
            "stat_summary": gb.get("stat_summary"),
            "notes": note,
            "sources": gb.get("sources") or [],
            "_origin": "build standard per ruolo (alberi dei talenti)",
        }

    def _lookup_owned(self, name: Optional[str]) -> Optional[Dict[str, Any]]:
        if not name:
            return None
        owned = getattr(self, "_owned_kb", {}) or {}
        return owned.get(normalize_name(name)) or self.kb.find(name)

    def gathering_marches(self, profile: Dict[str, Any], ranked: list, result: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Una marcia di raccolta per ogni comandante da raccolta: i talenti
        (Superior Tools ecc.) valgono solo per il primario, quindi ogni
        raccoglitore guida la propria marcia. I comandanti già usati nelle
        marce da combattimento restano liberi per quelle."""
        march = profile.get("march") or {}
        n = max(1, int(march.get("max_marches") or 1) - 1)
        busy = set()
        for role in ("barbarians", "defense", "attack"):
            p = (result["roles"].get(role) or {}).get("pair") or {}
            busy |= {normalize_name(str(p.get("primary") or "")), normalize_name(str(p.get("secondary") or ""))}
        gatherers = [(sc, ow, kb) for sc, ow, kb, _ in ranked
                     if "gathering" in KnowledgeBase.specialties(kb) or self.kb.gathering_bonus(kb) > 0]
        others = [(sc, ow, kb) for sc, ow, kb, _ in ranked
                  if (sc, ow, kb) not in gatherers and normalize_name(kb.get("name", "")) not in busy]
        primaries = gatherers[:n]
        spare = gatherers[n:] + others
        marches = []
        for i, (sc, ow, kb) in enumerate(primaries, 1):
            sec = spare.pop(0)[2] if spare else None
            marches.append({
                "march": i, "primary": kb.get("name"), "secondary": sec.get("name") if sec else None,
                "troops": {"troop_type": "siege", "tier": 1, "count": int(march.get("capacity") or 0)},
                "formation": "Line",
                "talent_build": self.talents_for("gathering", kb),
                "note": "raccoglitore primario: i suoi talenti di raccolta valgono per questa marcia",
            })
        for j in range(len(marches) + 1, n + 1):
            if not spare:
                break
            sc, ow, kb = spare.pop(0)
            marches.append({"march": j, "primary": kb.get("name"), "secondary": None,
                            "troops": {"troop_type": "siege", "tier": 1, "count": int(march.get("capacity") or 0)},
                            "formation": "Line", "talent_build": None,
                            "note": "nessun altro raccoglitore disponibile: comandante libero, raccolta più lenta"})
        return marches

    def _apply_strategy_pairs(self, profile: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Se il libro delle strategie documenta una coppia che possiedi per
        difesa (garrison_pairs) o attacco (meta_pairs), la propone in testa
        alla raccomandazione: una coppia meta documentata batte l'euristica."""
        owned_names = [c["name"] for c in iter_owned(profile)]

        def attack_pairs():
            # il Sunset Canyon è una modalità a parte: non decide la marcia d'attacco
            return [p for p in self.strategies.meta_pairs()
                    if "canyon" not in str(p.get("mode") or "").lower() or "field" in str(p.get("mode") or "").lower()]

        for role, getter in (("defense", self.strategies.garrison_pairs), ("attack", attack_pairs)):
            owned_pairs = StrategyBook.owned_pairs(getter(), owned_names)
            if not owned_pairs:
                continue
            best = owned_pairs[0]
            out = result["roles"][role]
            out["strategy_pairs_owned"] = owned_pairs
            cur = out.get("pair") or {}
            same = {normalize_name(str(cur.get("primary") or "")), normalize_name(str(cur.get("secondary") or ""))} == \
                   {normalize_name(str(best.get("primary") or "")), normalize_name(str(best.get("secondary") or ""))}
            if not cur.get("documented") or same:
                out["pair"] = {
                    "primary": best.get("primary"), "secondary": best.get("secondary"),
                    "score": cur.get("score"), "documented": True,
                    "note": f"coppia dal libro delle strategie ({best.get('mode') or best.get('budget') or role}): {best.get('why') or ''}",
                    "sources": best.get("sources") or [],
                }
                pk = self._lookup_owned(str(best.get("primary") or ""))
                sk = self._lookup_owned(str(best.get("secondary") or ""))
                if pk:
                    out["talent_build"] = self.talents_for(role, pk)
                    out["formation"] = self.formation_for(role, pk)
                    out["troops"] = self.troops_for(role, pk, profile, sk)
                    fname = self._formation_in_text(str(best.get("formation") or ""))
                    if fname:
                        out["formation"] = {"name": fname, "reason": f"indicata dalla guida per questa coppia ({str(best['formation'])[:120]})",
                                            "kb": self.kb.formation_by_name(fname)}

    # --------------------------------------------------------- training plan
    def training_plan(self, profile: Dict[str, Any], roles: Dict[str, Any]) -> Dict[str, Any]:
        """Piano che il bot può eseguire: ordini di addestramento, mai gemme.
        Obiettivo: per ogni ruolo una marcia piena del tipo/tier consigliato;
        per la raccolta tante marce di T1 assedio quante le marce disponibili."""
        march = profile.get("march") or {}
        cap = int(march.get("capacity") or 0)
        n_marches = int(march.get("max_marches") or 1)
        targets: Dict[Tuple[str, int], int] = {}
        reasons: Dict[Tuple[str, int], List[str]] = {}
        for role, out in roles.items():
            t = out.get("troops") or {}
            if not t.get("troop_type"):
                continue
            key = (t["troop_type"], int(t["tier"]))
            mult = max(1, n_marches - 1) if role == "gathering" else 1
            targets[key] = max(targets.get(key, 0), cap * mult)
            reasons.setdefault(key, []).append(f"{role}: {t.get('reason')}")
        orders = []
        for (tt, tier), target in sorted(targets.items()):
            have = _troop_count(profile, tt, tier)
            deficit = max(0, target - have)
            lower = {t2: _troop_count(profile, tt, t2) for t2 in range(1, tier)}
            upgradable = sum(v for t2, v in lower.items() if t2 >= tier - 1)
            if deficit <= 0:
                continue
            orders.append({
                "action": "train", "troop_type": tt, "tier": tier, "count": deficit,
                "have": have, "target": target, "reason": "; ".join(reasons[(tt, tier)]),
                "prefer_upgrade_from_lower_tier": upgradable if tier > 1 else 0,
                "no_gems": True, "use_speedups": "solo se già in inventario e se un evento premia l'addestramento",
                "requires_confirmation": False,
            })
        return {
            "orders": orders,
            "policy": [
                "Non usare mai gemme per truppe, code o velocizzazioni.",
                "Tenere sempre attiva una coda di addestramento (mai tempo morto in caserma/stalla/poligono/officina d'assedio).",
                "Se esistono truppe di tier inferiore, preferire l'upgrade quando c'è un evento che lo premia (più punti per risorsa).",
                "Non addestrare assedio sopra T1 per la raccolta.",
            ],
        }

    def _warnings(self, profile: Dict[str, Any], result: Dict[str, Any]) -> List[str]:
        w = []
        if not self.kb.commanders:
            w.append("KB comandanti vuota: esegui `python -m military_advisor build-kb` dopo la ricerca.")
        if result.get("unknown_commanders"):
            w.append("Comandanti non riconosciuti nella KB: " + ", ".join(result["unknown_commanders"]))
        if not (profile.get("march") or {}).get("capacity"):
            w.append("Capacità di marcia assente nel profilo: il piano di addestramento non può calcolare i conteggi.")
        if not profile.get("troops"):
            w.append("Conteggio truppe assente nel profilo: il piano assume 0 truppe.")
        for role, out in result["roles"].items():
            pair = out.get("pair") or {}
            if pair and not pair.get("documented"):
                w.append(f"{role}: coppia non documentata nelle fonti, scelta euristica.")
        return w

    # ---------------------------------------------------------------- report
    def render_report(self, result: Dict[str, Any]) -> str:
        it = {"gathering": "RACCOLTA", "barbarians": "BARBARI E FORTI", "defense": "DIFESA (guarnigione)", "attack": "ATTACCO (campo aperto / rally)"}
        lines = ["CONSIGLIERE MILITARE - Rise of Kingdoms", f"Generato: {result['generated_at']}",
                 f"KB: {result['kb_stats']}", ""]
        for role, out in result["roles"].items():
            lines.append(f"== {it[role]} ==")
            pair = out.get("pair") or {}
            if pair:
                doc = "coppia documentata" if pair.get("documented") else "coppia euristica"
                lines.append(f"Coppia: {pair.get('primary')} (primario) + {pair.get('secondary') or '-'} (secondario)  [{doc}]")
                if pair.get("note"):
                    lines.append(f"  Nota: {pair['note']}")
            tb = out.get("talent_build")
            if tb:
                origin = f" [{tb['_origin']}]" if tb.get("_origin") else ""
                lines.append(f"Talenti ({tb.get('purpose')}){origin}: alberi {', '.join(str(t) for t in (tb.get('trees') or []))}; "
                             f"chiave: {', '.join(str(t) for t in (tb.get('key_talents') or []))[:300]}")
                if tb.get("notes") and tb.get("_origin", "").startswith("build standard"):
                    lines.append(f"  Attenzione: {tb['notes']}")
            fm = out.get("formation") or {}
            if fm:
                lines.append(f"Formazione: {fm.get('name')} - {fm.get('reason')}")
            tr = out.get("troops") or {}
            if tr:
                lines.append(f"Truppe: {tr.get('count')} x {tr.get('troop_type')} T{tr.get('tier')} - {tr.get('reason')}")
            lines.append("Classifica:")
            for r in out.get("ranking") or []:
                lines.append(f"  - {r['name']}: {r['score']}  ({'; '.join(r['why'])})")
            src = out.get("sources") or []
            if src:
                lines.append("Fonti: " + "; ".join(f"{s.get('url')} ({s.get('page_date') or 'n/d'}, letto {s.get('retrieved') or '?'})" for s in src))
            lines.append("")
        gm = result.get("gathering_marches") or []
        if gm:
            lines.append("== MARCE DI RACCOLTA ==")
            for m in gm:
                lines.append(f"  {m['march']}. {m['primary']} + {m.get('secondary') or '-'} | {m['troops']['count']} x siege T1 | "
                             f"Line | {m['note']}")
            lines.append("")
        lines.append("== PIANO DI ADDESTRAMENTO ==")
        plan = result.get("training_plan") or {}
        if not plan.get("orders"):
            lines.append("Nessun ordine: obiettivi già coperti o profilo incompleto.")
        for o in plan.get("orders") or []:
            lines.append(f"  - Addestra {o['count']} {o['troop_type']} T{o['tier']} (hai {o['have']}, obiettivo {o['target']}); "
                         f"upgradabili da tier inferiore: {o['prefer_upgrade_from_lower_tier']}. Motivo: {o['reason']}")
        for p in plan.get("policy") or []:
            lines.append(f"  * {p}")
        lines.append("")
        dc = result.get("daily_checklist") or []
        if dc:
            lines.append("== ROUTINE GIORNALIERA (dal libro delle strategie) ==")
            for item in dc:
                if item.get("requires_confirmation"):
                    flag = " [CONFERMA]"
                else:
                    cw = StrategyBook.conditional_confirmation(item)
                    flag = f" [CONFERMA SE: {cw[:140]}]" if cw else ""
                lines.append(f"  {item.get('order', '?')}. {item.get('task')}{flag}")
            lines.append("  (regole if/then complete di ogni voce: python -m military_advisor daily)")
            lines.append("")
        rules = result.get("bot_rules") or []
        if rules:
            lines.append(f"== REGOLE PER IL BOT: {len(rules)} caricate ({sum(1 for r in rules if r.get('requires_confirmation'))} con conferma) ==")
            for r in rules[:15]:
                flag = " [CONFERMA]" if r.get("requires_confirmation") else ""
                lines.append(f"  - [{r.get('topic')}] {r.get('when')} -> {r.get('then')}{flag}")
            if len(rules) > 15:
                lines.append(f"  ... altre {len(rules) - 15} regole in raccomandazioni.json")
            lines.append("")
        lines.append("== VINCOLI ==")
        lines.append("  * Mai gemme. * Conferma prima di attaccare giocatori. * Conferma prima di consumare materiali rari.")
        if result.get("warnings"):
            lines.append("")
            lines.append("== AVVISI ==")
            lines.extend(f"  ! {w}" for w in result["warnings"])
        return "\n".join(lines)

    # -------------------------------------------------- gate per il bot
    def gate(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Il bot chiama gate(azione) prima di eseguire qualsiasi cosa.
        Ritorna {'allowed': bool, 'requires_confirmation': bool, 'reason': str}."""
        kind = str(action.get("kind") or "").lower()
        target = str(action.get("target") or "").lower()
        consumes = [str(x) for x in (action.get("consumes") or [])]
        if kind in ("verification", "captcha", "anti_bot_check", "solve_verification") or action.get("verification_window"):
            # I ToS Lilith e il Conduct Score (1.1.07) prevedono una finestra di
            # verifica anti-plugin: il bot non deve mai provare a risolverla.
            return {"allowed": False, "requires_confirmation": False, "stop_bot": True,
                    "reason": "finestra di verifica anti-plugin: fermare il bot, salvare lo screenshot e avvisare il proprietario; non tentare di risolverla"}
        blob = f"{kind} {target} {' '.join(consumes)}".lower()
        if "shield" in blob or "scudo" in blob or "scudi" in blob:
            return {"allowed": False, "requires_confirmation": False,
                    "reason": "scudi vietati dal proprietario (28/09/2026): non attivare, avvisare il proprietario"}
        if kind in ("delete_account", "switch_account", "link_account", "create_character", "account_settings"):
            return {"allowed": False, "requires_confirmation": False,
                    "reason": "impostazioni dell'account: mai toccate dal bot"}
        if "gem" in " ".join(consumes).lower() or action.get("spends_gems"):
            return {"allowed": False, "requires_confirmation": False, "reason": "spende gemme: vietato"}
        if kind in ("attack", "rally", "scout") and target in ("player", "city", "giocatore", "citta", "città", "flag", "alliance"):
            return {"allowed": True, "requires_confirmation": True, "reason": "attacco a un giocatore: serve conferma"}
        rare = [c for c in consumes if self.is_rare_material(c)]
        if rare:
            return {"allowed": True, "requires_confirmation": True, "reason": "consuma materiali rari: " + ", ".join(rare)}
        return {"allowed": True, "requires_confirmation": False, "reason": "ok"}
