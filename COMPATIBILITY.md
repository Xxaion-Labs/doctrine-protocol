# Compatibility

A project is Doctrine-compatible when it can use the public `.doctrine` format without requiring private extensions.

## Minimum requirements

- Load `.doctrine` files or concept nodes.
- Parse metadata and section headings.
- Validate required node structure.
- Produce mounted instruction context.
- Preserve stable IDs and source paths when available.
- Keep mount receipts inspectable.

## Badge language

Projects may say:

```text
.doctrine compatible
```

when they support the minimum requirements above.

## Implementation notes

Compatibility does not require a specific programming language. A compatible tool can be a Python package, local script, model adapter, editor plugin, or service wrapper.
