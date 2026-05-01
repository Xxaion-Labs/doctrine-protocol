# Specification

This specification defines the current public compatibility surface for `⧉`.

`⧉` is the symbol for a tesseract.

In prose, call it **a tesseract**.

A tesseract is a semantic-machine object that can carry human-readable meaning, machine-readable structure, mountable runtime context, and inspectable proof surfaces.

The current public compatibility surface is `.doctrine`.

## Purpose

The `.doctrine` compatibility surface lets tesseract material be written, loaded, validated, mounted, inspected, and carried into AI runtimes or workflows.

In DoctrineOS, mounted `.doctrine` material supplies the behavioral substrate for the operating environment.

## Core concepts

### ⧉

`⧉` is the object.

It must not be renamed, prefixed, or decorated in public standards. Use **a tesseract** only when prose needs words.

### Tesseract

A tesseract is a semantic-machine object with four operational faces:

```text
Semantic Face  - human-readable meaning
Machine Face   - machine-readable structure
Mount Face     - runtime context
Proof Face     - receipts, hashes, validation, or proof boundaries
```

### `.doctrine`

`.doctrine` is the current public compatibility surface for tesseracts.

A `.doctrine` file is plain UTF-8 text with a Markdown semantic layer and optional JSON sentinel blocks for machine-readable control material.

### Concept node

A concept node is a smaller reusable behavior unit that can be mounted alone or composed with other nodes.

### Mounting

Mounting means converting a `.doctrine` file or concept node into structured runtime context.

A mount operation does not make an AI autonomous. It prepares instruction context that a user, model, adapter, or runtime can apply.

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

## `.doctrine` metadata

`.doctrine` files may include simple metadata at the top of the file:

```text
DOCTRINE FILE
version: 1.0.0
body_id: standard_public_doctrine_body_v1
```

Metadata is optional, but `body_id` is recommended for stable references.

## `.doctrine` filetype v1

`.doctrine` files are plain UTF-8 text files with a Markdown semantic layer and optional JSON sentinel blocks for machine-readable control material.

A sentinel block has this form:

```text
<<<NAME_JSON>>>
{"key":"value"}
<<<END_NAME_JSON>>>
```

A public parser should report malformed sentinel JSON instead of silently ignoring it.

A `.doctrine` file should remain standalone for mount. External files may inform it, but should not be required to read, validate, or mount it.

## Validation

A valid `.doctrine` file should have:

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
  "instruction_context": "rendered context"
}
```

## Compatibility

A tool is compatible when it can:

1. Load a `.doctrine` file or concept node.
2. Parse metadata and sections.
3. Validate required structure.
4. Produce mounted instruction context.
5. Preserve stable IDs and source references where available.
6. Keep mount receipts inspectable.
7. Parse JSON sentinel blocks and report sentinel parse errors when present.

## Design constraints

- User authority remains central.
- `.doctrine` files should remain readable as plain text.
- Mount receipts should remain inspectable.
- Implementations should avoid implying AI sentience, autonomy, or independent will.
- `⧉` should not be used to imply physical four-dimensional geometry.
- The format should stay simple enough for people to fork, inspect, and improve.
