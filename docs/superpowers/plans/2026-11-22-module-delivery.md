# Module Delivery Implementation Plan

> **For agentic workers:** Use the design in `docs/superpowers/specs/2026-11-22-module-delivery-design.md`; verify each task before starting the next. This plan is executed in the current session without a new commit.

**Goal:** Make automotive module work traceable from source requirements to final verified code and show a complete example.

**Architecture:** One reusable decision principle lives in `skills/`. The automotive package owns the lifecycle playbook, output contract, deterministic structural check, and worked example. Existing SRS, STS, readiness, implementation, change, and verification skills remain the stage owners.

**Tech stack:** Markdown and a Python 3 standard-library validator.

**Spec:** `docs/superpowers/specs/2026-11-22-module-delivery-design.md`

## Tasks

- [x] Add `skills/decision-trace/SKILL.md` and its ignored Korean mirror; link it from shared specification, engineering, and README without duplicating the principle.
- [x] Add `skills/workflow-design/SKILL.md` for reusable stage and handoff reasoning, with Korean mirror and routing from the automotive full-delivery playbook.
- [x] Add `skills/skill-design/SKILL.md` as the agent-facing naming and placement principle for future skills, with Korean mirror and an invocation entry.
- [x] Add the automotive module-delivery playbook and artifact contract; update router and stage playbooks to route issues and results through the contract.
- [x] Create a complete illustrative module bundle under automotive examples, including source, SRS, STS, issues, work packet, traceability, and verification.
- [x] Make its SRS and STS follow the shared reference formats; add a generated completion report and an honest skill-to-output audit.
- [x] Add a deterministic structural validator and exercise it on the valid example and deliberately broken copies.
- [x] Mirror new automotive instructional docs to the ignored Korean tree, then verify links, package structure, and Git status. Do not commit this task.

## Review focus

- An unresolved issue must not appear as an approved expected result.
- A decision must not be marked complete before its document and code effects are evidenced.
- A simulated example must not claim real ECU or HIL execution.
- The validator should detect broken ID links but must not claim to verify requirement meaning.
- The full playbook must not duplicate or bypass leaf-skill approval gates.
