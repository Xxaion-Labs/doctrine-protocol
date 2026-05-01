# Roadmap

DoctrineOS is the public AI-native operating system prototype built around `.glyph` Tesseracts.

```text
.glyph

    (digital)
A                Tesseract

 ⧉
```

The roadmap moves from public filetype compatibility to userland prototype, then into local runtime, bootable environment, AI-native desktop, and deeper operating-system integration.

## Phase 0: Public Filetype Foundation

Status: complete.

- public `.glyph` standard
- current `.doctrine` compatibility surface
- SDK and CLI
- CLI for mount, validate, inspect, and registry build
- parser and validator
- mount receipts with context hashes
- public standard compatibility template
- starter public nodes
- generated node registry
- validation workflow
- AGPLv3-or-later anti-capture license

## Phase 1: Userland Prototype

Status: complete.

Goal: prove the control spine before building a full OS image.

Complete:

- DoctrineOS shell
- profile loader
- mount receipt display
- safe command router
- stub adapters
- action log
- permission prompts
- state manifest
- default DoctrineOS profile
- receipt and state tests

The current spine is:

```text
Tesseract-compatible file -> mount -> command -> capability -> permission -> adapter -> receipt -> state
```

## Phase 2: Local Runtime

Status: active.

Goal: make DoctrineOS useful on a normal machine.

In progress:

- capability kernel

Planned:

- receipt ledger
- filesystem adapter
- project workspace model
- local model adapter
- terminal adapter with permission gates
- config and profile manager
- rollback points

## Phase 3: Bootable Environment

Goal: ship a real bootable environment.

Planned:

- Linux-based image
- DoctrineOS shell as primary interface
- local-first setup wizard
- profile mounting at boot
- system state dashboard

## Phase 4: AI-Native Desktop

Goal: make the whole environment Tesseract-aware.

Planned:

- Tesseract-aware launcher
- app and workflow registry
- node package manager
- visible receipts
- permission ledger
- user-controlled automation queues

## Phase 5: Deeper OS Integration

Goal: move from AI-native userland toward deeper system integration.

Planned:

- service supervision
- policy-governed background tasks
- tighter filesystem indexing
- hardware and device capability models
- stronger sandboxing

## Release discipline

Every public release should remain:

- generic
- reusable
- auditable
- user-governed
- non-autonomous
- AGPLv3-or-later
- aligned with DoctrineOS as public-good infrastructure
- bounded against unsupported claims
