---
name: spec-tests
description: Use when creating or revising a software test specification with an STS format and example.
---

# Test Specification

Apply `specification` when developing the tests. Use the [STS format](formats/sts.md) as a reference for possible document structure and the [worked example](examples/sts-example.md) as an illustration. Write the document in the form that makes the tests easiest to understand, run, and assess.

## IDs and traceability

- `TC-<id>` identifies a test case.
- `REQ-<id>` identifies its source requirement; link each case to the requirements it tests.
- `ISSUE-<id>` identifies unresolved behavior or a problem found during testing.

Keep IDs unique and stable. Preserve existing IDs when revising the document. Show the SRS version, `REQ` → `TC` coverage, and any gaps.

## Test design

Choose techniques based on the requirement: equivalence partitioning and boundary value analysis for ranges, decision tables or combination testing for interacting conditions, state transition testing for changes of state, scenario testing for workflows, and error guessing for likely failures. Explain in the STS which techniques were used and why, with links to the relevant `REQ` and `TC` IDs. Record a meaningful gap or reason when a relevant technique cannot be applied. Do not invent expected behavior; link an `ISSUE` when the requirement leaves it unresolved.

Give each test enough preconditions, data, steps, expected results, pass criteria, and evidence for another person to reproduce and assess it. Record observed results and evidence when tests are run.

Domain-specific test environments, techniques, standards, and approval rules belong in the calling domain profile.
