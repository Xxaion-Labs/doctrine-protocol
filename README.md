# DoctrineOS

[![Validate DoctrineOS](https://github.com/Xxaion-Labs/DoctrineOS/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/DoctrineOS/actions/workflows/validate.yml)

**DoctrineOS is an AGPL operating system prototype for the post-app age of AI: sovereign computing where intelligence is native, doctrine governs the machine, and the user remains the root of power.**

Version: 0.1.0 Prototype  
License: AGPLv3-or-later

## What this is

DoctrineOS is a public, doctrine-native AI operating system prototype.

It is not a chatbot, wrapper, plugin, desktop assistant, or agent demo. It is the beginning of a user-governed computing environment where AI is part of the operating layer itself and Doctrine Protocol supplies the behavioral control substrate.

## What it unlocks

DoctrineOS moves AI from an app-shaped box into a governed operating surface:

- the user remains root authority
- doctrine profiles define operating behavior
- actions are capability-scoped
- permissioned actions emit receipts
- runtime state stays inspectable
- adapters connect models, files, tools, apps, and services
- public code remains open under AGPLv3-or-later

## Current status

DoctrineOS currently includes:

- Doctrine Protocol SDK and CLI
- `.doctrine` file loading, parsing, validation, and mounting
- mount receipts with context hashes
- public concept nodes and generated node registry
- adapter examples
- DoctrineOS prototype shell
- default DoctrineOS profile
- action receipts and runtime state logging
- GitHub Actions validation

## DoctrineOS prototype shell

The `doctrineos` command is the first runnable DoctrineOS control surface.

It loads a doctrine profile, mounts it, plans command intent, identifies needed capabilities, asks for permission where required, routes approved commands to safe adapters, writes action receipts, and records runtime state.

```bash
doctrineos --json
doctrineos inspect workspace
doctrineos --yes inspect workspace
```

Runtime state and receipts are written under `.doctrineos/` by default.

## Quick start

```bash
git clone https://github.com/Xxaion-Labs/DoctrineOS.git
cd DoctrineOS
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

## Project map

- [Vision](VISION.md) — why DoctrineOS exists
- [Architecture](ARCHITECTURE.md) — system layers and control spine
- [Roadmap](ROADMAP.md) — build path from prototype to public OS environment
- [Prototype Shell](docs/prototype-shell.md) — runnable shell guide
- [Doctrine Protocol Specification](SPEC.md) — `.doctrine` format and mount receipts
- [Compatibility](COMPATIBILITY.md) — `.doctrine compatible` requirements
- [Examples](examples/README.md) — adapter and workflow examples
- [Nodes](nodes/README.md) — public concept node library
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution guide

## Repository structure

- `standard_public_template.doctrine` — core public doctrine template
- `profiles/` — DoctrineOS profile examples
- `doctrineos/` — DoctrineOS prototype shell and runtime
- `sdk/` — Doctrine Protocol Python SDK
- `nodes/` — public concept nodes
- `registry/` — generated public node registry
- `examples/` — adapter and workflow examples
- `tools/` — validation and helper tools
- `tests/` — SDK, example, and DoctrineOS tests
- `docs/` — additional DoctrineOS docs

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
