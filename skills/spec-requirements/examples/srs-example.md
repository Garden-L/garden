# Software Requirements Specification: Personal Notes App

| Field | Value |
| --- | --- |
| Document ID | SRS-NOTES-EXAMPLE |
| Version / status | 0.1 / example |
| Author / reviewer / approver | Example author / not assigned / not assigned |

## 1. Purpose and scope

This SRS defines note creation, editing, listing, and deletion for one user's local notes app. Accounts and synchronization across devices are outside scope.

## 2. System context

The user interacts with the app's interface. The app stores notes locally on the user's device; no external service is required.

## 3. Users and scenarios

The user creates a note (`REQ-001`), finds and edits it (`REQ-002`), removes it (`REQ-003`), or views notes ordered by recent updates (`REQ-004`).

## 4. Requirements

| ID | Category | Requirement | Source | Priority | Acceptance condition |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | Functional | The app shall create a note with a title and body supplied by the user. | Example stakeholder need | Must | After saving, the note appears in the list with the supplied title and body. |
| REQ-002 | Functional | The app shall allow the user to edit an existing note's title and body. | Example stakeholder need | Must | Reopening the saved note shows the updated title and body. |
| REQ-003 | Functional | The app shall allow the user to delete an existing note. | Example stakeholder need | Must | After deletion, the note is absent from the list and cannot be reopened there. |
| REQ-004 | Functional | The app shall list notes in most recently updated order. | Example stakeholder need | Should | Updating a note moves it to the top of the list. |

No quality requirement was supplied for this example.

## 5. Interfaces and data

Each note has a title and body stored locally. Account, export, and synchronization interfaces are outside scope. `REQ-001` through `REQ-004` use this note data.

## 6. Constraints and assumptions

Notes are stored on the current device. The example assumes one user and one local collection.

## 7. Open issues and decisions

No open issue or decision is supplied in this example.

## 8. References and glossary

There are no external references. A **note** is one user-authored title-and-body item. The matching [STS example](../../spec-tests/examples/sts-example.md) links its test cases to these `REQ` IDs.

## Revision history

| Version | Change |
| --- | --- |
| 0.1 | Initial example |
