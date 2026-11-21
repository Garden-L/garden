---
name: implementation-readiness-review
description: Use when an automotive SRS and/or STS already exists and must be checked before production code or automated tests begin.
---

# Implementation Readiness Review

Apply the shared `engineering-design` method, then add the automotive-specific SRS/STS, safety, target, and HIL readiness criteria below. Review the existing SRS and STS before code implementation. Decide whether implementation can start, identify only the issues that could change the implementation or tests, and propose the first TDD slices.

This skill does not author or silently repair requirements, does not write production code or automated tests, and does not replace the SRS or STS skills.

## Review in five passes

### 1. Confirm the baseline

Record the SRS and STS identifiers/versions, the target software or component, and the available code, build, test, simulator, ECU, or HIL context. If an input needed to implement or test the first slice is missing, report it as an issue.

### 2. Check implementability

Read the SRS and STS together. For each behavior in scope, verify that the documents define enough to implement without guessing:

- trigger, inputs, outputs, units, limits, and timing;
- states, initialization, reset, shutdown, and recovery;
- invalid input, timeout, fault, and diagnostic behavior;
- interfaces, ownership, dependencies, and target constraints.

Report conflicts between SRS and STS instead of choosing an interpretation. Consider safety, cybersecurity, diagnostics, calibration, variants, and resource constraints only when they are supplied or explicitly in scope. Do not invent safety levels, compliance claims, or missing acceptance criteria.

### 3. Check testability and traceability

Build a compact mapping:

```text
SRS requirement → STS test case → implementation unit/interface → planned automated test
```

Flag requirements with no test coverage, tests with no requirement basis, unobservable expected results, and missing boundary/error/state/recovery cases. Keep the original IDs. Mark unknown expected behavior as `Decision Needed`.

### 4. Propose the implementation boundary

Define the smallest useful first vertical slice. For each proposed slice, state its responsibility, linked requirement/test IDs, inputs/outputs, dependencies, and unit-test boundary. Prefer deterministic core logic and stable interfaces before hardware or platform adapters.

### 5. Define the TDD order and gate

For the first slice, specify the first failing behavior test, the minimum implementation that should make it pass, and the evidence to retain. Use this loop:

```text
RED: write and run one failing behavior test
GREEN: implement the smallest change
REFACTOR: improve structure while all relevant tests stay green
```

Use one verdict:

- `READY` — no unresolved issue prevents the first slice from being implemented and tested.
- `READY WITH CONDITIONS` — the first slice is isolated, but listed conditions or decisions must be tracked.
- `NOT READY` — a missing decision, conflict, interface, expected result, or test environment can invalidate the first slice.

Do not declare `READY` because the documents are formatted or because a prototype could be written.

## Required output

Return a short Markdown report with this order:

1. **Verdict** — one of the three verdicts and the reason.
2. **Baseline** — SRS/STS versions, scope, and missing inputs.
3. **Findings** — only actionable findings, with severity `Blocking`, `High`, `Medium`, or `Observation`, affected IDs, evidence, and required decision.
4. **Traceability** — compact SRS → STS → implementation/test mapping and uncovered items.
5. **First TDD slice** — first failing test, minimum implementation, and next slices in order.
6. **Entry conditions** — what must be true before code changes begin.
7. **Open decisions** — decision-ready questions with recommended options and implementation/testing impact.

## Review boundaries

- Do not rewrite SRS/STS wording; send requirement changes to the owning workflow.
- Do not infer behavior from what would be convenient to implement.
- Do not treat unit-test readiness as proof of integration, target, or HIL readiness.
- Do not create code or automated tests during this review.
- If the user requests a throwaway prototype, label its assumptions and keep it separate from the readiness verdict.

## Completion checklist

- [ ] Document versions and scope are recorded.
- [ ] SRS/STS conflicts and missing inputs are explicit.
- [ ] Interfaces, states, errors, timing, and boundaries were checked.
- [ ] Requirement-to-test gaps are listed.
- [ ] First vertical slice and first failing test are defined.
- [ ] Verdict follows the gate rules.
