# Software Test Documentation Skill Design

## Intent

Create a reusable skill that reads an SRS or other requirements document and produces a consistent Software Test Specification (STS) and supporting test-design documents. The skill is intended to make the planned test scope explicit before implementation begins, including the test sequence, expected results, traceability, and requirements-level edge cases.

## Goals

- Extract testable requirements, conditions, constraints, and assumptions from an SRS.
- Decide what should be tested and explain why each test area is in scope.
- Derive normal, error, boundary, invalid-input, state-transition, permission, and other requirements-level edge cases when the SRS supports them.
- Produce a fixed-format STS with a clear execution order and pass/fail criteria.
- Maintain traceability from requirement IDs to test conditions and test cases.
- Identify ambiguous, missing, contradictory, or non-verifiable requirements separately from the test cases.
- Keep document identifiers, field names, severity/priority labels, and status values consistent.

## Non-goals

- Do not infer implementation-specific tests from source code in the initial workflow.
- Do not design unit-test code, integration-test code, automation scripts, or fixtures.
- Do not claim that a test is executable when the SRS does not define enough information.
- Do not include implementation-discovered defects or code-review edge cases in the initial STS. Reserve a future regression-update mode for that work.

## Scope Boundary

The initial skill operates at the requirements/specification level:

`SRS → requirements extraction → test scope → test conditions → edge-case review → STS/test cases → traceability and quality review`

The future extension may add:

`implementation/code review → discovered behavior or defect → regression test update`

That extension must preserve the original requirement IDs and mark code-derived cases separately from SRS-derived cases.

## Approaches Considered

### 1. Document-generation-only workflow

Generate an STS and test cases from the SRS with minimal traceability.

Trade-off: quick to use, but weak at identifying coverage gaps and keeping requirements linked to tests.

### 2. Requirements-traceability workflow — selected

Build the STS around a stable chain of identifiers:

`REQ → TEST-CONDITION → TEST-CASE`

Generate the document sections, edge-case review, and execution procedure from that chain.

Trade-off: requires more disciplined extraction, but gives the clearest coverage, gap detection, and change impact analysis.

### 3. Full test-lifecycle workflow

Provide separate modes for SRS analysis, STS generation, edge-case review, implementation review, and regression maintenance.

Trade-off: extensible, but broader than the immediate need. The initial skill will implement the requirements-level modes and leave a clear extension point for code-derived regression updates.

## Proposed Skill Structure

Location: `automotive-development/skills/software-test-documentation/`

```text
software-test-documentation/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── sts-template.md
    ├── test-case-schema.md
    ├── edge-case-review-guide.md
    └── traceability-and-quality-checks.md
```

The main `SKILL.md` will contain routing, required workflow, output contract, and document-quality rules. Detailed document fields and review heuristics will live in focused references so they can be loaded only when needed.

## Required Workflow

1. Identify the source requirements document, version, scope, and exclusions.
2. Extract every requirement with its original ID or assign a stable ID when none exists.
3. Classify each requirement as functional, non-functional, interface, data, security/permission, state/lifecycle, operational, or constraint.
4. Mark each requirement as testable, partially testable, ambiguous, contradictory, or not testable from the supplied information.
5. Define test conditions and the applicable test type or test level for each testable requirement.
6. Derive the normal path and explicitly supported error paths.
7. Conduct the requirements-level edge-case review using only stated or logically implied boundaries; label assumptions instead of silently inventing behavior.
8. Group test conditions into test suites and order them by prerequisite and dependency.
9. Write each test case with preconditions, setup/data, exact procedure steps, expected result per step or checkpoint, cleanup, priority, and traceability.
10. Produce the STS, test-case list, edge-case review, traceability matrix, and open-issues list in the fixed formats.
11. Run the document quality review: coverage, ordering, duplicate cases, orphan requirements, unsupported assumptions, missing expected results, and inconsistent identifiers.

## STS Output Contract

Every generated STS must contain these sections in this order:

1. Document control and revision history
2. Purpose and scope
3. References and source requirement versions
4. System under test and test boundaries
5. Test assumptions, dependencies, environment, and data needs
6. Requirement classification and testability assessment
7. Test strategy and selected test types
8. Test suites and execution order
9. Detailed test cases
10. Requirements-to-test traceability matrix
11. Requirements-level edge-case review
12. Ambiguous, missing, contradictory, or deferred requirements
13. Entry criteria, exit criteria, pass/fail rules, and evidence requirements
14. Risks, exclusions, and open decisions

## Test Procedure Contract

Each test case must make the execution sequence unambiguous:

- Test case ID and linked requirement IDs
- Objective
- Priority and rationale
- Preconditions
- Environment/configuration
- Test data setup
- Numbered procedure steps in execution order
- Expected result for every meaningful step or checkpoint
- Final pass/fail criterion
- Cleanup or reset steps
- Evidence to capture
- Notes, assumptions, and unresolved questions

The skill must not collapse setup, action, and verification into a vague paragraph. If the SRS does not define an expected result, the case must be marked as blocked or require clarification rather than inventing a result.

## Edge-Case Review Contract

The edge-case review must be a separate, auditable section. For each candidate case, record:

- Edge-case ID
- Linked requirement ID
- Trigger or boundary
- Why the case matters
- Expected behavior stated by the SRS, logically implied behavior, or missing behavior
- Test disposition: include, clarify, defer, or exclude
- Priority/risk
- Follow-up question if the requirement is insufficient

Review dimensions include empty/null/missing values, minimum and maximum values, just-inside and just-outside boundaries, invalid formats, duplicate inputs, ordering, state transitions, retries/timeouts, permissions, unavailable dependencies, concurrency where specified, localization/time zones where specified, and data volume limits. A dimension is only applicable when supported by the SRS or explicitly marked as a question; the skill must not turn generic checklists into unsupported product behavior.

## Traceability and Identifier Rules

- Preserve source requirement IDs whenever present.
- Use stable generated IDs only when the source has no usable IDs, and record the mapping.
- Use prefixes `REQ-`, `TC-`, `SUITE-`, `EDGE-`, and `ISSUE-`.
- Every test case must trace to at least one requirement or be explicitly labeled as a derived-risk case.
- Every testable requirement must trace to one or more test conditions or be listed as an uncovered requirement.
- Do not silently reuse IDs after a requirement or test case is removed.

## Validation Plan

The skill will be created and validated using pressure scenarios based on realistic SRS inputs. Validation will check that the agent:

- follows the fixed section order;
- writes explicit numbered procedures and expected results;
- separates stated behavior from assumptions;
- finds requirements-level edge cases without inventing implementation behavior;
- reports ambiguous or untestable requirements;
- produces complete bidirectional traceability;
- maintains consistent IDs and statuses.

The validation will include incomplete requirements, conflicting requirements, boundary-heavy requirements, and a requirement with no explicit ID. The skill will be run through the repository's skill validator after authoring.

## Open Implementation Choices

- Default output format: Markdown, with tables where they improve traceability and numbered lists for procedures.
- Default language: match the source SRS language unless the user requests another language.
- Default test priority vocabulary: Critical, High, Medium, Low; use source terminology when one is already defined.
- Default behavior for missing requirements: document the gap and ask for clarification; do not fabricate expected behavior.
