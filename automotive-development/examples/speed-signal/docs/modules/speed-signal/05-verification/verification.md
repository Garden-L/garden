# Speed signal verification — local example

**Claim under review:** the local Python model implements [REQ-001 to REQ-005](../01-srs/SRS.md) and behaves as the five [STS cases](../02-sts/STS.md) describe. This is not a claim about ECU, HIL, vehicle, safety, or release behavior.

**Environment:** local Python 3, `unittest`; source and tests in this example. **Command:** `python3 -m unittest discover -s tests -v` from `automotive-development/examples/speed-signal/`. **Observed result:** five tests ran and passed. The [captured output](evidence/unittest-2026-11-22.txt) is the evidence for this run.

| Requirement | Test | Status | Observation | Evidence |
| --- | --- | --- | --- | --- |
| REQ-001 | TC-001 | Pass | Both valid endpoints kept the flag clear | [test and log](evidence/unittest-2026-11-22.txt) |
| REQ-002 | TC-002 | Pass | Both adjacent invalid values set the flag | [test and log](evidence/unittest-2026-11-22.txt) |
| REQ-003 | TC-003 | Pass | Flag clear at 100 ms, set at 101 ms | [test and log](evidence/unittest-2026-11-22.txt) |
| REQ-004 | TC-004 | Pass | Cleared only after the third valid message | [test and log](evidence/unittest-2026-11-22.txt) |
| REQ-005 | TC-005 | Pass | Power-off cleared state and suspended timeout | [test and log](evidence/unittest-2026-11-22.txt) |

**Decision check:** [ISSUE-001](../01-srs/issues.md#issue-001--power-off-during-a-timeout) has a recorded illustrative owner choice, updated SRS and STS links, implementation, and a passing local test. Its `Verified` state is limited to the local model.

**Conclusion:** `Verified` for the declared local example scope. **Outside observation:** ECU, HIL, vehicle integration, physical timing accuracy, diagnostics persistence, safety, and release. None has been run or approved. A production module would need its own source decisions and target-environment evidence before claiming those outcomes.
