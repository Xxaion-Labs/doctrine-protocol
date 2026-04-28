import json
from pathlib import Path
from typing import Any, Dict, Optional

from .adapters import StubAdapter
from .capability_kernel import CapabilityKernel
from .policy import DEFAULT_POLICY_MODES
from .profile import DoctrineOSProfile
from .receipts import build_action_receipt, write_receipt
from .state import StateStore


DEFAULT_PROFILE_PATH = "profiles/default.doctrine"


class DoctrineOSRuntime:
    def __init__(
        self,
        profile_path: str = DEFAULT_PROFILE_PATH,
        workspace: str = ".",
        state_dir: str = ".doctrineos",
        capability_kernel: Optional[CapabilityKernel] = None,
    ):
        self.profile = DoctrineOSProfile(profile_path)
        self.workspace = Path(workspace)
        self.state_dir = Path(state_dir)
        self.receipts_dir = self.state_dir / "receipts"
        self.state = StateStore(self.state_dir / "state.json")
        self.adapter = StubAdapter()
        self.capability_kernel = capability_kernel or CapabilityKernel(policy_modes=DEFAULT_POLICY_MODES)

    def boot_status(self) -> Dict[str, Any]:
        return {
            "system": "DoctrineOS",
            "profile": self.profile.name,
            "profile_path": str(self.profile.path),
            "mount": "verified",
            "context_sha256": self.profile.context_sha256,
            "user_authority": "root",
            "capabilities": self.capability_kernel.describe(),
        }

    def plan(self, command: str) -> Dict[str, Any]:
        normalized = command.strip().lower()
        if normalized in {"state", "show state", "status"}:
            capability_name = "state.read"
            capability = self.capability_kernel.get(capability_name)
            return {
                "intent": "show_state",
                "capability": capability.name,
                "risk_level": capability.risk_level,
                "mode": capability.default_mode,
                "requires_permission": capability.requires_permission,
            }
        if normalized.startswith("inspect"):
            capability_name = "files.read"
            capability = self.capability_kernel.get(capability_name)
            return {
                "intent": "inspect_workspace",
                "capability": capability.name,
                "risk_level": capability.risk_level,
                "mode": capability.default_mode,
                "requires_permission": capability.requires_permission,
            }
        capability_name = "none"
        capability = self.capability_kernel.get(capability_name)
        return {
            "intent": "echo",
            "capability": capability.name,
            "risk_level": capability.risk_level,
            "mode": capability.default_mode,
            "requires_permission": capability.requires_permission,
        }

    def execute(self, command: str, approved: Optional[bool] = None) -> Dict[str, Any]:
        plan = self.plan(command)
        decision = self.capability_kernel.evaluate(str(plan["capability"]), approved=approved)
        allowed = decision.allowed

        if not allowed:
            result = "refused: " + decision.reason
        elif plan["intent"] == "inspect_workspace":
            result = json.dumps(self.adapter.inspect_workspace(self.workspace), indent=2)
        elif plan["intent"] == "show_state":
            result = json.dumps(self.state.snapshot(), indent=2)
        else:
            result = json.dumps(self.adapter.echo(command), indent=2)

        receipt = build_action_receipt(
            command=command,
            intent=str(plan["intent"]),
            capability=decision.capability.name,
            allowed=allowed,
            result=result,
            doctrine_receipt=self.profile.receipt,
        )
        receipt["risk_level"] = decision.capability.risk_level
        receipt["policy_mode"] = decision.mode
        receipt["policy_reason"] = decision.reason
        receipt_path = write_receipt(receipt, self.receipts_dir)
        self.state.record_action(str(receipt_path), command, allowed)

        return {
            "plan": plan,
            "decision": {
                "capability": decision.capability.name,
                "mode": decision.mode,
                "allowed": decision.allowed,
                "requires_permission": decision.requires_permission,
                "requires_receipt": decision.requires_receipt,
                "reason": decision.reason,
            },
            "allowed": allowed,
            "result": result,
            "receipt_path": str(receipt_path),
            "receipt": receipt,
        }
