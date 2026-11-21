# Independent STS Reviewer Checklist

Use this checklist in a fresh review context with the source SRS and the draft STS. The reviewer checks the artifacts themselves and does not assume that the author's interpretation is correct.

## Review inputs

- Source SRS and version
- Draft STS
- Any approved assumptions or decisions

## Review checks

### Requirements and traceability

- Every testable requirement has at least one linked `TC` or an explained coverage gap.
- Every `TC` links to a valid requirement.
- Requirement IDs, test case IDs, and references are consistent.
- Unclear or conflicting requirements are recorded as `ISSUE` items.

### Test design

- Normal behavior is covered where required.
- Applicable boundary, empty/missing, invalid, timing, state, recovery, interface, and permission conditions are considered.
- The selected test technique matches the requirement and input shape.
- Edge cases with defined expected behavior are executable test cases. Undefined behavior is an issue and coverage gap pending a decision.

### Test procedure

- Each test case has the prerequisites, input/trigger, steps, expected results, pass criteria, and evidence needed for reproduction.
- Setup, action, verification, and cleanup are clear where applicable.
- Steps are executable in the stated order.
- Each meaningful step has an observable expected result.

### Requirements discipline

- Expected results are supported by the SRS or explicitly marked as requiring a decision.
- No implementation-specific behavior has been invented.
- The STS does not claim actual execution or code coverage before implementation and test execution.

## Review output

Return a table with:

| ID | Review status | Location | Finding | Evidence | Recommended action | Status |
|---|---|---|---|---|---|---|
| REV-001 | Must Fix | TC-001 |  |  |  | Open |

Use `Must Fix` for an incorrect or missing requirement, expected result, procedure, or traceability link. Use `Clarification Needed` when the SRS does not define enough information. Use `Suggestion` for clarity, formatting, or consistency improvements.

End with:

- Review verdict: `Approved`, `Approved with Suggestions`, or `Revision Required`
- Count by review status
- Accepted risks or unresolved decisions
- Required follow-up before STS approval
