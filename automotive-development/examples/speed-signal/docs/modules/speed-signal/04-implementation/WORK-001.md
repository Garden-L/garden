# WORK-001 — local speed monitor

**Baseline:** [SRS revision 1](../01-srs/SRS.md), [STS revision 1](../02-sts/STS.md), [ISSUE-001 decision](../01-srs/issues.md#issue-001--power-off-during-a-timeout). **Status:** local implementation and tests verified. **Owner:** illustrative module implementer. **Revision:** this example package; no specific commit SHA or MR is claimed.

**Scope:** implement `REQ-001` through `REQ-005` and the matching `TC-001` through `TC-005` in a small Python model. **Allowed files:** `src/speed_signal.py`, `tests/test_speed_signal.py`, and this example's documentation. **Out of scope:** ECU interfaces, bus encoding, hardware timing, safety qualification, production release.

**Dependencies and decisions:** `ISSUE-001` is decided for the local model before `REQ-005` and `TC-005` are implemented. The code uses integer tenths of km/h and integer milliseconds from the SRS. No additional public interface or schema is changed.

**Implementation:** [source code](../../../../src/speed_signal.py) and [unit tests](../../../../tests/test_speed_signal.py). **Check command:** `python3 -m unittest discover -s tests -v` from the example root. **Acceptance:** all five linked cases pass. **Observed result:** five tests passed; see the [captured log](../05-verification/evidence/unittest-2026-11-22.txt) and [verification](../05-verification/verification.md).

**Rollback:** remove this illustrative module only; there is no target ECU integration or deployed artifact. **Delivery gate:** no push, MR, merge, or release is claimed by this example.
