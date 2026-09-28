"""Test del motore con una mini-KB sintetica (non dipende dalla ricerca)."""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from military_advisor.advisor import MilitaryAdvisor  # noqa: E402
from military_advisor.kb import KnowledgeBase, normalize_name  # noqa: E402
from military_advisor.account_reader import validate_profile  # noqa: E402


def _src(url="https://example.test/x", date="2026-01-02"):
    return [{"url": url, "site": "example", "page_date": date, "retrieved": "2026-09-27", "fields": ["*"]}]


@pytest.fixture()
def kb(tmp_path):
    cmds = [
        {"name": "Sun Tzu", "rarity": "Epic", "specialties": ["Infantry", "Garrison", "Skill"], "troop_type": "infantry",
         "skills": [{"slot": 1, "name": "Art of War", "type": "active", "rage": 1000, "effect": "Deals damage to 3 targets"}],
         "talent_builds": [{"purpose": "open_field", "trees": ["Skill", "Infantry"], "key_talents": ["Feral Nature"]},
                           {"purpose": "garrison", "trees": ["Garrison", "Infantry"], "key_talents": ["City Guardian"]}],
         "pairings": [{"partner": "Richard I", "this_as": "secondary", "purpose": "open field", "note": "AOE + tank"}],
         "ratings": [{"source_url": "x", "open_field": "A", "garrison": "A", "rally": "C"}], "sources": _src()},
        {"name": "Richard I", "rarity": "Legendary", "specialties": ["Infantry", "Garrison", "Defense"], "troop_type": "infantry",
         "skills": [], "talent_builds": [{"purpose": "garrison", "trees": ["Garrison"], "key_talents": ["Impregnable"]}],
         "pairings": [{"partner": "Sun Tzu", "this_as": "primary", "purpose": "garrison", "note": ""}],
         "ratings": [{"source_url": "x", "open_field": "A", "garrison": "A+", "rally": "C"}], "sources": _src()},
        {"name": "Cao Cao", "rarity": "Legendary", "specialties": ["Cavalry", "Peacekeeping", "Mobility"], "troop_type": "cavalry",
         "skills": [{"slot": 2, "name": "The Qingzhou Army", "type": "passive", "effect": "Increases damage to barbarians by 50%"}],
         "talent_builds": [{"purpose": "barbarians", "trees": ["Cavalry", "Peacekeeping"], "key_talents": ["Insight"]}],
         "pairings": [{"partner": "Boudica", "this_as": "primary", "purpose": "barbarian forts", "note": ""}],
         "ratings": [{"source_url": "x", "open_field": "A", "garrison": "D", "rally": "C"}], "sources": _src()},
        {"name": "Boudica", "rarity": "Epic", "specialties": ["Integration", "Peacekeeping", "Skill"], "troop_type": "integration",
         "skills": [{"slot": 2, "name": "Group Battle", "type": "passive", "effect": "Increases damage to barbarians by 25%"}],
         "talent_builds": [{"purpose": "barbarians", "trees": ["Peacekeeping", "Skill"], "key_talents": ["Feral Nature"]}],
         "pairings": [], "ratings": [], "sources": _src()},
        {"name": "Constance", "rarity": "Elite", "specialties": ["Integration", "Gathering", "Skill"], "troop_type": "integration",
         "skills": [{"slot": 2, "name": "The Regent", "type": "passive", "effect": "Increases wood gathering speed by 20%"}],
         "talent_builds": [{"purpose": "gathering", "trees": ["Gathering"], "key_talents": ["Superior Tools"]}],
         "pairings": [{"partner": "Sarka", "this_as": "primary", "purpose": "gathering", "note": ""}], "ratings": [], "sources": _src()},
        {"name": "Šárka", "aliases": ["Sarka"], "rarity": "Elite", "specialties": ["Integration", "Gathering", "Skill"], "troop_type": "integration",
         "skills": [{"slot": 2, "name": "The Maidens' War", "type": "passive", "effect": "gathering speed 18%"}],
         "talent_builds": [], "pairings": [], "ratings": [], "sources": _src()},
    ]
    d = tmp_path / "data"
    d.mkdir()
    (d / "commanders.json").write_text(json.dumps({"commanders": cmds}), encoding="utf-8")
    (d / "armamenti.json").write_text(json.dumps({"formations": [{"name": "Wedge", "bonus": "+5% skill damage"}, {"name": "Line", "bonus": "+10% gathering"}],
                                                  "rare_materials": [{"name": "Sage's Testimony"}]}), encoding="utf-8")
    return KnowledgeBase(d)


@pytest.fixture()
def profile():
    return json.loads((ROOT / "military_advisor" / "account_profile.example.json").read_text(encoding="utf-8"))


def test_normalize():
    assert normalize_name("Yi Seong-Gye (Prime)") == "yi seong gye prime"
    assert normalize_name("Šárka") == "sarka"


def test_find_alias(kb):
    assert kb.find("Sarka")["name"] == "Šárka"
    assert kb.find("sun tzu")["name"] == "Sun Tzu"


def test_recommend_roles(kb, profile):
    adv = MilitaryAdvisor(kb)
    res = adv.recommend(profile)
    roles = res["roles"]
    assert roles["gathering"]["pair"]["primary"] in ("Constance", "Šárka")
    assert roles["gathering"]["troops"]["troop_type"] == "siege" and roles["gathering"]["troops"]["tier"] == 1
    assert roles["barbarians"]["pair"]["primary"] == "Cao Cao"
    assert roles["barbarians"]["pair"]["secondary"] == "Boudica"
    assert roles["barbarians"]["pair"]["documented"] is True
    assert roles["defense"]["pair"]["primary"] in ("Richard I", "Sun Tzu")
    assert roles["attack"]["troops"]["tier"] == 4
    assert res["constraints"]["no_gems"] is True
    plan = res["training_plan"]
    assert all(o["no_gems"] for o in plan["orders"])
    assert any(o["troop_type"] == "siege" and o["tier"] == 1 for o in plan["orders"])
    report = adv.render_report(res)
    assert "RACCOLTA" in report and "PIANO DI ADDESTRAMENTO" in report


def test_gate(kb):
    adv = MilitaryAdvisor(kb)
    assert adv.gate({"kind": "train", "consumes": ["food"]}) == {"allowed": True, "requires_confirmation": False, "reason": "ok"}
    assert adv.gate({"kind": "attack", "target": "player"})["requires_confirmation"] is True
    assert adv.gate({"kind": "attack", "target": "barbarian"})["requires_confirmation"] is False
    assert adv.gate({"kind": "transmute", "consumes": ["Transmutation Stone"]})["requires_confirmation"] is True
    assert adv.gate({"kind": "craft", "consumes": ["Sage's Testimony"]})["requires_confirmation"] is True
    assert adv.gate({"kind": "buy", "spends_gems": True})["allowed"] is False


def test_validate_profile(profile):
    assert validate_profile(profile) == []
    bad = dict(profile); bad["commanders"] = [{"name": "X", "skills": [9, 1, 1, 1]}]
    assert validate_profile(bad)


def test_strategy_book_pairs(tmp_path, kb, profile):
    from military_advisor.strategies import StrategyBook
    d = kb.data_dir
    (d / "strategia_difesa.json").write_text(json.dumps({
        "garrison_pairs": [{"primary": "Richard I", "secondary": "Sun Tzu", "troop_type": "infantry", "budget": "f2p",
                            "why": "tank + AOE", "formation": "Tercio", "sources": _src()}],
        "bot_rules": [{"id": "def-1", "when": "rally in arrivo", "then": "scudo", "requires_confirmation": False, "sources": _src()}],
    }), encoding="utf-8")
    (d / "strategia_routine.json").write_text(json.dumps({
        "daily_checklist": [{"order": 2, "task": "alliance help", "reset": "00:00 UTC", "bot_rule": "premi aiuta", "requires_confirmation": False, "sources": _src()},
                            {"order": 1, "task": "tavern", "reset": "00:00 UTC", "bot_rule": "apri forzieri", "requires_confirmation": False, "sources": _src()}]
    }), encoding="utf-8")
    sb = StrategyBook(d)
    assert [i["order"] for i in sb.daily_checklist()] == [1, 2]
    assert len(sb.bot_rules()) == 3
    adv = MilitaryAdvisor(kb, strategies=sb)
    res = adv.recommend(profile)
    pair = res["roles"]["defense"]["pair"]
    assert pair["primary"] == "Richard I" and pair["secondary"] == "Sun Tzu" and pair["documented"]
    assert res["roles"]["defense"]["formation"]["name"] == "Tercio"
    assert len(res["bot_rules"]) == 3
    assert "ROUTINE GIORNALIERA" in adv.render_report(res)


def test_prime_not_confused(tmp_path):
    d = tmp_path / "d"; d.mkdir()
    (d / "commanders.json").write_text(json.dumps({"commanders": [
        {"name": "Sun Tzu Prime", "rarity": "Legendary", "specialties": ["Infantry"], "sources": []}]}), encoding="utf-8")
    kb = KnowledgeBase(d)
    assert kb.find("Sun Tzu") is None          # l'Epic non deve diventare il Prime
    assert kb.find("sun tzu prime")["name"] == "Sun Tzu Prime"


def test_prime_alias_not_confused(tmp_path):
    d = tmp_path / "d"; d.mkdir()
    (d / "commanders.json").write_text(json.dumps({"commanders": [
        {"name": "Boudica Prime", "aliases": ["Legendary Boudica"], "sources": []}]}), encoding="utf-8")
    assert KnowledgeBase(d).find("Boudica") is None


def test_same_name_two_rarities(tmp_path):
    d = tmp_path / "d"; d.mkdir()
    (d / "commanders.json").write_text(json.dumps({"commanders": [
        {"name": "Pelagius", "rarity": "Legendary", "sources": []},
        {"name": "Pelagius", "rarity": "Epic", "sources": []}]}), encoding="utf-8")
    kb = KnowledgeBase(d)
    assert kb.find("Pelagius", "Epic")["rarity"] == "Epic"
    assert kb.find("pelagius", "legendary")["rarity"] == "Legendary"


def test_formation_names(tmp_path):
    d = tmp_path / "d"; d.mkdir()
    (d / "armamenti.json").write_text(json.dumps({"formations": [
        {"name": "Wedge Formation"}, {"name": "Wedge Formation II"}, {"name": "Line Formation"}]}), encoding="utf-8")
    kb = KnowledgeBase(d)
    assert kb.formation_by_name("Wedge")["name"] == "Wedge Formation"
    assert kb.formation_by_name("Wedge II")["name"] == "Wedge Formation II"
    assert kb.formation_by_name("line formation")["name"] == "Line Formation"


def test_talents_fallback_checks_trees(tmp_path):
    from military_advisor.strategies import StrategyBook
    d = tmp_path / "d"; d.mkdir()
    (d / "commanders.json").write_text(json.dumps({"commanders": [
        {"name": "Tank", "specialties": ["Infantry", "Garrison", "Defense"], "talent_builds": [
            {"purpose": "open_field", "trees": ["Infantry"], "key_talents": ["X"]}], "sources": []}]}), encoding="utf-8")
    (d / "talenti.json").write_text(json.dumps({"role_builds": [
        {"role": "garrison", "trees": ["Garrison", "Skill", "Infantry"],
         "talents_in_order": [{"name": "Impregnable", "points": 3}], "sources": []}]}), encoding="utf-8")
    kb = KnowledgeBase(d)
    adv = MilitaryAdvisor(kb, strategies=StrategyBook(d))
    tb = adv.talents_for("defense", kb.find("Tank"))
    assert tb["_origin"].startswith("build standard")
    assert tb["usable_trees"] == ["Garrison", "Infantry"]
    assert "Skill" in tb["notes"]
    # per l'attacco la guida del comandante ha la sua build: vince quella
    assert adv.talents_for("attack", kb.find("Tank"))["_origin"].startswith("build del comandante")


def test_gate_hard_stops(kb):
    adv = MilitaryAdvisor(kb)
    v = adv.gate({"kind": "captcha"})
    assert v["allowed"] is False and v["stop_bot"] is True
    assert adv.gate({"kind": "tap", "verification_window": True})["stop_bot"] is True
    assert adv.gate({"kind": "delete_account"})["allowed"] is False
    assert adv.gate({"kind": "travel", "consumes": ["Gems"]})["allowed"] is False


def test_tier_parsing():
    from military_advisor.kb import tier_to_score as t
    assert t("A") == 7.0 and t("Tier A") == 7.0 and t("A-tier") == 7.0
    assert t("B (colonna Defense)") == 5.0
    assert t("4/5 stelle") == 8.0 and abs(t("4.4/5 (11 voti)") - 8.8) < 1e-9 and t("5 stelle") == 10.0
    assert t("KvK1 A / KvK2 A / SoC B") == (7 + 7 + 5) / 3
    assert t("Z") > t("S+")
    assert t("1/5 (placeholder non valutato)") is None and t("5 stelle (ironico)") is None
    assert t("no") is None and t("pessimo") is None


def test_no_shields_policy(kb):
    from military_advisor.strategies import apply_user_policy
    adv = MilitaryAdvisor(kb)
    assert adv.gate({"kind": "activate_shield"})["allowed"] is False
    assert adv.gate({"kind": "use_item", "consumes": ["Peace Shield 8h"]})["allowed"] is False
    r = apply_user_policy({"id": "x", "when": "rally", "then": "Attivare il Peace Shield posseduto, poi notificare l'utente."})
    assert r["then"].startswith("MAI attivare scudi") and r["user_policy"] == "never_activate_shield"
    keep = apply_user_policy({"id": "y", "then": "Non consumare scudi o teletrasporti: verificare il garrison plan."})
    assert "user_policy" not in keep
