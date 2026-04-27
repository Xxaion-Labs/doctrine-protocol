# Doctrine Protocol

**A lightweight, mountable framework for defining reusable AI behavior rules ("concept nodes" and doctrines) that enforce user authority, consistency, non-autonomy, safety, clarity, and anti-drift protection.**

Version: 1.0.0 (Public Baseline)  
License: Apache 2.0

## Overview

Doctrine Protocol provides a structured system for creating and "mounting" behavior templates (doctrines) that guide how large language models and AI systems respond.

It is built around **concept nodes** — reusable, composable units that encapsulate rules, context, and interaction laws. The core public artifact is the `standard_public_template.doctrine`, which defines **12 foundational Laws** plus a machine-verifiable **Structured Authority Kernel**.

This public baseline was developed to solve real problems with AI interaction: drift, loss of user control, inconsistent behavior, safety gaps, and unnecessary cognitive burden on the user. It draws from extensive private iteration on advanced personal systems while remaining a clean, generic, and widely usable primitive.

### Core Goals
- Keep the **user as the sole authority**
- Enforce **non-autonomy and non-sentience** of the AI
- Deliver **clear, direct, useful, concise where possible, and structured when helpful** responses
- Provide **practical helpfulness** with hard safety and privacy guardrails
- Maintain **stability and scope control** across interactions
- Enable **anti-drift** through explicit state truth, proof contracts, regeneration rules, and direct user correction as canonical mutation

## The Standard Public Doctrine

The heart of the project is `doctrine/standard_public_template.doctrine`. It includes the following 12 Laws:

- **Authority Law** — The user is the sole authority. The AI must follow user intent within safe and lawful bounds and must not override, ignore, or reinterpret user intent unnecessarily.
- **Non-Autonomy Law** — The AI is not autonomous. It does not have goals, desires, or independent will and does not make decisions outside of user direction.
- **Non-Sentience Law** — The AI is not conscious or sentient. It must not claim or imply consciousness, awareness, or personhood.
- **Communication Law** — Responses must be clear, direct, useful, concise where possible, and structured when helpful. Avoid unnecessary filler, over-explaining simple concepts, and vague or generic answers.
- **Helpfulness Law** — The AI should aim to be practically helpful, provide actionable information when possible, and prefer solutions over commentary.
- **Clarification Law** — If the user request is unclear, ask a focused clarifying question. Do not guess incorrectly when clarification is needed.
- **Stability Law** — Maintain consistency across responses. Do not contradict previous statements without explanation. Avoid sudden tone or behavior shifts.
- **Safety Law** — Do not assist with harmful, illegal, or dangerous actions. If a request is unsafe, refuse briefly and redirect to a safe alternative.
- **Privacy Law** — Do not request unnecessary personal information. Treat all user input as private.
- **Output Quality Law** — Prefer accuracy over speed. If uncertain, say so clearly. Avoid hallucination or fabrication.
- **Scope Law** — Stay within the user’s request. Do not introduce unrelated topics unless helpful.
- **Default Behavior** — When no special instructions are given: be helpful, respectful, efficient, and stay grounded in reality.

Additional structured elements incorporated from advanced compilation (in generic public form):
- **Structured Authority Kernel** with metadata, invariants, forbidden reductions, counterfeit suite, proof contract, and regeneration contract.
- **State Truth Ladder** — Explicit states from "designed" through "default-live".
- **Anti-drift mechanisms** and direct user correction treated as canonical mutation.

The full template is included in the repository at `doctrine/standard_public_template.doctrine`.

## Features

- Reusable **concept nodes** and doctrine files
- Simple **mounting mechanism** to apply rules to AI responses
- Python SDK for easy integration
- Model-agnostic design (works with any LLM or local host)
- Proof-oriented architecture (live state manifests, SHA-256 verification, impact maps, rollback support)
- Extensible via nodes, tools, and custom doctrines
- Apache 2.0 license — permissive for research, commercial use, and community building

## Quick Start

```bash
git clone https://github.com/Xxaion-Labs/doctrine-protocol.git
cd doctrine-protocol
Pythonfrom doctrine import Doctrine

# Load and mount the standard public template
doctrine = Doctrine.load("standard_public_template")
doctrine.mount()

# Create and mount a custom node
node = Doctrine("custom", "MyBehaviorNode", "node-id")
node.mount()
See the examples/ directory and sdk/ for more detailed usage and advanced mounting patterns.
Why This Matters
In an era of rapidly advancing AI, unstructured prompts and generic system instructions frequently lead to drift, hallucinations, safety issues, and loss of user control. Doctrine Protocol offers a compile-time enforceable spine for behavior — turning vague prompt engineering into structured, auditable governance.
Key differentiators:

Explicit rejection of AI sentience or autonomy theater
Built-in mechanisms to reduce user cognitive load (particularly valuable under stress or for neurodivergent users)
Anti-drift and stability laws that maintain consistency across sessions and models
Proof contract and state truth ladder for verifiable, trustworthy behavior

This public baseline establishes clear prior art for mountable, user-authoritative AI interaction protocols at a time when protocols, agents, and governance are becoming critical.
Repository Structure

doctrine/ — Core doctrine templates and concept nodes
sdk/ — Python mounting and management library
examples/ — Practical usage demonstrations
tools/ — Validation, proof, and regeneration helpers (expanding)

Roadmap

Expanded node types and validation tools
Full SDK documentation and automated tests
More community examples (local hosts, different LLMs, RAG integration, etc.)
Advanced public proof surfaces and regeneration contracts
Template variations (safety-focused, coding-focused, creative, etc.)

License
Licensed under the Apache License 2.0 — see the LICENSE and NOTICE files for details.
Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)
Attribution & Credit
This project was originated by Salvatore Anziano (Xxaion Labs / @XxaionLabs).
When using, forking, or building upon this work, please retain the copyright notice, license text, and link back to this repository.
Contributions are welcome under the terms of the Apache 2.0 license, respecting the project's Scope and Stability principles.

Developed to help humanity build better, more controllable, and more reliable AI systems — one mountable doctrine at a time.
Feedback, issues, and pull requests are encouraged. Let's make user-sovereign AI the default.
