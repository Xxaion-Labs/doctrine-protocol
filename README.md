## Doctrine Protocol

[![Validate Doctrine Protocol](https://github.com/Xxaion-Labs/doctrine-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/doctrine-protocol/actions/workflows/validate.yml)

**A lightweight, mountable framework for reusable AI behavior rules, concept nodes, doctrine files, mount receipts, validation, and anti-drift control.**

Version: 1.0.0 (Public Baseline)  
License: AGPLv3-or-later

## Overview

Doctrine Protocol provides a structured system for creating and mounting behavior templates that guide how AI systems respond.

It is built around **concept nodes**: reusable units that encode rules, context, and interaction patterns. The core public artifact is `standard_public_template.doctrine` in the repository root.

## DoctrineOS Direction

Doctrine Protocol is the control substrate for DoctrineOS: a public, doctrine-native AI operating system direction.

DoctrineOS aims to become a real user-controlled computing environment where AI is part of the operating system itself and doctrine supplies the behavioral control layer.

Start here:

- [DoctrineOS Direction](DOCTRINE_OS.md)
- [DoctrineOS Architecture Seed](DOCTRINE_OS_ARCHITECTURE.md)
- [DoctrineOS Roadmap](docs/doctrineos_roadmap.md)
- [DoctrineOS Prototype Shell](docs/doctrineos_shell.md)

## Core Goals

- Keep the user as the root authority.
- Keep AI systems non-autonomous and non-sentient.
- Make AI behavior clearer, steadier, and easier to inspect.
- Support practical helpfulness with privacy and safety boundaries.
- Reduce drift through explicit doctrine, validation, receipts, and correction loops.

## License Position

Doctrine Protocol is licensed under **AGPLv3-or-later** so the public project and modified public versions stay under the same open license family.

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

Run the DoctrineOS prototype shell:

```bash
doctrineos --json
doctrineos inspect workspace
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

doctrine = Doctrine.load("standard_public_template")
receipt = doctrine.mount()
print(receipt["instruction_context"])
```

## Features

- Reusable concept nodes and doctrine files
- Simple mounting mechanism to apply doctrine context
- Python SDK (`from doctrine import Doctrine`)
- CLI command (`doctrine`)
- DoctrineOS prototype shell command (`doctrineos`)
- Model-agnostic design
- Mount receipts with context hashes
- Registry and validation tooling
- AGPLv3-or-later licensing

## Reference Docs

- [Specification](SPEC.md) — protocol definitions, node format, validation, and mount receipt shape
- [Compatibility](COMPATIBILITY.md) — `.doctrine compatible` requirements and adoption language
- [Examples](examples/README.md) — prompt export, API payload, and local model examples
- [Nodes](nodes/README.md) — public node library and node format
- [Roadmap](ROADMAP.md) — public development path
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution workflow and safety rules

## Repository Structure

- `standard_public_template.doctrine` — core public doctrine template
- `profiles/` — DoctrineOS profile examples
- `nodes/` — concept nodes
- `sdk/` — Python mounting library
- `doctrineos/` — DoctrineOS prototype shell and runtime
- `tools/` — validation and helper tools
- `tests/` — SDK, example, and DoctrineOS tests
- `registry/` — generated public node registry
- `examples/` — adapter and workflow examples
- `docs/` — DoctrineOS and project docs

## Development

```bash
pip install -e . pytest
python -m pytest
python tools/validate_nodes.py
python tools/check_registry.py
```

## License

Licensed under the GNU Affero General Public License v3.0 or later. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)

When using or forking, please retain attribution and link back to this repository.
