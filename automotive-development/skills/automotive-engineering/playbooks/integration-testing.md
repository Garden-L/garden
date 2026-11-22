# Integration Testing

Use when a change must be checked across components, interfaces, build configurations, simulator, ECU, HIL, or vehicle environments.

1. Identify the integrated revision, participating components, configurations, environment, and linked `REQ`/`TC`/`WORK` IDs.
2. Apply `verification` and the automotive `software-test-documentation` profile for applicable procedures and evidence expectations. Do not modify the STS as part of test execution.
3. Confirm setup, calibration, target identity, preconditions, stimulus, observation points, cleanup, and safety controls that are defined by the approved procedure.
4. Run the narrowest integration checks that cover changed interactions, then required regression or target checks.
5. Record actual commands/procedures, revision, environment, logs, expected and observed results, and unavailable checks.
6. When a failure occurs, verify the setup and expectation before assigning cause; route reproducible code defects to [Bug Fix](bug-fix.md).

Output: integration verdict and evidence, with target/HIL/vehicle gaps clearly marked pending or blocked.
