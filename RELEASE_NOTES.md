# Release Notes

## v1.0.0-public-baseline

Doctrine Protocol public baseline.

This release establishes `.doctrine` as a public, mountable protocol surface for reusable AI behavior rules, concept nodes, and doctrine files.

### Included

- Public standard doctrine template
- Python SDK
- CLI commands for mount, validate, inspect, and registry build
- Parser and validator
- Mount receipts with context hashes
- Public specification
- Compatibility guidance
- Starter node library
- Generated node registry
- Tests and GitHub Actions validation
- Apache 2.0 licensing

### Public starter nodes

- anti-drift
- clarity
- concise-response
- example
- safety-boundary
- user-authority

### Compatibility floor

A project may be `.doctrine compatible` when it can load doctrine files or concept nodes, parse metadata and sections, validate required structure, produce mounted instruction context, preserve stable IDs and source paths, and keep mount receipts inspectable.
