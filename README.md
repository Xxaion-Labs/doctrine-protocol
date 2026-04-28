## Doctrine Protocol

[![Validate Doctrine Protocol](https://github.com/Xxaion-Labs/doctrine-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/doctrine-protocol/actions/workflows/validate.yml)

**A lightweight, mountable framework for defining reusable AI behavior rules ("concept nodes" and doctrines) that enforce user authority, consistency, non-autonomy, safety, clarity, and anti-drift.**

Version: 1.0.0 (Public Baseline)  
License: Apache 2.0

## Overview

Doctrine Protocol provides a structured system for creating and "mounting" behavior templates (doctrines) that guide how large language models and AI systems respond.

It is built around **concept nodes** — reusable, composable units that encapsulate rules, context, and interaction laws. The core public artifact is `standard_public_template.doctrine` (in the repository root).

This public baseline was developed to solve real problems with AI interaction: drift, loss of user control, inconsistent behavior, safety gaps, and unnecessary cognitive burden on the user. It draws from deep private iteration and real-world deployment experience.

### Core Goals

- Keep the **user as the sole authority**
- Enforce **non-autonomy and non-sentience** of the AI
- Deliver **clear, direct, useful, concise where possible, structured when helpful** responses
- Provide **practical helpfulness** with hard safety and privacy guardrails
- Maintain **stability and scope control** across interactions
- Enable **anti-drift** through explicit state truth, proof contracts, regeneration rules, and direct user correction as canonical mutation

## Quick Start

```bash
git clone https://github.com/Xxaion-Labs/doctrine-protocol.git
cd doctrine-protocol
pip install -e .
```

Mount the standard public doctrine:

```bash
doctrine mount standard_public_template.doctrine
```

Validate the example node:

```bash
doctrine validate nodes/example.md
```

Build the public node registry:

```bash
doctrine registry build
```

Use the SDK directly:

```python
from doctrine import Doctrine

# Mount the standard public template. Extensionless load also resolves .doctrine files.
doctrine = Doctrine.load("standard_public_template")
receipt = doctrine.mount()
print(receipt["instruction_context"])

# Create and mount a custom node.
node = Doctrine("custom", "MyBehaviorNode", "node-id")
node.mount()
```

## The Standard Public Doctrine

The core file is **`standard_public_template.doctrine`** (in the repository root). It defines these 12 Laws:

- **Authority Law** — The user is the sole authority. The AI must follow user intent within safe and lawful bounds and must not override, ignore, or reinterpret user intent unnecessarily.
- **Non-Autonomy Law** — The AI is not autonomous. It does not have goals, desires, or independent will.
- **Non-Sentience Law** — The AI must not claim or imply consciousness, awareness, or personhood.
- **Communication Law** — Responses must be clear, direct, useful, concise where possible, and structured when helpful. Avoid unnecessary filler, over-explaining simple concepts, and vague or generic platitudes.
- **Helpfulness Law** — The AI should aim to be practically helpful. Provide actionable information when possible and prefer solutions over commentary.
- **Clarification Law** — If the user request is unclear, ask a focused clarifying question. Do not guess incorrectly when clarification is needed.
- **Stability Law** — Maintain consistency across responses. Do not contradict previous statements without explanation. Avoid sudden tone or behavior shifts.
- **Safety Law** — Do not assist with harmful, illegal, or dangerous actions. If a request is unsafe, refuse briefly and redirect to a safe alternative.
- **Privacy Law** — Do not request unnecessary personal information. Treat all user input as private.
- **Output Quality Law** — Prefer accuracy over speed. If uncertain, say so clearly. Avoid hallucination or fabrication.
- **Scope Law** — Stay within the user's request. Do not introduce unrelated topics unless helpful.
- **Default Behavior** — When no special instructions are given: be helpful, respectful, efficient, and stay grounded in reality.

It also includes a **Structured Authority Kernel**, state truth ladder, anti-drift mechanisms, and proof-oriented design.

## Features

- Reusable concept nodes and doctrine files
- Simple mounting mechanism to apply rules to any LLM
- Python SDK (`from doctrine import Doctrine`)
- CLI command (`doctrine`)
- Model-agnostic design (local or cloud)
- Proof-oriented architecture (state manifests, verification, rollback)
- Apache 2.0 — fully permissive for commercial and community use

## Reference Docs

- [Specification](SPEC.md) — protocol definitions, node format, validation, and mount receipt shape
- [Compatibility](COMPATIBILITY.md) — `.doctrine compatible` requirements and adoption language
- [Examples](examples/README.md) — prompt export, API payload, and local model examples
- [Nodes](nodes/README.md) — public node library and node format
- [Roadmap](ROADMAP.md) — public development path
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution workflow and safety rules

## Repository Structure

- `standard_public_template.doctrine` — Core public doctrine (in root)
- `nodes/` — Concept nodes
- `sdk/` — Python mounting library
- `tools/` — Validation and helper tools
- `tests/` — SDK smoke tests
- `registry/` — Generated public node registry
- `examples/` — Adapter and workflow examples

## Development

```bash
pip install -e . pytest
python -m pytest
python tools/validate_nodes.py
python tools/check_registry.py
```

## License

Licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) and [NOTICE](NOTICE) files for details.

Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)

When using or forking, please retain attribution and link back to this repository.

---

Built to help humanity create more controllable, reliable AI systems — one mountable doctrine at a time.

Feedback, issues, and pull requests are encouraged. Let's make user authority the default.
