# Automotive SRS Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a small skill that converts sentence-level automotive requirements into a structured SRS while identifying ambiguity, context mismatch, duplication, and unverifiable wording.

**Architecture:** Keep the main behavior in `SKILL.md` and place the output contract plus a concrete example in `references/`. The skill will separate source text, normalized requirement, refinement rationale, and unresolved confirmation items so it does not silently invent requirements.

**Tech Stack:** Markdown, YAML metadata, Codex skill conventions.

**Spec:** `docs/superpowers/specs/2026-11-19-automotive-srs-design.md`

## Global Constraints

- Output is Markdown SRS.
- Do not determine ISO 26262, ISO 21434, or ASPICE compliance.
- Do not invent safety integrity levels, threat models, or detailed architecture.
- Do not generate implementation or test code.
- Keep original wording distinct from proposed refinement.

## Review Focus

- Ambiguous actor, trigger, condition, or measurable threshold: must become a refinement proposal or confirmation item.
- Context mismatch between related requirements: must be flagged rather than silently reconciled.
- Duplicate or inconsistent terminology: must be consolidated with the chosen term explained.
- Unverifiable wording such as “quickly” or “normally”: must receive a measurable acceptance proposal or remain unresolved.
- Safety/security implications not supported by input: must remain confirmation items, not conclusions.

### Task 1: Define the Automotive SRS skill behavior

**Files:**
- Modify: `/Users/jeong/Desktop/skills/automotive-srs/SKILL.md`

**Interfaces:**
- Consumes: User-provided sentence-level automotive requirements.
- Produces: A Markdown SRS with structured requirements, quality findings, refinement proposals, and unresolved items.

- [ ] Replace the initializer placeholder description with a discriminating description for automotive SRS generation and refinement.
- [ ] Document the workflow: classify input, normalize requirements, inspect quality/context, preserve source wording, and produce the SRS sections.
- [ ] Define requirement fields: ID, statement, rationale/source, priority, verification method, dependencies, and status.
- [ ] Define the required distinction between source text, normalized text, proposed refinement, and confirmation-needed text.
- [ ] State that unsupported assumptions must be marked `TBD`, `TBC`, or confirmation-needed.

### Task 2: Add the reusable output contract and example

**Files:**
- Create: `/Users/jeong/Desktop/skills/automotive-srs/references/srs-output-format.md`
- Create: `/Users/jeong/Desktop/skills/automotive-srs/references/example.md`

**Interfaces:**
- Consumes: The workflow defined in `SKILL.md`.
- Produces: A compact output schema and an input-to-SRS example for future use.

- [ ] Define the Markdown section order and requirement table fields in `srs-output-format.md`.
- [ ] Add an example input containing at least one vague timing phrase, one missing condition, and one context mismatch.
- [ ] Show the resulting SRS, findings, refinement proposals, and unresolved confirmation items in `example.md`.
- [ ] Link both references from `SKILL.md` with routing guidance.

### Task 3: Configure metadata and validate

**Files:**
- Modify: `/Users/jeong/Desktop/skills/automotive-srs/agents/openai.yaml`

- [ ] Set the UI description and default prompt to describe SRS generation and requirement refinement.
- [ ] Run `quick_validate.py` against the skill folder when the YAML dependency is available.
- [ ] Inspect the generated tree and confirm all references are linked from `SKILL.md`.
