# Roadmap

DoctrineOS is the public AI-native operating system prototype built on Doctrine Protocol.

The roadmap moves from protocol foundation to userland prototype, then into local runtime, bootable environment, AI-native desktop, and deeper operating-system integration.

## Phase 0: Protocol Foundation

Status: complete.

- Doctrine Protocol SDK
- CLI for mount, validate, inspect, and registry build
- parser and validator
- mount receipts with context hashes
- public standard doctrine template
- starter public nodes
- generated node registry
- validation workflow
- AGPLv3-or-later anti-capture license

## Phase 1: Userland Prototype

Status: complete.

Goal: prove the control spine before building a full OS image.

Complete:

- DoctrineOS shell
- doctrine profile loader
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
doctrine profile -> mount -> command -> capability -> permission -> adapter -> receipt -> state
```

## Phase 2: Local Runtime

Status: next.

Goal: make DoctrineOS useful on a normal machine.

Planned:

- capability kernel
- receipt ledger
- filesystem adapter
- project workspace model
- local model adapter
- safe terminal adapter with permission gates
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

Goal: make the whole environment doctrine-aware.

Planned:

- doctrine-aware launcher
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
