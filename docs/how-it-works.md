# How Soul Protocol Works

Soul Protocol is a public prototype for turning readable meaning into mountable runtime structure.

It is built around one practical claim:

```text
AI systems become safer and more useful when their operating context is structured, inspectable, permissioned, and reusable.
```

## 1. The problem: disposable context

Most AI workflows are temporary.

A user gives instructions. A system retrieves some files. A model answers. Then the useful shape of that interaction often evaporates.

That causes familiar failures:

- the same context must be reconstructed again
- important boundaries are forgotten
- old instructions drift into new work
- tools act without enough visible authority
- outputs are hard to audit later
- the user has to keep operating the machinery manually

Soul Protocol addresses this by giving important context a body.

## 2. The object

A Soul Protocol object is readable by humans and structured for machines.

```text
.soul

    (digital)
A                Soul Protocol object

 ⧉
```

The object can carry:

- semantic meaning
- metadata
- sections
- machine-readable control blocks
- mount requirements
- authority boundaries
- validation rules
- proof surfaces

In the current prototype, `.doctrine` files and public nodes serve as the compatibility layer that proves the mechanism while `.soul` matures as the public trajectory.

## 3. Mounting

Mounting converts an object into runtime context.

A mount operation should answer:

```text
What was mounted?
Where did it come from?
What structure was extracted?
What context was produced?
What errors occurred?
What hash identifies the mounted context?
```

The result is a mount receipt.

A mount receipt is not decoration. It is the first proof surface. It records the boundary between static object and runtime context.

## 4. Capability boundaries

After context is mounted, the runtime may receive a command.

The command is not executed blindly. It is interpreted against capabilities.

Examples:

```text
files.read
shell.run
network.access
model
repo.write
```

A capability is a named power. Naming the power makes it inspectable. Once it is inspectable, it can be permissioned.

## 5. Permission gates

Permission gates keep the human as root authority.

If a command requires a sensitive capability, the runtime should ask before crossing that boundary.

The key pattern is:

```text
intent -> required capability -> permission -> action
```

This makes powerful behavior slower where it should be slower, and faster where it is safe to be fast.

## 6. Adapters

Adapters connect the protocol runtime to the outside world.

An adapter might talk to:

- the filesystem
- a model API
- a local model
- a shell
- an editor
- a browser
- a repository
- another service

The adapter should only receive the approved action, not unlimited authority.

## 7. Receipts

After an action runs, the runtime emits a receipt.

A receipt should preserve:

- what was requested
- what capability was used
- whether permission was granted
- what adapter handled the action
- what result was produced
- when it happened
- what state changed

Receipts make the system less foggy. They let humans and future tools inspect what actually occurred.

## 8. State

State is the recoverable memory of the runtime.

It can include:

- mounted profile
- context hashes
- action receipts
- logs
- manifests
- policy decisions
- rollback points

State is not authority by itself. It is evidence. It helps the system recover without pretending to know more than it can prove.

## 9. Nodes

Nodes are small reusable behavior units.

A node can define a principle, boundary, style, workflow, or operating rule. Nodes can be mounted alone or composed with other context.

This lets a larger system grow from small verified pieces instead of one opaque blob.

## 10. The full spine

```text
Soul Protocol object
  -> validation
  -> mount
  -> mount receipt
  -> instruction context
  -> command interpretation
  -> capability check
  -> permission gate
  -> adapter call
  -> action receipt
  -> runtime state
```

This is the public control spine.

The mythic part is the compression of the idea. The practical part is the machinery: plain text, parsers, hashes, receipts, capabilities, adapters, and user authority.

## 11. What Soul Protocol is not

Soul Protocol is not a claim that AI is sentient.

It is not a claim that an AI should own authority.

It is not a claim that a symbol has supernatural power.

It is a protocol direction: make AI-native behavior mountable, inspectable, permissioned, and reusable.

## 12. Why open source matters

Soul Protocol is AGPLv3-or-later because the public floor should remain inspectable.

The protocol is meant to be forked, audited, criticized, extended, and improved. The whole point is legible power.
