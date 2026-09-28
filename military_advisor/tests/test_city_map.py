import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from military_advisor.city_map import CityMap, canonical_building, MAX_FAILURES  # noqa: E402


def test_italian_and_english_names():
    assert canonical_building("Mercato") == "Trading Post"
    assert canonical_building("Mercato Lv.12") == "Trading Post"
    assert canonical_building("TRADING POST") == "Trading Post"
    assert canonical_building("Miniera d'oro Lv 5") == "Goldmine"
    assert canonical_building("qualcosa di strano") is None


def test_learn_is_relative_and_survives_resolution_change(tmp_path):
    m = CityMap()
    s = m.learn("Mercato", 960, 540, (1920, 1080))
    assert (s.x, s.y) == (0.5, 0.5)
    p = tmp_path / "city.json"
    m.save(p)
    m2 = CityMap.load(p)
    assert m2.to_pixels(m2.find("Trading Post"), (2400, 1080)) == (1200, 540)


def test_moved_building_triggers_relearn_then_stop():
    m = CityMap()
    m.learn("Taverna", 100, 100, (1000, 1000))
    assert m.verify("Tavern", "Taverna Lv 10")["action"] == "proceed"
    for i in range(1, MAX_FAILURES):
        assert m.verify("Tavern", "Ospedale")["action"] == "relearn"
    assert m.verify("Tavern", "Ospedale")["action"] == "stop_and_notify"
    m.learn("Taverna", 300, 400, (1000, 1000))  # ritrovata in una nuova posizione
    assert m.find("Tavern").failures == 0 and m.verify("Tavern", "Taverna")["ok"]


def test_unknown_building_needs_learning():
    assert CityMap().verify("Academy", "Accademia")["action"] == "relearn"
