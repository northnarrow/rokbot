import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from military_advisor import adb_tools as a  # noqa: E402


def test_parse_devices():
    out = "List of devices attached\nR5CT12345\tdevice\nemulator-5554\tunauthorized\n\n"
    assert a.parse_devices(out) == [("R5CT12345", "device"), ("emulator-5554", "unauthorized")]


def test_parse_wm_size_prefers_override():
    assert a.parse_wm_size("Physical size: 1080x2400\n") == (1080, 2400)
    assert a.parse_wm_size("Physical size: 1440x3200\nOverride size: 1080x2400\n") == (1080, 2400)
    assert a.parse_wm_size("garbage") is None


def test_parse_density():
    assert a.parse_density("Physical density: 420\nOverride density: 480") == 480


def test_parse_focus():
    w = "  mCurrentFocus=Window{a1b2c3 u0 com.lilithgame.roc.gp/com.harry.engine.MainActivity}"
    assert a.parse_focus(w) == "com.lilithgame.roc.gp"
    act = "    mResumedActivity: ActivityRecord{77 u0 com.android.launcher3/.Launcher t12}"
    assert a.parse_focus(act) == "com.android.launcher3"


def test_parse_packages():
    assert a.parse_packages("package:com.a\npackage:com.lilithgame.roc.gp\n") == ["com.a", "com.lilithgame.roc.gp"]


def test_png_size(tmp_path):
    import struct, zlib
    raw = b"\x00\x00\x00\x00"
    png = (b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + struct.pack(">IIBBBBB", 3, 2, 8, 2, 0, 0, 0)
           + struct.pack(">I", zlib.crc32(b"IHDR")) + b"\x00" * 8)
    p = tmp_path / "x.png"; p.write_bytes(png)
    assert a.png_size(p) == (3, 2)


def test_report_without_adb(monkeypatch, tmp_path):
    monkeypatch.setenv("ADB_PATH", "")
    monkeypatch.setattr(a.shutil, "which", lambda _: None)
    rep = a.phone_report(tmp_path)
    assert rep["steps"][0]["ok"] is False and "adb non trovato" in rep["steps"][0]["error"]
