# SRS to STS

Use when an automotive SRS must become a testable STS.

1. Confirm the SRS revision, scope, and open decisions.
2. Apply `spec-tests` to make each case traceable and its expected result observable. Choose techniques that fit the requirement, such as boundaries for ranges and timing, decision tables for interacting conditions, and state transitions for modes and recovery. Use the [automotive STS context](../references/automotive-sts-context.md) to select relevant vehicle state, power mode, signal range/validity, timing, fault, recovery, interface, and permission conditions.
3. Give every test case an observable expected result supported by the SRS or an approved decision. For undefined behavior, link an `ISSUE` and show the coverage gap rather than inventing a pass condition.
4. State the actual environment, stimulus, observation point, and evidence when known. Keep planned checks separate from executed results and mark unavailable ECU/HIL/vehicle environments as gaps.
5. Apply shared `review` and check the SRS-to-STS mapping, test boundaries, procedure order, expected results, and decision-linked gaps using the [STS reviewer checklist](../references/sts-reviewer-checklist.md).
6. Apply `verification` before reporting coverage; do not claim test execution or target evidence that has not occurred.

Output: an STS with traceable test cases, justified design techniques, executable procedures, and explicit test gaps. Use English unless the project requests another language. The shared STS format is a reference, not a required layout; the [automotive example](../references/automotive-sts-example.md) is illustrative.
