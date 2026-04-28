from pathlib import Path

from doctrineos.runtime import DoctrineOSRuntime
from doctrineos.shell import main


def test_doctrineos_boot_status(tmp_path):
    runtime = DoctrineOSRuntime(state_dir=str(tmp_path / "state"))
    status = runtime.boot_status()
    assert status["system"] == "DoctrineOS"
    assert status["mount"] == "verified"
    assert status["user_authority"] == "root"
    assert status["context_sha256"]


def test_doctrineos_uses_default_profile(tmp_path):
    runtime = DoctrineOSRuntime(state_dir=str(tmp_path / "state"))
    status = runtime.boot_status()
    assert status["profile"] == "doctrineos_default_profile_v1"
    assert status["profile_path"] == "profiles/default.doctrine"


def test_doctrineos_refuses_unapproved_permissioned_action(tmp_path):
    state_dir = tmp_path / "state"
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(state_dir))
    output = runtime.execute("inspect workspace", approved=False)
    assert output["allowed"] is False
    assert "refused" in output["result"]
    assert output["receipt"]["allowed"] is False


def test_doctrineos_refused_action_writes_receipt_and_state(tmp_path):
    state_dir = tmp_path / "state"
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(state_dir))
    output = runtime.execute("inspect workspace", approved=False)

    receipt_path = Path(output["receipt_path"])
    state_path = state_dir / "state.json"

    assert receipt_path.exists()
    assert state_path.exists()
    assert "refused" in receipt_path.read_text(encoding="utf-8")
    assert "inspect workspace" in state_path.read_text(encoding="utf-8")


def test_doctrineos_executes_approved_stub_action(tmp_path):
    (tmp_path / "example.txt").write_text("hello", encoding="utf-8")
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(tmp_path / "state"))
    output = runtime.execute("inspect workspace", approved=True)
    assert output["allowed"] is True
    assert "example.txt" in output["result"]
    assert output["receipt"]["capability"] == "files.read"


def test_doctrineos_approved_action_writes_receipt_and_state(tmp_path):
    (tmp_path / "example.txt").write_text("hello", encoding="utf-8")
    state_dir = tmp_path / "state"
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(state_dir))
    output = runtime.execute("inspect workspace", approved=True)

    receipt_path = Path(output["receipt_path"])
    state_path = state_dir / "state.json"

    assert receipt_path.exists()
    assert state_path.exists()
    assert "example.txt" in receipt_path.read_text(encoding="utf-8")
    assert "inspect workspace" in state_path.read_text(encoding="utf-8")


def test_doctrineos_cli_json_boot(capsys):
    result = main(["--json"])
    captured = capsys.readouterr()
    assert result == 0
    assert "DoctrineOS" in captured.out
