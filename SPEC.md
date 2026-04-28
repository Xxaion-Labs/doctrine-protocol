# Doctrine Protocol Specification

Version: 1.0.0 Public Baseline

## Purpose

Doctrine Protocol defines a portable format for reusable AI behavior rules, concept nodes, and doctrine files.

A `.doctrine` file is intended to be loaded, validated, mounted, and transformed into instruction context that an AI system or workflow can consume.

## Core Concepts

### Doctrine

A doctrine is a structured behavior template. It may define laws, constraints, defaults, or reusable interaction rules.

### Concept Node

A concept node is a smaller reusable unit that can be mounted alone or composed with other nodes.

### Mounting

Mounting means converting a doctrine or concept node into a structured runtime payload.

A mount operation does not make an AI autonomous. It prepares instruction context that a user, model, or adapter can apply.

### Mount Receipt

A mount receipt is the structured output of a mount operation. It provides a machine-readable record of what was mounted.

## Node Format

A public node should contain these sections:

```markdown
# Node: example

## Definition
A short definition.

## Usage
How the node is used.

## Example
A minimal example.

## ID
example-1
```

## Doctrine Metadata

Doctrine files may include simple metadata at the top of the file:

```text
DOCTRINE FILE
version: 1.0.0
body_id: standard_public_doctrine_body_v1
```

Metadata is optional, but `body_id` is recommended for stable references.

## Validation

A valid doctrine should have:

- a name
- an ID
- sections that can be parsed into instruction context

A strict public node should have:

- Definition
- Usage
- Example
- ID

## Mount Receipt Shape

A mount receipt should include:

```json
{
  "mounted": true,
  "name": "example",
  "id": "example-1",
  "source": "nodes/example.md",
  "mounted_at": "UTC timestamp",
  "context_sha256": "sha256 hash",
  "metadata": {},
  "errors": [],
  "instruction_context": "rendered doctrine context"
}
```

## Compatibility

A tool is Doctrine-compatible if it can:

1. Load a doctrine or node file.
2. Parse metadata and sections.
3. Validate required structure.
4. Produce mounted instruction context.
5. Preserve stable IDs and source references where available.

## Design Constraints

- User authority remains central.
- Doctrines should remain readable as plain text.
- Mount receipts should be inspectable.
- Implementations should avoid implying AI sentience, autonomy, or independent will.
- The format should stay simple enough for people to fork, inspect, and improve.
