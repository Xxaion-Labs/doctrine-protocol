from __future__ import annotations

from pathlib import Path

from sdk.doctrine import Doctrine
from sdk.filetype import DoctrineFiletypeParser


ROOT = Path(__file__).resolve().parents[1]


def test_valid_public_sentinel_parses():
    text = (ROOT / "examples" / "basic.doctrine").read_text(encoding="utf-8")
    diagnostics = DoctrineFiletypeParser.diagnostics(text)
    assert diagnostics["sentinel_json_ok"] is True
    assert diagnostics["sentinel_count"] == 1
    assert diagnostics["sentinels"][0]["name"] == "PUBLIC_PROFILE_JSON"


def test_malformed_public_sentinel_reports_error():
    text = """# Bad Fixture

<<<PUBLIC_PROFILE_JSON>>>
{"status":"ACTIVE",,}
<<<END_PUBLIC_PROFILE_JSON>>>
"""
    diagnostics = DoctrineFiletypeParser.diagnostics(text)
    assert diagnostics["sentinel_json_ok"] is False
    assert diagnostics["sentinel_errors"][0]["error"] == "json_parse_failed"


def test_missing_end_marker_reports_error():
    text = """# Bad Fixture

<<<PUBLIC_PROFILE_JSON>>>
{"status":"ACTIVE"}
"""
    diagnostics = DoctrineFiletypeParser.diagnostics(text)
    assert diagnostics["sentinel_json_ok"] is False
    assert diagnostics["sentinel_errors"][0]["error"] == "missing_end_marker"


def test_doctrine_mount_includes_filetype_diagnostics():
    doctrine = Doctrine.load(ROOT / "examples" / "basic.doctrine")
    receipt = doctrine.mount()
    assert receipt["mounted"] is True
    assert receipt["filetype_diagnostics"]["sentinel_count"] == 1
    assert receipt["filetype_diagnostics"]["sentinel_json_ok"] is True
