import json
from pathlib import Path
from typing import Any, Dict, Optional

from .adapters import StubAdapter
from .capabilities import get_capability
from .profile import DoctrineOSProfile
from .receipts import build_action_receipt, write_receipt
from .state import StateStore


class DoctrineOSRuntime:
    def __init__(
        self,
        profile_path: str = "standard_public_template.doctrine",
        workspace: str = ".",
        state_dir: str = ".doctrineos",
    ):
        self.profile = DoctrineOSProfile(profile_path)
        self.workspace = Path(workspace)
        self.state_dir = Path(state_dir)
        self.receipts_dir = self.state_dir / "receipts"
        self.state = StateStore(self.state_dir / "state.json")
        self.adapter = StubAdapter()

    def boot_status(self) -> Dict[str, Any]:
        return {
            "system": "DoctrineOS",
            "profile": self.profile.name,
            "mount": "verified",
            "context_sha256": self.profile.context_sha256,
            "user_authority": "root",
            "capabilities": {
                "files.read": "ask",
                "shell.run": "ask",
                "network.access": "off",
                "model": "stub",
            },
        }

    def plan(self, command: str) -> Dict[str, Any]:
        normalized = command.strip().lower()
        if normalized in {"state", "show state", "status"}:
            return {"intent": "show_state", "capability": "state.read", "requires_permission": False}
        if normalized.startswith("inspect"):
            cap = get_capability("files.read")
            return {"intent": "inspect_workspace", "capability": cap.name, "requires_permission": cap.requires_permission}
        return {"intent": "echo", "capability": "none", "requires_permission": False}

    def execute(self, command: str, approved: Optional[bool] = None) -> Dict[str, Any]:
        plan = self.plan(command)
        requires_permission = bool(plan["requires_permission"])
        allowed = bool(approved) if requires_permission else True

        if requires_permission and not allowed:
            result = "refused: permission not granted"
        elif plan["intent"] == "inspect_workspace":
            result = json.dumps(self.adapter.inspect_workspace(self.workspace), indent=2)
        elif plan["intent"] == "show_state":
            result = json.dumps(self.state.snapshot(), indent=2)
        else:
            result = json.dumps(self.adapter.echo(command), indent=2)

        receipt = build_action_receipt(
            command=command,
            intent=str(plan["intent"]),
            capability=str(plan["capability"]),
            allowed=allowed,
            result=result,
            doctrine_receipt=self.profile.receipt,
        )
        receipt_path = write_receipt(receipt, self.receipts_dir)
        self.state.record_action(str(receipt_path), command, allowed)

        return {
            "plan": plan,
            "allowed": allowed,
            "result": result,
            "receipt_path": str(receipt_path),
            "receipt": receipt,
        }
