---
name: software-test-documentation
description: Use when an automotive SRS needs traceable test cases and executable test procedures in an STS.
---

# Automotive STS profile

Apply `spec-tests` for general STS principles, ID links, test design techniques, and a reference format. This profile adds [automotive considerations](references/automotive-context.md). The [automotive example](examples/example-sts.md) illustrates vehicle signal, timing, recovery, and open-decision cases; it is not a required layout.

For a module that proceeds through code delivery, write the STS into the project's [module bundle](../../docs/module-deliverables.md). Link unresolved behavior to the canonical `01-srs/issues.md` record and show its coverage gap in `traceability.md`.

Derive test conditions from the SRS while considering relevant vehicle modes, power transitions, signal ranges and validity, timing boundaries, faults, recovery, interfaces, and permissions. Use the test design techniques in `spec-tests` and explain the selected techniques in the STS. Treat edge cases as ordinary `TC` cases when the expected result is supported. If the SRS leaves the result undefined, record an `ISSUE` and the resulting test gap; do not invent a pass criterion.

Describe the actual available target or test environment when known, including configuration, stimulus, observation point, and evidence. Order procedures by real prerequisites. Keep each case executable and linked to its source `REQ` IDs. Do not require a suite hierarchy or fixed document section order merely to satisfy this profile.

Apply `review` for the shared review method, then use the [STS review checklist](references/sts-reviewer-checklist.md) for test-specific checks against the SRS. Resolve supported findings and report remaining decisions or coverage gaps without claiming execution that has not happened. Use a fresh independent review context for substantial or consequential STSs when available; otherwise label the review as self-review.
