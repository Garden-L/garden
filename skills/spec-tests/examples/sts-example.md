# Example STS: Personal Notes App

This STS verifies the companion [SRS example](../../spec-requirements/examples/srs-example.md). The test cases use its requirement IDs.

## 1. Document information

- Version: 0.1
- Status: Example

## 2. Purpose and scope

Verify note creation, editing, deletion, and list ordering. Multi-user behavior and synchronization are out of scope.

## 3. Test basis and traceability

| Requirement | Test case | Coverage |
| --- | --- | --- |
| REQ-001 | TC-001 | Create and retrieve a note |
| REQ-002 | TC-002 | Edit and retrieve a note |
| REQ-003 | TC-003 | Delete a note |
| REQ-004 | TC-004 | Order notes after update |

## 4. Test environment and data

- A clean local app instance
- Two notes with distinct titles and bodies for ordering tests

## 5. Test strategy

Exercise each requirement through the user-visible application behavior. Confirm persisted results by reopening the relevant view.

## 6. Test cases and procedures

### TC-001 — Create a note (REQ-001)

1. Create a note with title `First note` and body `Remember this item`.
2. Save the note and open the note list.

**Expected result:** The list contains `First note`; opening it shows `Remember this item`.

### TC-002 — Edit a note (REQ-002)

1. Open an existing note and change its title to `Revised note` and body to `Updated text`.
2. Save, return to the list, and reopen the note.

**Expected result:** The reopened note shows `Revised note` and `Updated text`.

### TC-003 — Delete a note (REQ-003)

1. Delete an existing note from the app.
2. Return to the note list and search for its title.

**Expected result:** The note is absent and cannot be reopened from the list.

### TC-004 — Order notes by most recent update (REQ-004)

1. Create notes `Alpha` and `Beta` in that order.
2. Edit and save `Alpha`.
3. Return to the note list.

**Expected result:** `Alpha` appears before `Beta`.

## 7. Results and unresolved items

Record each case as passed, failed, blocked, or not run, with the observed result and evidence. No unresolved items are supplied in this example.
