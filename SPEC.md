# Doctrine Protocol Specification

Doctrine Protocol is the control substrate inside DoctrineOS.

It defines a portable, plain-text format for reusable AI behavior rules, concept nodes, doctrine files, mounting, validation, and mount receipts.

## Purpose

Doctrine Protocol lets behavior control material be written, loaded, validated, mounted, inspected, and carried into AI runtimes or workflows.

In DoctrineOS, mounted doctrine supplies the behavioral substrate for the operating environment.

## Core concepts

### Doctrine

A doctrine is a structured behavior template. It may define laws, constraints, defaults, operating rules, or reusable interaction patterns.

### Concept node

A concept node is a smaller reusable behavior unit that can be mounted alone or composed with other nodes.

### Mounting

Mounting means converting a doctrine or concept node into a structured runtime payload.

A mount operation does not make an AI autonomous. It prepares instruction context that a user, model, adapter, or DoctrineOS runtime can apply.

### Mount receipt

A mount receipt is the structured output of a mount operation. It provides a machine-readable record of what was mounted.

## Node format

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

## Doctrine metadata

Doctrine files may include simple metadata at the top of the file:

```text
DOCTRINE FILE
version: 1.0.0
body_id: standard_public_doctrine_body_v1
```

Metadata is optional, but `body_id` is recommended for stable references.

## Doctrine filetype v1

`.doctrine` files are plain UTF-8 text files with a Markdown semantic layer and optional JSON sentinel blocks for machine-readable control material.

A sentinel block has this form:

```text
<<<NAME_JSON>>>
{"key":"value"}
<<<END_NAME_JSON>>>
```

A public parser should report malformed sentinel JSON instead of silently ignoring it.

A doctrine file should remain standalone for mount. External files may inform a doctrine, but should not be required to read, validate, or mount it.

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

A strict `.doctrine` file should additionally have:

- UTF-8 readable text
- parseable top metadata when metadata is present
- parseable `##` sections
- parseable JSON sentinel blocks when sentinel blocks are present

## Mount receipt shape

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
6. Keep mount receipts inspectable.

A tool is `.doctrine` filetype-compatible if it can also parse JSON sentinel blocks and report sentinel parse errors.

## Design constraints

- User authority remains central.
- Doctrines should remain readable as plain text.
- Mount receipts should be inspectable.
- Implementations should avoid implying AI sentience, autonomy, or independent will.
- The format should stay simple enough for people to fork, inspect, and improve.
