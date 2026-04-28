# Public Nodes

Doctrine nodes are small reusable behavior units for Doctrine Protocol and DoctrineOS-compatible runtimes.

Each node can be mounted alone or composed with other doctrine content.

## Node format

A public node should include:

```markdown
# Node: node-name

## Definition
Short definition.

## Usage
How to use the node.

## Example
Minimal example.

## ID
stable-node-id
```

## Current nodes

- `anti-drift.md` — encourages consistency with the active doctrine context
- `clarity.md` — encourages clear, direct, readable responses
- `concise-response.md` — encourages useful responses with minimal unnecessary length
- `example.md` — minimal reusable concept example
- `safety-boundary.md` — keeps safety and lawful boundaries explicit
- `user-authority.md` — keeps user direction central to the interaction

## Registry

The generated registry is stored at `registry/index.json`.

When adding or changing nodes, run:

```bash
python tools/build_registry.py
python tools/check_registry.py
```
