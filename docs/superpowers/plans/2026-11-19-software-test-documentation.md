# Software Test Documentation Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate a reusable `software-test-documentation` skill that converts SRS-level requirements into a consistently formatted STS, test cases, requirements-level edge-case review, execution procedures, and traceability artifacts.

**Architecture:** Keep the skill entrypoint small and route detailed document contracts to focused references. The workflow is requirements-only for the first version: `SRS → extraction → test design → edge-case review → ordered procedures → traceability → quality review`. Code-derived regression cases remain a documented future extension, not an initial input.

**Tech Stack:** Markdown skill instructions, Markdown reference templates, YAML UI metadata, repository shell validator, and isolated pressure-scenario evaluation.

**Spec:** `docs/superpowers/specs/2026-11-19-software-test-documentation-design.md`

## Global Constraints

- The initial workflow operates at the requirements/specification level only.
- Every STS must use the fixed section order defined in the design spec.
- Test procedures must use explicit numbered steps with expected results for meaningful checkpoints.
- Requirements-level edge cases must be separated from implementation/code-derived cases.
- Missing or ambiguous expected behavior must be reported, not fabricated.
- IDs use `REQ-`, `TC-`, `SUITE-`, `EDGE-`, and `ISSUE-` prefixes.
- Markdown is the default output format and source-language matching is the default language behavior.

## Review Focus

- Incomplete SRS requirements: the skill should mark the case as clarification-needed instead of inventing expected behavior; test in the extraction and quality-review task.
- Boundary and just-outside values: the skill should distinguish stated limits from unsupported assumptions; test in the edge-case guide task.
- Requirement conflicts: the skill should preserve both source references and raise an issue; test in the requirements-analysis task.
- Procedure ordering: setup, action, checkpoint, cleanup, and evidence should remain separate and ordered; test in the STS template task.
- Traceability gaps: orphan requirements and orphan test cases should be visible; test in the traceability-reference task.

---

### Task 1: Establish Failing Pressure Scenarios

**Files:**
- Create: `automotive-development/skills/software-test-documentation/evaluation/pressure-scenarios.md`
- Create: `automotive-development/skills/software-test-documentation/evaluation/baseline-results.md`

**Interfaces:**
- Consumes: the design spec and realistic SRS fragments.
- Produces: pressure scenarios and observed baseline failures used to shape the skill.

- [ ] **Step 1: Write three combined-pressure scenarios** covering incomplete requirements, boundary-heavy behavior, and conflicting requirements while requiring an STS with ordered procedures.
- [ ] **Step 2: Run the scenarios without the skill** using an isolated evaluator and record the exact omissions, invented assumptions, ID inconsistencies, and procedure-shape failures.
- [ ] **Step 3: Record baseline rationalizations and failure patterns** in `baseline-results.md`, separating missing structure from incorrect judgment.
- [ ] **Step 4: Verify the baseline artifacts** include at least one scenario where a no-guidance agent would plausibly fabricate an expected result or skip traceability.

### Task 2: Create the Skill Entrypoint and UI Metadata

**Files:**
- Create: `automotive-development/skills/software-test-documentation/SKILL.md`
- Create: `automotive-development/skills/software-test-documentation/agents/openai.yaml`

**Interfaces:**
- Consumes: baseline failures from Task 1 and the design spec.
- Produces: a discoverable skill that routes to the relevant references and enforces the requirements-level STS workflow.

- [ ] **Step 1: Write the minimal skill contract** with a `Use when...` description, scope boundary, required workflow, output contract, and routing links.
- [ ] **Step 2: Add explicit counters for baseline failures** including unsupported behavior invention, vague procedures, missing expected results, and orphan requirements.
- [ ] **Step 3: Add the UI metadata** with a display name, short description, default prompt mentioning `$software-test-documentation`, and implicit invocation enabled.
- [ ] **Step 4: Verify the entrypoint** links every reference it conditionally requires and does not duplicate the detailed schemas.

### Task 3: Define the STS and Test-Case Format

**Files:**
- Create: `automotive-development/skills/software-test-documentation/references/sts-template.md`
- Create: `automotive-development/skills/software-test-documentation/references/test-case-schema.md`

**Interfaces:**
- Consumes: the ID rules and STS output contract from the spec.
- Produces: copyable Markdown structures for the fixed STS section order and individual test cases.

- [ ] **Step 1: Write the STS template** with all fourteen required sections in the specified order.
- [ ] **Step 2: Write the test-case schema** with IDs, traceability, preconditions, environment, data, numbered procedure, checkpoint expectations, pass/fail rule, cleanup, evidence, and assumptions.
- [ ] **Step 3: Add one complete TypeScript-oriented example** showing a requirements-level input validation case without relying on implementation details.
- [ ] **Step 4: Add a format checklist** that catches collapsed setup/action/verification paragraphs, missing expectations, inconsistent IDs, and unordered procedures.

### Task 4: Define Edge-Case Review and Traceability Guidance

**Files:**
- Create: `automotive-development/skills/software-test-documentation/references/edge-case-review-guide.md`
- Create: `automotive-development/skills/software-test-documentation/references/traceability-and-quality-checks.md`

**Interfaces:**
- Consumes: the STS/test-case formats from Task 3.
- Produces: focused guidance for SRS-level edge-case decisions and bidirectional coverage review.

- [ ] **Step 1: Write the edge-case review contract** with candidate dimensions, disposition values, and the rule that unsupported behavior becomes a question rather than a fabricated expectation.
- [ ] **Step 2: Write the traceability model** for `REQ → TEST-CONDITION → TEST-CASE`, generated IDs, orphan detection, and code-derived cases excluded from the initial mode.
- [ ] **Step 3: Write the quality-review checklist** for coverage, duplicates, unsupported assumptions, missing expected results, section order, and issue classification.
- [ ] **Step 4: Add a compact review matrix** mapping common SRS signals to edge-case checks and the required evidence in the STS.

### Task 5: Validate, Refactor, and Package the Skill

**Files:**
- Modify: `automotive-development/skills/software-test-documentation/SKILL.md`
- Modify: `automotive-development/skills/software-test-documentation/references/*.md`
- Create: `automotive-development/skills/software-test-documentation/evaluation/green-results.md`

**Interfaces:**
- Consumes: all skill resources from Tasks 2–4 and the pressure scenarios from Task 1.
- Produces: a validated skill whose outputs satisfy the design spec under realistic SRS pressure.

- [ ] **Step 1: Run the repository skill validator** against `automotive-development/skills/software-test-documentation` and fix frontmatter, naming, or placeholder failures.
- [ ] **Step 2: Run the same pressure scenarios with the skill loaded** and capture the generated document shape and decisions.
- [ ] **Step 3: Compare green results against baseline failures** and add only narrow wording or reference changes that close observed loopholes.
- [ ] **Step 4: Re-run validation** after refactoring and confirm all required sections, ordered procedures, edge-case dispositions, and traceability links remain present.
- [ ] **Step 5: Review the final file tree and git diff** to confirm only the design, plan, and requested skill artifacts were added.
