from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from sdk.cli import cmd_doctor, cmd_inspect
from sdk.doctrine import Doctrine
from sdk.filetype import DoctrineFiletypeParser


ROOT = Path(__file__).resolve().parents[1]


class Args:
    def __init__(self, path: str, format: str = "json"):
        self.path = path
        self.format = format


def capture_stdout(fn, args):
    buffer = StringIO()
    with redirect_stdout(buffer):
        rc = fn(args)
    return rc, buffer.getvalue()


def assert_no_private_project_terms(text: str):
    forbidden = ["Xxen", ".soul", ".sol", "kernel", "private material", "private_", "proto-soul", "proto-.soul"]
    lowered = text.lower()
    for term in forbidden:
        assert term.lower() not in lowered, term


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


def test_doctor_markdown_valid_fixture_is_readable():
    rc, out = capture_stdout(cmd_doctor, Args(str(ROOT / "examples" / "basic.doctrine"), "markdown"))
    assert rc == 0
    assert "# DoctrineOS Doctor Report" in out
    assert "PASS" in out
    assert "WARN" in out
    assert "## Proof boundaries" in out
    assert "What this proves" in out
    assert "What this does not prove" in out
    assert "implementation-specific extension" in out
    assert_no_private_project_terms(out)


def test_inspect_markdown_valid_fixture_is_readable():
    rc, out = capture_stdout(cmd_inspect, Args(str(ROOT / "examples" / "basic.doctrine"), "markdown"))
    assert rc == 0
    assert "# DoctrineOS Inspect Report" in out
    assert "PASS" in out
    assert "PUBLIC_PROFILE_JSON" in out
    assert "## Next safe actions" in out
    assert_no_private_project_terms(out)


def test_doctor_markdown_malformed_sentinel_reports_fail():
    with TemporaryDirectory() as tmp:
        bad = Path(tmp) / "bad.doctrine"
        bad.write_text("""DOCTRINE FILE
version: 1.0.0
body_id: bad_public_fixture

# Bad Public Fixture

## Definition
A deliberately malformed public fixture.

<<<PUBLIC_PROFILE_JSON>>>
{"status":"ACTIVE",,}
<<<END_PUBLIC_PROFILE_JSON>>>
""", encoding="utf-8")
        rc, out = capture_stdout(cmd_doctor, Args(str(bad), "markdown"))
    assert rc == 1
    assert "FAIL" in out
    assert "json_parse_failed" in out
    assert "sentinel_diagnostics" in out
    assert "Repair the listed FAIL diagnostics" in out
    assert_no_private_project_terms(out)
