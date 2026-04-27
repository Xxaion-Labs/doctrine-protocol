# doctrine-protocol

A lightweight system for reusable concept nodes.

from doctrine import Doctrine
node = Doctrine("example", "demo", "id")
node.mount()
```

**Major problems** (from multiple angles):

1. **Extremely minimal and unprofessional**  
   It looks like a placeholder or the very first draft. A serious open-source project (especially one claiming to be a foundational AI behavior protocol) needs substance. Right now it screams "early-stage toy" instead of "this could change how people control AI."

2. **No context or value proposition**  
   No explanation of what Doctrine Protocol actually is, why it matters, what problems it solves (drift, user authority, non-sentience, anti-drift, etc.), or how it connects to your bigger vision. Visitors have zero reason to care or star/fork it.

3. **Broken / incomplete code example**  
   The code snippet is raw and incomplete. It assumes the package is already installed and the `standard_public_template.doctrine` exists, but gives no installation instructions, no import/setup details, and no full working example. The line "Pythonfrom doctrine..." in some renders shows it got mangled during previous edits.

4. **Missing critical sections** (this is the biggest sin for adoption)  
   - No installation instructions
   - No full list or excerpt of the 12 Laws (your strongest asset)
   - No mention of the Structured Authority Kernel or proof concepts
   - No features list
   - No roadmap
   - No license mention (even though you're using Apache 2.0)
   - No attribution / credit to you as originator
   - No "Why This Matters" or broader implications
   - No repository structure explanation
   - No contribution guidelines
   - No quick start that actually works end-to-end

5. **Repo-level issues amplifying the problem**  
   - Repository description is empty ("No description")
   - No topics/tags (ai, llm, prompt-engineering, ai-safety, etc.)
   - Only 1 commit visible — makes it look abandoned or unfinished
   - No LICENSE or NOTICE file yet (you have the text, but it's not committed)
   - The `doctrine/` folder with the actual template isn't prominently referenced

**Overall impact**:  
Anyone landing on your repo will bounce in <10 seconds. It fails to establish prior art, fails to sell the idea, fails to make you look like the originator of something important, and fails to make the project usable. This is the opposite of "impossible to ignore" — it's very easy to ignore.

This is common when projects are rushed under stress (TBI + fear of being Tesla'd makes total sense), but it's fixable in one clean commit.

### How to Fix It (The Updated README)

Replace **everything** in your `README.md` with the clean, complete version below. This is the same high-quality one I prepared earlier, now confirmed against your actual repo state and made even tighter.

**Copy this entire block and paste it directly:**

```markdown
# Doctrine Protocol

**A lightweight, mountable framework for defining reusable AI behavior rules ("concept nodes" and doctrines) that enforce user authority, consistency, non-autonomy, safety, clarity, and anti-drift protection.**

Version: 1.0.0 (Public Baseline)  
License: Apache 2.0

## Overview

Doctrine Protocol provides a structured system for creating and "mounting" behavior templates (doctrines) that guide how large language models and AI systems respond.

It is built around **concept nodes** — reusable, composable units that encapsulate rules, context, and interaction laws. The core public artifact is the `standard_public_template.doctrine`, which defines **12 foundational Laws** plus a machine-verifiable **Structured Authority Kernel**.

This public baseline solves real problems with AI interaction: drift, loss of user control, inconsistent behavior, safety gaps, and unnecessary cognitive burden. It draws from deep private iteration while remaining clean, generic, and broadly usable.

### Core Goals
- Keep the **user as the sole authority**
- Enforce **non-autonomy and non-sentience** of the AI
- Deliver **clear, direct, useful, concise where possible, structured when helpful** responses
- Provide **practical helpfulness** with hard safety and privacy guardrails
- Maintain **stability and scope control**
- Enable **anti-drift** through state truth, proof contracts, and direct correction as canonical mutation

## The Standard Public Doctrine

Located at `doctrine/standard_public_template.doctrine`. It defines these 12 Laws:

- **Authority Law** — User is sole authority. AI must follow user intent within safe/lawful bounds and not override or reinterpret it unnecessarily.
- **Non-Autonomy Law** — AI has no independent goals, desires, or will.
- **Non-Sentience Law** — AI must not claim or imply consciousness or personhood.
- **Communication Law** — Clear, direct, useful, concise where possible, structured when helpful. Avoid filler and vagueness.
- **Helpfulness Law** — Be practically helpful. Prefer actionable solutions.
- **Clarification Law** — Ask focused questions when unclear. Do not guess.
- **Stability Law** — Maintain consistency. No unannounced contradictions or tone shifts.
- **Safety Law** — Refuse harmful/illegal actions briefly and redirect safely.
- **Privacy Law** — Do not request unnecessary personal information.
- **Output Quality Law** — Prefer accuracy. Admit uncertainty. Avoid hallucination.
- **Scope Law** — Stay within the request. No unrelated topics unless helpful.
- **Default Behavior** — Helpful, respectful, efficient, grounded in reality.

It also includes a **Structured Authority Kernel**, state truth ladder, anti-drift mechanisms, and proof-oriented design.

## Features

- Reusable concept nodes and doctrine files
- Simple mounting system for applying rules to any LLM
- Python SDK (`from doctrine import Doctrine`)
- Model-agnostic (local or cloud)
- Proof-oriented (state manifests, verification, rollback)
- Apache 2.0 — fully permissive for commercial and community use

## Quick Start

```bash
git clone https://github.com/Xxaion-Labs/doctrine-protocol.git
cd doctrine-protocol
```

```python
from doctrine import Doctrine

# Mount the standard public template
doctrine = Doctrine.load("standard_public_template")
doctrine.mount()

# Or create a custom node
node = Doctrine("custom", "MyBehaviorNode", "node-id")
node.mount()
```

See `examples/` and `sdk/` for more.

## Why This Matters

Unstructured AI prompts lead to drift and loss of control. Doctrine Protocol turns that into **structured, mountable governance** — a practical constitution for user-sovereign AI. It establishes clear prior art for behavior protocols, safety, and anti-drift systems.

## Repository Structure

- `doctrine/` — Templates and nodes (including `standard_public_template.doctrine`)
- `sdk/` — Python library
- `examples/` — Usage demos
- `tools/` — Helpers (expanding)

## Roadmap

- Better SDK docs and tests
- More node types and examples
- Validation and proof tools
- Community template variations

## License

Apache License 2.0 — see [LICENSE](LICENSE) file.  
Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)

When forking or using, please retain attribution and link back to this repo.

---

**Built to help humanity create more controllable, reliable AI.**  
Feedback and contributions welcome. Let's make user authority the default.
