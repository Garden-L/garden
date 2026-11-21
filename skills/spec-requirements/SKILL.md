---
name: spec-requirements
description: Use when creating or revising a software requirements specification with an SRS format and example.
---

# Requirements Specification

Apply `specification` when developing the requirements. Use the [SRS format](formats/srs.md) as a reference for possible document structure and the [worked example](examples/srs-example.md) as an illustration. Write the document in the form that makes its requirements easiest to understand and trace.

## IDs

- `REQ-<id>` identifies a functional or quality requirement.
- `ISSUE-<id>` identifies an unresolved question or problem.

Keep IDs unique and stable. Preserve existing IDs when revising the document.

## Requirements

State one verifiable obligation per `REQ`. Make its source and observable acceptance condition clear; include priority when it helps decisions. Connect relevant scenarios, interfaces, constraints, and issues by ID. Keep detailed test procedures in the STS.

Domain-specific terminology, standards, and approval rules belong in the calling domain profile.
