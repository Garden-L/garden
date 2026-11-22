# Implementation report

**Work item:** [WORK-001](WORK-001.md). **Baseline:** [SRS](../01-srs/SRS.md), [STS](../02-sts/STS.md), [ISSUE-001](../01-srs/issues.md). **Result:** local implementation complete and five local tests passed.

## Changes

- Implemented range acceptance, invalid values, strict timeout, three-message recovery, and the decided local power-off reset in [speed_signal.py](../../../../src/speed_signal.py).
- Added behavior tests for `TC-001` through `TC-005` in [test_speed_signal.py](../../../../tests/test_speed_signal.py).
- No ECU integration, production code, commit, or MR is included in this example.

## Checks

Command from the example root: `python3 -m unittest discover -s tests -v`.

**Observed:** 5 tests passed. See [captured output](../05-verification/evidence/unittest-2026-11-22.txt). This is a local example run only.

## Deviations and remaining work

No deviation from `WORK-001` in the local example. ECU/HIL adaptation, physical timing, diagnostics, safety, and release work are not represented or verified.
