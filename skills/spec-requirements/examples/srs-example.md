# Example SRS: Personal Notes App

## 1. Document information

- Version: 0.1
- Status: Example

## 2. Purpose and scope

This SRS defines basic note creation, editing, listing, and deletion for a single-user personal notes app. Account management and synchronization across devices are out of scope.

## 3. System context

The user interacts with the app through its interface. The app stores notes locally on the user's device.

## 4. Users and scenarios

The user creates a note, later finds and edits it, or removes it when it is no longer needed.

## 5. Functional requirements

| ID | Requirement | Source | Priority | Acceptance condition |
| --- | --- | --- | --- | --- |
| REQ-001 | The app shall create a note with a title and body supplied by the user. | Example stakeholder need | Must | After saving, the note appears in the note list with the supplied title and body. |
| REQ-002 | The app shall allow the user to edit the title and body of an existing note. | Example stakeholder need | Must | After saving an edit, reopening the note shows the updated title and body. |
| REQ-003 | The app shall allow the user to delete an existing note. | Example stakeholder need | Must | After deletion, the note no longer appears in the note list and cannot be reopened from that list. |
| REQ-004 | The app shall show notes in a list ordered by most recently updated first. | Example stakeholder need | Should | Updating a note moves it to the top of the list. |

## 6. Quality requirements

No quality requirements were supplied for this example.

## 7. Interfaces and data

Each note has a title and body. Account, export, and synchronization interfaces are out of scope.

## 8. Constraints and assumptions

- Notes are stored on the current device.
- The example assumes one user and one local collection.

## 9. Open issues and decisions

No open issues in this example.

## 10. References and glossary

No external references. A **note** is one user-authored title-and-body item.
