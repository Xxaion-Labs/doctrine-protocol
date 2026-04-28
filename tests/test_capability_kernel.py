from doctrineos.capability_kernel import (
    Capability,
    CapabilityKernel,
    MODE_ALLOW,
    MODE_ASK,
    MODE_OFF,
    RISK_LOW,
)


def test_allow_mode_allows_without_permission():
    kernel = CapabilityKernel(policy_modes={"state.read": MODE_ALLOW})
    decision = kernel.evaluate("state.read")
    assert decision.allowed is True
    assert decision.requires_permission is False
    assert decision.reason == "allowed by policy"


def test_ask_mode_requires_approval():
    kernel = CapabilityKernel(policy_modes={"files.read": MODE_ASK})
    denied = kernel.evaluate("files.read", approved=False)
    approved = kernel.evaluate("files.read", approved=True)
    assert denied.allowed is False
    assert denied.requires_permission is True
    assert denied.reason == "permission required"
    assert approved.allowed is True
    assert approved.reason == "approved by user"


def test_off_mode_blocks_even_when_approved():
    kernel = CapabilityKernel(policy_modes={"network.access": MODE_OFF})
    decision = kernel.evaluate("network.access", approved=True)
    assert decision.allowed is False
    assert decision.requires_permission is False
    assert decision.reason == "blocked by policy"


def test_unknown_capability_defaults_to_ask_high_risk():
    kernel = CapabilityKernel()
    capability = kernel.get("unknown.power")
    decision = kernel.evaluate("unknown.power", approved=False)
    assert capability.name == "unknown.power"
    assert capability.default_mode == MODE_ASK
    assert capability.risk_level == "high"
    assert decision.allowed is False


def test_custom_capability_can_be_registered():
    kernel = CapabilityKernel(
        capabilities={
            "custom.safe": Capability(
                name="custom.safe",
                description="Custom low-risk test capability.",
                risk_level=RISK_LOW,
                default_mode=MODE_ALLOW,
                requires_receipt=True,
                adapter_binding="custom.safe",
            )
        }
    )
    decision = kernel.evaluate("custom.safe")
    assert decision.allowed is True
    assert decision.capability.adapter_binding == "custom.safe"


def test_describe_exposes_policy_modes():
    kernel = CapabilityKernel(policy_modes={"network.access": MODE_OFF})
    described = kernel.describe()
    assert described["network.access"]["mode"] == MODE_OFF
    assert described["network.access"]["risk_level"] == "high"
