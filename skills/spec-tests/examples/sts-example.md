# Software Test Specification: Personal Notes App

| Field | Value |
| --- | --- |
| Document ID | STS-NOTES-EXAMPLE |
| Version / status | 0.1 / example, not executed |
| Author / reviewer / approver | Example author / not assigned / not assigned |

## 1. Purpose and scope

Verify creation, editing, deletion, and list ordering in the companion [SRS example](../../spec-requirements/examples/srs-example.md). Accounts and synchronization are outside scope.

## 2. Test basis and traceability

| Basis document | Version | Location |
| --- | --- | --- |
| SRS-NOTES-EXAMPLE | 0.1 | [SRS](../../spec-requirements/examples/srs-example.md) |

| Requirement ID | Test case IDs | Coverage / gap |
| --- | --- | --- |
| REQ-001 | TC-001 | Create and reopen a note; empty-title behavior is ISSUE-001 |
| REQ-002 | TC-002 | Edit and reopen a note |
| REQ-003 | TC-003 | Delete a note |
| REQ-004 | TC-004 | Reorder after an update |

## 3. Test environment and data

Use a clean local app instance. For `TC-004`, prepare two notes with distinct titles and bodies. This example specifies tests only; no app instance or test run is supplied.

## 4. Test strategy

Use scenario testing for the user-visible create, edit, and delete flows; use a state transition from initial order to updated order for `REQ-004`. Confirm persisted results by reopening the relevant view. The SRS does not define empty-title behavior, so do not invent a pass criterion for it.

## 5. Test cases and procedures

### TC-001: create a note

**Requirement:** `REQ-001`. **Technique:** scenario testing. **Precondition:** clean app. **Data:** title `First note`, body `Remember this item`.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Create and save the note. | The note is saved. |
| 2 | Open the list and then the note. | The list contains `First note`; the opened body is `Remember this item`. |

**Pass criterion:** both title and body persist. **Evidence plan:** list and reopened-note observations.

### TC-002: edit a note

**Requirement:** `REQ-002`. **Technique:** scenario testing. **Precondition:** an existing note. **Data:** title `Revised note`, body `Updated text`.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Edit the title and body, then save. | The edit is saved. |
| 2 | Return to the list and reopen the note. | `Revised note` and `Updated text` appear. |

**Pass criterion:** both edited values persist. **Evidence plan:** reopened-note observation.

### TC-003: delete a note

**Requirement:** `REQ-003`. **Technique:** scenario testing. **Precondition:** an existing note.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Delete the note. | The deletion action completes. |
| 2 | Return to the list and search for its title. | The note is absent and cannot be reopened from the list. |

**Pass criterion:** the deleted note is unavailable from the list. **Evidence plan:** list observation.

### TC-004: order notes after an update

**Requirement:** `REQ-004`. **Technique:** state transition testing. **Precondition:** clean app. **Data:** notes `Alpha` and `Beta`.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Create `Alpha`, then `Beta`. | Both appear in the list. |
| 2 | Edit and save `Alpha`; return to the list. | `Alpha` appears before `Beta`. |

**Pass criterion:** the updated note moves to the top. **Evidence plan:** list order before and after update.

## 6. Results and unresolved items

| Test case ID | Status | Observed result | Evidence | Issue ID |
| --- | --- | --- | --- | --- |
| TC-001 | Not run | — | — | — |
| TC-002 | Not run | — | — | — |
| TC-003 | Not run | — | — | — |
| TC-004 | Not run | — | — | — |

**ISSUE-001:** The SRS does not specify what happens when the title is empty. Why it matters: a negative-input test would have no supported expected result. The requirement owner must define whether empty titles are accepted or rejected; only then can a corresponding `TC` be added. No execution or passing result is claimed.

## Revision history

| Version | Change | Author |
| --- | --- | --- |
| 0.1 | Initial example | Example author |
