---
name: verification
description: Use before making a claim about a result to examine the actual result and the evidence that supports the claim.
---

# Verification

Verification checks whether a real result meets an explicit expectation under stated conditions. A check that uses the wrong build, setup, input, or environment can produce a convincing but false conclusion.

## How to verify

1. **Set up the real case.** Identify the behavior to check, expected result, build or artifact revision, environment, starting state, and input data. Use the intended target when available; name any stand-in and its differences.
2. **Run the check as specified.** Follow the procedure in order. Confirm preconditions, observe important intermediate states as well as the final result, and retain the actual output or trace. A command exit code alone may not prove the behavior.
3. **Cover the affected behavior.** Run the normal case and the relevant boundary, invalid-input, error, or state-transition cases. Choose cases based on the change and its risks; do not add unrelated coverage for appearance.
4. **Compare expected with actual.** Record the exact difference. If a check fails, repeat it with the same revision and conditions, then inspect the setup and expected result before blaming the artifact. Change one condition at a time when isolating the cause.
5. **Check the correction.** After a change, rerun the failed case and the relevant regression checks. Do not weaken the expected result just to make the check pass.
6. **Limit the conclusion.** Report pass, fail, or inconclusive for the conditions actually checked. Name important cases or environments that remain unverified.

## When a result is unclear

- If the expected behavior is missing or contradictory, the result is **inconclusive** until the expectation is clarified.
- If the procedure, data, setup, or expected result is wrong, correct the check and rerun it; the run does not establish an artifact defect.
- If the expectation and check are sound and the same mismatch reproduces, report the artifact as failing that expectation.
- If the required target is unavailable, report the target claim as unverified even when a local or simulated run passes.

## Record the evidence

State the artifact revision and environment, setup and inputs, command or procedure, expected result, actual result, evidence location, and conclusion. Explain why a mismatch matters in terms of the affected behavior or decision. Separate what the evidence shows from any suspected cause, and say what remains unknown.

**Example:** If a timeout test fails at 100 ms but the procedure may have advanced to 101 ms, inspect the timestamp trace and repeat at the specified boundary before changing code. A reproducible mismatch at 100 ms against a clear expectation supports an artifact failure; an incorrect timestamp means the check must be corrected first.
