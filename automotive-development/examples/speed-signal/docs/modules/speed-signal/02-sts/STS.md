# Software Test Specification: local speed monitor

| Field | Value |
| --- | --- |
| Document ID | STS-SPEED-LOCAL |
| Version / status | 1 / locally executed example |
| Date | 2026-11-22 |
| Author / reviewer / approver | Example author / no independent agent review / illustrative decision owner only |

## 1. Purpose and scope

Verify the local Python model against [SRS revision 1](../01-srs/SRS.md). ECU, HIL, vehicle, safety, and release verification are outside this STS. The [verification record](../05-verification/verification.md) assesses the executed results; this document defines the cases and their expected behavior.

## 2. Test basis and traceability

| Basis document | Version | Location |
| --- | --- | --- |
| SRS-SPEED-LOCAL | 1 | [srs.md](../01-srs/SRS.md) |

| Requirement ID | Test case IDs | Coverage / gap |
| --- | --- | --- |
| REQ-001 | TC-001 | Both inclusive speed endpoints |
| REQ-002 | TC-002 | Adjacent invalid partitions |
| REQ-003 | TC-003 | 100/101 ms timeout boundary |
| REQ-004 | TC-004 | Three-message recovery transition |
| REQ-005 | TC-005 | Power-off decision from [ISSUE-001](../01-srs/issues.md#issue-001--power-off-during-a-timeout) |

## 3. Test environment and data

The test item is [speed_signal.py](../../../../src/speed_signal.py), driven by [test_speed_signal.py](../../../../tests/test_speed_signal.py) under local Python 3 `unittest`. Speed data is integer tenths of km/h; time data is integer ms. Each test starts with a fresh powered-on monitor. No physical ECU or bus stimulus is used.

## 4. Test strategy

Use boundary value analysis for the inclusive range and strict timeout, equivalence partitioning for invalid speed, and state transition testing for recovery and power mode. Run the five independent cases with `python3 -m unittest discover -s tests -v` from the example root. A case passes when its asserted observations match the expected results below. Retain the [run log](../05-verification/evidence/unittest-2026-11-22.txt). The method does not assess physical timing accuracy or target integration.

## 5. Test cases and procedures

### TC-001: valid speed endpoints

**Requirement:** `REQ-001`. **Technique:** boundary value analysis. **Precondition:** fresh powered-on monitor with clear invalid flag. **Data:** 0 and 2500.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Send speed 0 at 0 ms; inspect invalid flag. | Flag remains clear. |
| 2 | Send speed 2500 at 1 ms; inspect invalid flag. | Flag remains clear. |

**Pass criterion:** both endpoint observations are clear. **Evidence:** [test_TC_001](../../../../tests/test_speed_signal.py) and [run log](../05-verification/evidence/unittest-2026-11-22.txt).

### TC-002: speeds just outside the range

**Requirement:** `REQ-002`. **Technique:** equivalence partitioning and boundary value analysis. **Precondition:** a fresh powered-on monitor for each value. **Data:** -1 and 2501.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Send -1 at 0 ms; inspect invalid flag. | Flag is set. |
| 2 | Reset the monitor; send 2501 at 0 ms; inspect invalid flag. | Flag is set. |

**Pass criterion:** both invalid partitions set the flag. **Evidence:** [test_TC_002](../../../../tests/test_speed_signal.py) and [run log](../05-verification/evidence/unittest-2026-11-22.txt).

### TC-003: strict timeout boundary

**Requirement:** `REQ-003`. **Technique:** boundary value analysis. **Precondition:** fresh powered-on monitor. **Data:** valid speed 100, ticks at 100 and 101 ms.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Receive speed 100 at 0 ms. | Flag is clear. |
| 2 | Tick at 100 ms; inspect flag. | Flag remains clear. |
| 3 | Tick at 101 ms; inspect flag. | Flag is set. |

**Pass criterion:** transition occurs only after 100 ms. **Evidence:** [test_TC_003](../../../../tests/test_speed_signal.py) and [run log](../05-verification/evidence/unittest-2026-11-22.txt).

### TC-004: recovery after three valid messages

**Requirement:** `REQ-004`. **Technique:** state transition testing. **Precondition:** invalid flag set by sending -1. **Data:** valid speed 100 at 1, 2, and 3 ms.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Send first valid message; inspect flag. | Flag remains set. |
| 2 | Send second consecutive valid message; inspect flag. | Flag remains set. |
| 3 | Send third consecutive valid message; inspect flag. | Flag clears. |

**Pass criterion:** flag clears only after the third message. **Evidence:** [test_TC_004](../../../../tests/test_speed_signal.py) and [run log](../05-verification/evidence/unittest-2026-11-22.txt).

### TC-005: power-off during timeout

**Requirement:** `REQ-005`, originating from [ISSUE-001](../01-srs/issues.md#issue-001--power-off-during-a-timeout). **Technique:** state transition testing across power modes and a timeout boundary. **Precondition:** fresh powered-on monitor. **Data:** valid speed 100; times 0, 101, 500, 501, and 601 ms.

| Step | Action | Expected result |
| --- | --- | --- |
| 1 | Receive speed 100 at 0 ms; tick at 101 ms. | Flag is set by timeout. |
| 2 | Power off; inspect flag. | Flag clears. |
| 3 | Tick at 500 ms while off; inspect flag. | Flag stays clear. |
| 4 | Power on, receive speed 100 at 501 ms, tick at 601 ms. | Flag remains clear at the new 100 ms boundary. |

**Pass criterion:** all four observations match `REQ-005`. **Evidence:** [test_TC_005](../../../../tests/test_speed_signal.py) and [run log](../05-verification/evidence/unittest-2026-11-22.txt).

## 6. Results and unresolved items

| Test case ID | Status | Observed result | Evidence | Issue ID |
| --- | --- | --- | --- | --- |
| TC-001 | Pass | Both endpoints clear | [local log](../05-verification/evidence/unittest-2026-11-22.txt) | — |
| TC-002 | Pass | Both invalid values set flag | [local log](../05-verification/evidence/unittest-2026-11-22.txt) | — |
| TC-003 | Pass | Clear at 100 ms; set at 101 ms | [local log](../05-verification/evidence/unittest-2026-11-22.txt) | — |
| TC-004 | Pass | Clear after third valid message | [local log](../05-verification/evidence/unittest-2026-11-22.txt) | — |
| TC-005 | Pass | Power-off clears and suspends timeout | [local log](../05-verification/evidence/unittest-2026-11-22.txt) | [ISSUE-001](../01-srs/issues.md#issue-001--power-off-during-a-timeout), verified locally |

No unresolved issue remains inside the local-model scope. Target-environment testing remains outside scope; see [verification.md](../05-verification/verification.md).

## Revision history

| Version | Date | Change | Author |
| --- | --- | --- | --- |
| 1 | 2026-11-22 | Added `TC-005` after illustrative `ISSUE-001` decision and recorded local run | Example author |
