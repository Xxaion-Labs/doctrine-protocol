# Architecture

DoctrineOS is a user-governed AI operating system prototype built around mountable Tesseracts.

```text
.glyph

    (digital)
A                Tesseract

 ⧉
```

The symbol is the object. In prose, call it **a Tesseract**.

DoctrineOS begins as a userland runtime on an open base system and grows toward a bootable, AI-native operating environment.

## Layer model

```text
DoctrineOS
├─ Base System
│  └─ Linux or another open base capable of booting real hardware
├─ Tesseract Control Layer
│  └─ .glyph and .doctrine-compatible mounts, authority policy, receipts, validation, profiles
├─ AI System Shell
│  └─ user-facing command surface for natural language and structured commands
├─ Capability Layer
│  └─ permissioned access to files, shell, apps, network, models, and tools
├─ Adapter Layer
│  └─ model adapters, local tools, APIs, filesystem, browser, editor, repo tools
├─ State Layer
│  └─ manifests, logs, hashes, receipts, rollback points, project context
├─ Node Package Layer
│  └─ installable public behavior nodes and packages
├─ Application Layer
│  └─ Tesseract-aware apps and workflows
└─ User Authority Layer
   └─ the human remains root authority
```

## Current control spine

The current prototype proves this spine:

```text
Tesseract-compatible file -> mount -> command -> capability -> permission -> adapter -> receipt -> state
```

## First build target

The first practical target is not a custom kernel.

The first target is a Tesseract-aware userland running on an open base system:

1. local command shell first
2. mounting before automation
3. receipts before trust
4. user authority before autonomy
5. bootable environment later

## Operating principles

- The OS must be user-governed.
- The AI layer must remain non-autonomous.
- Actions must be inspectable.
- Powerful actions must be permissioned.
- State must be legible and recoverable.
- Tesseracts must be mountable, composable, and verifiable.
- Public code must remain open under AGPLv3-or-later.

## Current milestone

DoctrineOS currently has a minimal shell that can:

- load a Tesseract-compatible profile
- mount it
- emit receipts
- accept user commands
- route commands to safe stub adapters
- log actions
- show state
- refuse unpermissioned actions

This proves the operating control spine before full desktop or kernel-level integration.

## Boundary

DoctrineOS does not claim AI sentience, autonomy, independent will, unsupported capability, or physical four-dimensional geometry.
