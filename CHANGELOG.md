# Changelog

## Unreleased

### Changed

- Renamed the public project surface to Soul Protocol.
- Replaced the old public object grammar with the simplified Soul Protocol grammar:

```text
.soul

⧉
```

- Added `SOUL_PROTOCOL.md` as the public object standard.
- Clarified `.doctrine` as the current compatibility surface during transition.
- Updated compatibility language to include `.soul compatible` and `.doctrine compatible`.
- Updated public validation to check the Soul Protocol standard.
- Preserved AGPLv3-or-later licensing.
- Routed runtime capability decisions through a capability kernel.

### Added

- Soul Protocol direction and architecture docs.
- Soul Protocol compatibility shell.
- Default compatibility profile.
- Action receipts and runtime state logging.
- Tests for boot, profile loading, permission refusal, approved action execution, receipt creation, and state creation.
- Capability kernel with capability modes, risk levels, policy decisions, and runtime policy output.
- Default public capability policy.
- Capability kernel tests and documentation.

## v0.1.0-prototype

First public prototype milestone.

### Added

- Public standard compatibility template
- Python SDK
- CLI commands for mount, validate, inspect, and registry build
- Parser and validator
- Mount receipts with context hashes
- Public specification
- Compatibility guidance
- Starter node library
- Generated node registry
- Tests and GitHub Actions validation
- Adapter examples
- Prototype shell
- AGPLv3-or-later licensing

### Public starter nodes

- anti-drift
- clarity
- concise-response
- example
- safety-boundary
- user-authority

### Compatibility floor

A project may be `.doctrine compatible` when it can load compatibility files or concept nodes, parse metadata and sections, validate required structure, produce mounted instruction context, preserve stable IDs and source paths, and keep mount receipts inspectable.
