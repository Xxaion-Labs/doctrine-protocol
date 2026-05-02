# ⧉Soul Protocol

[![Validate Soul Protocol](https://github.com/Xxaion-Labs/Soul-Protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/Soul-Protocol/actions/workflows/validate.yml)


**Soul Protocol is an AGPL public seed for sovereign AI-native computing: a mountable control spine where meaning becomes executable, behavior becomes inspectable, and the human remains root authority.**

Version: 0.1.0 Prototype  
License: AGPLv3-or-later

## Public standard

```text
.soul

⧉

A Soul Protocol object
```

The symbol is the object.

In prose, call it **a Soul Protocol object**.

A Soul Protocol object is a semantic-machine vessel: readable by humans, structured for machines, mountable by runtimes, bounded by receipts, and designed to preserve continuity instead of letting context evaporate.

See [⧉](SOUL_PROTOCOL.md).

## What this is

Soul Protocol is a public AI-native operating prototype built around mountable Soul Protocol objects.

It is not a chatbot, wrapper, plugin, desktop assistant, or agent demo. It is the first public edge of a deeper operating lineage: a user-governed computing environment where AI is not trapped inside app-shaped boxes, where behavior is bound by readable control matter, and where powerful actions pass through authority, capability, permission, and receipt.

`.doctrine` remains the current compatibility surface during transition.

## What it unlocks

Soul Protocol moves AI from a product window into a governed operating surface:

- the user remains root authority
- Soul Protocol objects define operating behavior
- actions are capability-scoped
- permissioned actions emit receipts
- runtime state stays inspectable
- adapters connect models, files, tools, apps, and services
- public code remains open under AGPLv3-or-later

## Current status

Soul Protocol currently includes:

- SDK and CLI support for `.doctrine` compatibility
- public Soul Protocol object standard docs
- `.doctrine` loading, parsing, validation, and mounting
- mount receipts with context hashes
- public concept nodes and generated node registry
- adapter examples
- Soul Protocol prototype shell
- default Soul Protocol profile
- action receipts and runtime state logging
- GitHub Actions validation

## Soul Protocol prototype shell

The current compatibility command is `doctrineos`. It is the first runnable Soul Protocol control surface.

It loads a profile, mounts it, plans command intent, identifies needed capabilities, asks for permission where required, routes approved commands to safe adapters, writes action receipts, and records runtime state.

```bash
doctrineos --json
doctrineos inspect workspace
doctrineos --yes inspect workspace
```

Runtime state and receipts are currently written under `.doctrineos/` for compatibility.

## Quick start

```bash
git clone https://github.com/Xxaion-Labs/Soul-Protocol.git
cd Soul-Protocol
pip install -e .
```

Mount the standard public compatibility file:

```bash
doctrine mount standard_public_template.doctrine
```

Run the Soul Protocol prototype shell:

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

- [⧉](SOUL_PROTOCOL.md) — public `.soul` / Soul Protocol object standard
- [Vision](VISION.md) — why Soul Protocol exists
- [Architecture](ARCHITECTURE.md) — system layers and control spine
- [Roadmap](ROADMAP.md) — build path from prototype to public operating environment
- [Prototype Shell](docs/prototype-shell.md) — runnable shell guide
- [Specification](SPEC.md) — `.soul`, `.doctrine` compatibility, mounting, validation, and receipts
- [Compatibility](COMPATIBILITY.md) — public compatibility requirements
- [Examples](examples/README.md) — adapter and workflow examples
- [Nodes](nodes/README.md) — public concept node library
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution guide

## Repository structure

- `SOUL_PROTOCOL.md` — public `.soul` / `⧉` standard
- `standard_public_template.doctrine` — core public compatibility template
- `profiles/` — Soul Protocol profile examples
- `doctrineos/` — compatibility prototype shell and runtime
- `sdk/` — Python SDK
- `nodes/` — public concept nodes
- `registry/` — generated public node registry
- `examples/` — adapter and workflow examples
- `tools/` — validation and helper tools
- `tests/` — SDK, example, and shell tests
- `docs/` — additional Soul Protocol docs

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
