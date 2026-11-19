---
name: software-test-documentation
description: Use when an automotive SRS or requirements document needs a concise STS with traceable test cases and ordered test procedures.
---

# Software Test Documentation

Create an English STS from the supplied automotive SRS. Use [references/sts-template.md](references/sts-template.md) for the document format and [examples/example-sts.md](examples/example-sts.md) as a completed example.

When an independent agent or reviewer is available, run the STS review workflow in [references/sts-reviewer-checklist.md](references/sts-reviewer-checklist.md) after the first draft.

## STS authoring procedure

1. Read the SRS and preserve its requirement IDs.
2. Identify the behavior, inputs, outputs, limits, states, roles, and error conditions that must be verified.
3. Create one `TC-###` for each testable condition. Put the condition type, test technique, input/trigger, procedure, expected result, evidence, and pass criteria inside the same test case.
4. Order the test cases by prerequisites and execution dependencies.
5. Use explicit numbered steps for setup, action, verification, and cleanup.
6. Give every meaningful step an observable expected result.
7. Provide one traceability summary linking requirements to test cases.
8. Record unclear or conflicting behavior as `ISSUE-###` with the reason a decision is needed, options, recommendation, and testing impact.

## Independent STS Review

After generating the first draft, ask an independent reviewer to compare the SRS and STS without relying on the author's conclusions. The reviewer must check requirement coverage, expected-result correctness, test technique selection, boundary and missing-data conditions, procedure order, duplicate cases, traceability, and unresolved decisions.

The reviewer returns findings with `Must Fix`, `Clarification Needed`, or `Suggestion` status and a location in the STS. Revise the STS for valid findings, then run the review again when a Must Fix finding changes the test design. Include the final review summary and remaining open decisions in the STS handoff.

## Record types

- `REQ-###`: source requirement from the SRS.
- `TC-###`: the complete test unit, including normal tests, boundary tests, invalid-input tests, timing tests, state tests, recovery tests, and additional edge cases.
- `ISSUE-###`: an unresolved requirement or decision that affects testing.

Do not create separate IDs for test conditions, test procedures, or edge cases. An edge case is represented as a `TC-###` with condition type `Additional Edge Case`. If its expected behavior is unclear, link the test case to an `ISSUE-###` and mark it `Decision Needed`.

## Boundaries

- Design tests from requirements; do not inspect implementation code or create automated test code.
- Do not invent an expected result that the SRS does not state or logically require.
- Never omit the test procedure from a test case.
- Keep implementation-derived regression tests for a later STS update.

## Output order

1. One STS traceability summary.
2. Test cases in execution order, each with its complete procedure.
3. Decision-ready issues and additional edge-case test cases.

Use English unless the user requests another language.
