# Automotive STS considerations

Use the shared `spec-tests` [format](../../skills/spec-tests/formats/sts.md) only as a structural example. The STS may use prose, lists, tables, or diagrams as needed.

- Derive test conditions from the relevant vehicle state, ignition or power mode, signal range and validity, timeout, fault, recovery, interface, and permission rules in the SRS. Do not assume every category applies.
- Apply suitable design techniques, such as boundary value analysis for numeric or timing limits and state transition testing for mode or fault recovery. Explain the selection near the relevant requirements or cases.
- For each executable `TC`, identify the source `REQ`, initial vehicle or system state, stimulus and data, observable response, pass criterion, and evidence. Include ordered steps when execution depends on sequence.
- State the actual environment and observation point if known (for example simulator, bench, ECU, or HIL). If unavailable, mark the environmental assumption or gap instead of inventing hardware or tooling.
- Treat a supported edge case as another `TC`. When expected behavior is undefined, record an `ISSUE` and affected coverage rather than assigning a passing result.
- Preserve SRS version and `REQ` → `TC` traceability. Keep execution results separate from planned tests until the tests have run.

See the [automotive STS example](automotive-sts-example.md) for one possible presentation.
