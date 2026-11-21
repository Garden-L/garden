---
name: software-test-documentation
description: Use when an automotive SRS needs traceable test cases and executable test procedures in an STS.
---

# Automotive STS profile

Apply `spec-tests` for general STS principles, ID links, test design techniques, and a reference format. This profile adds [automotive considerations](references/automotive-context.md). The [automotive example](examples/example-sts.md) illustrates vehicle signal, timing, recovery, and open-decision cases; it is not a required layout.

Derive test conditions from the SRS while considering relevant vehicle modes, power transitions, signal ranges and validity, timing boundaries, faults, recovery, interfaces, and permissions. Use the test design techniques in `spec-tests` and explain the selected techniques in the STS. Treat edge cases as ordinary `TC` cases when the expected result is supported. If the SRS leaves the result undefined, record an `ISSUE` and the resulting test gap; do not invent a pass criterion.

Describe the actual available target or test environment when known, including configuration, stimulus, observation point, and evidence. Order procedures by real prerequisites. Keep each case executable and linked to its source `REQ` IDs. Do not require a suite hierarchy or fixed document section order merely to satisfy this profile.

When independent review is available, use the [STS review brief](references/sts-reviewer-checklist.md) to check the draft against the SRS. Resolve supported findings and report remaining decisions or coverage gaps without claiming execution that has not happened.
