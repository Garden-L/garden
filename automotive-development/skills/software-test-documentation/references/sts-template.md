# Software Test Specification (STS)

This compact template combines the practical parts of a test design specification, test case specification, and test procedure specification. It follows the terminology used by ISO/IEC/IEEE 29119-3 while remaining usable as one Markdown document.

For a compact STS, keep the main reading flow together: one traceability summary first, then test cases in execution order with their procedures, followed by only the additional edge-case and decision items.

## 1. Document control

| Field | Value |
|---|---|
| Document ID | STS-### |
| Title |  |
| System / test item |  |
| SRS reference |  |
| SRS version |  |
| Author |  |
| Reviewer |  |
| Status | Draft / Review / Approved |
| Date |  |

### Revision history

| Version | Date | Author | Change | Approval |
|---|---|---|---|---|

## 2. Purpose and scope

### 2.1 Purpose

### 2.2 In scope

### 2.3 Out of scope

## 3. Test basis and references

| Reference ID | Document | Version / section | Used for |
|---|---|---|---|

## 4. Test item and test boundaries

- Test item:
- Features or requirements covered:
- Interfaces and dependencies:
- Excluded implementation details:

## 5. Assumptions, environment, and test data

- Assumptions:
- Preconditions:
- Environment/configuration:
- Test data:
- Required accounts, roles, or permissions:

## 6. Requirement testability summary

| Requirement | Summary | Testable? | Reason / issue |
|---|---|---|---|
| REQ-001 |  | Yes / Partial / No |  |

## 7. Test strategy and test conditions

| Suite | Test type | Test condition | Rationale | Priority |
|---|---|---|---|---|
| SUITE-001 | Functional |  |  | High |

## 8. Test suites and execution order

| Order | Suite | Prerequisite | Entry condition | Exit condition |
|---|---|---|---|---|
| 1 | SUITE-001 |  |  |  |

## 9. Test procedure and test cases

This section is mandatory. Define the execution order for each suite and the detailed steps for each test case. Do not replace procedure steps with a short narrative.

### 9.1 Test procedure summary

| Suite | Execution order | Preconditions | Completion condition |
|---|---|---:|---|---|
| SUITE-001 | 1 |  |  |

### 9.2 Detailed test case

#### TC-001: [behavior under test]

- Requirement(s): REQ-001
- Suite: SUITE-001
- Execution order: 1
- Objective:
- Priority: Optional; use only when defined by the source SRS or project convention
- Preconditions:
- Test data:

#### Procedure steps

1. **Setup:** [exact preparation action]
   - Expected:
2. **Action:** [exact user/system action]
   - Expected:
3. **Verification:** [exact observation or check]
   - Expected:
4. **Cleanup:** [reset or teardown action]
   - Expected:

- Pass criteria:
- Evidence:
- Notes / assumptions:

### 9.3 Test case classification

Keep the test condition, test technique, and procedure inside each `TC-###`. Do not create separate IDs for conditions, procedures, or edge cases.

| Test case | Requirement | Condition type | Test technique | Input / trigger | Status |
|---|---|---|---|---|---|
| TC-001 | REQ-001 | Boundary | Boundary Value Analysis | 0.0 km/h | Ready |

## 10. Requirements-to-test traceability

| Requirement | Test case condition type(s) | Test case(s) | Coverage status |
|---|---|---|---|
| REQ-001 |  | TC-001 | Covered / Partial / Uncovered |

## 11. Additional edge-case test cases

Create additional edge cases as ordinary `TC-###` records with condition type `Additional Edge Case`. Boundary values, empty or missing values, invalid values, timing, state transition, and recovery tests are also ordinary `TC-###` records with their applicable condition type.

| Test case | Related requirement(s) | Additional condition | Why it is additional | Status | Priority |
|---|---|---|---|---|---|
| TC-### | REQ-001 |  |  | Ready / Decision Needed | Medium |

Use `Clarify` when the SRS does not define the expected result. Do not silently turn an assumption into a passing criterion.

## 12. Decision-ready open items

Use this section for every unresolved requirement, missing expected result, conflicting rule, or decision that changes the test scope. The purpose is to make the item immediately decidable, not merely to record that something is unclear.

| ID | Requirement | Status | Decision needed | Why the decision is needed | Options | Recommended decision | Impact on test scope/procedure | Decision owner | Due date |
|---|---|---|---|---|---|---|---|---|---|
| ISSUE-001 | REQ-001 | Decision Needed |  |  | A / B |  |  |  |  |

### Decision item detail

#### ISSUE-001: [short decision title]

- Requirement reference:
- Current ambiguity or conflict:
- Why this decision is needed now:
- Option A:
- Option B:
- Recommended option and reason:
- Impact if Option A is selected:
- Impact if Option B is selected:
- Tests or procedures affected:
- Decision owner:
- Decision due date:
- Final decision:
- Decision date:

## 13. Open issues and exclusions

| ID | Requirement | Issue / question | Impact | Owner / decision |
|---|---|---|---|---|
| ISSUE-001 | REQ-001 |  |  |  |

## 14. Entry, exit, and pass/fail criteria

- Entry criteria:
- Exit criteria:
- A test passes when:
- A test fails when:
- Evidence required:
- Known exclusions:

## 15. Independent STS review summary

| Review iteration | Reviewer | Verdict | Must Fix | Clarification Needed | Suggestion | Remaining issues |
|---:|---|---|---:|---:|---:|---|
| 1 |  | Approved / Approved with Suggestions / Revision Required | 0 | 0 | 0 |  |

Link detailed findings to the reviewer checklist and record accepted risks or unresolved decisions here.

## Final review checklist

- [ ] Every testable requirement has at least one test condition or is explicitly marked uncovered.
- [ ] Every test case has a requirement link, preconditions, data, numbered steps, expected results, and pass criteria.
- [ ] Every test suite has an execution order and entry/completion condition.
- [ ] Test suites are ordered by prerequisites.
- [ ] Test cases cover applicable normal, boundary, empty/missing, invalid, timing, state, and recovery behavior.
- [ ] Additional edge cases are represented as `TC-###` records with `Additional Edge Case` as the condition type.
- [ ] Every unresolved item explains why a decision is needed and shows its testing impact.
- [ ] Ambiguities and conflicts are listed as decision-ready issues.
- [ ] No implementation-specific behavior was invented.
