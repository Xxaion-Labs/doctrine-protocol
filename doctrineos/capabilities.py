from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class CapabilityRequest:
    name: str
    description: str
    requires_permission: bool = True


DEFAULT_CAPABILITIES: Dict[str, CapabilityRequest] = {
    "files.read": CapabilityRequest(
        name="files.read",
        description="Read workspace files or directories.",
        requires_permission=True,
    ),
    "shell.run": CapabilityRequest(
        name="shell.run",
        description="Run a shell command.",
        requires_permission=True,
    ),
    "network.access": CapabilityRequest(
        name="network.access",
        description="Access network resources.",
        requires_permission=True,
    ),
}


def get_capability(name: str) -> CapabilityRequest:
    return DEFAULT_CAPABILITIES.get(
        name,
        CapabilityRequest(name=name, description="Unknown capability.", requires_permission=True),
    )
