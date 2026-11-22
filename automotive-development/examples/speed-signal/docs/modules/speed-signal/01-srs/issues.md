# Speed signal issues and decisions

This is the authoritative issue record for the example. The SRS, STS, work packet, and traceability map link here rather than repeating the decision rationale.

## ISSUE-001 — power-off during a timeout

**Status:** `Verified` for the local model. **Observed gap:** `SRC-1` through `SRC-4` do not define whether the invalid flag and pending timeout survive power-off. **Why it matters:** two plausible behaviors produce different SRS acceptance conditions, test oracles, and code states; choosing silently could make a test pass for the wrong reason.

**Options:** A: clear the flag and pending timeout on power-off, then restart monitoring after power-on; simple local reset but discards a prior fault state. B: retain the flag and pending timeout across power-off; preserves fault history but requires defined persistence and clock behavior. **Recommendation:** A for this illustrative local model, because persistence is not otherwise in scope. A real vehicle owner would need to decide the applicable power-state and diagnostic behavior.

**Illustrative decision:** Example module owner chose A on 2026-11-22 for this local example only. The earlier gap remains visible in [source notes](../source.md). **Applied to:** [REQ-005](SRS.md), [TC-005](../02-sts/STS.md), [WORK-001](../04-implementation/WORK-001.md), [implementation](../../../../src/speed_signal.py). This is a pre-baseline example decision; if it had changed an approved SRS/STS, the automotive baseline-change workflow would apply.

**Verification:** [test_TC_005](../../../../tests/test_speed_signal.py) passed in the [local test run](../05-verification/evidence/unittest-2026-11-22.txt), as assessed in [verification.md](../05-verification/verification.md). **Remaining limit:** no ECU, HIL, or vehicle power-state evidence. The issue is verified only within the declared local-model scope.
