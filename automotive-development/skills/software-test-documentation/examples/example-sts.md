# Example STS: Vehicle Speed Signal Validation

This example assumes the following SRS requirements:

| ID | Requirement |
|---|---|
| REQ-001 | The system shall accept a vehicle speed signal from 0 to 250 km/h in increments of 0.1 km/h. |
| REQ-002 | The system shall set `SpeedSignalInvalid` when the received speed is below 0 km/h or above 250 km/h. |
| REQ-003 | The system shall set `SpeedSignalInvalid` when no valid speed signal is received for more than 100 ms. |
| REQ-004 | The system shall clear `SpeedSignalInvalid` after three consecutive valid messages are received. |

## 1. STS traceability summary

| Order | Requirement | Condition type | Test technique | Test case | Status |
|---:|---|---|---|---|---|---|
| 1 | REQ-001 | Boundary: minimum valid value, `0.0 km/h` | Boundary Value Analysis | TC-001 | Ready |
| 2 | REQ-001 | Boundary: maximum valid value, `250.0 km/h` | Boundary Value Analysis | TC-002 | Ready |
| 3 | REQ-002 | Invalid: above maximum, `250.1 km/h` | Equivalence Partitioning | TC-003 | Ready |
| 4 | REQ-003 | Timing/Timeout: no message for more than `100 ms` | Boundary Value Analysis | TC-004 | Ready |
| 5 | REQ-004 | State Transition: three valid messages after fault | State Transition Testing | TC-005 | Ready |
| 6 | REQ-001, REQ-003 | Shutdown during timeout; expected behavior undefined | Risk-based analysis | ISSUE-001; test gap | Decision Needed |

## 2. Test cases and procedures

### TC-001: Accept the minimum valid speed

- Requirement: REQ-001
- Test condition: Minimum valid value, `0.0 km/h`
- Test technique: Boundary Value Analysis
- Execution order: 1
- Priority: High
- Preconditions: Speed monitoring is enabled and the signal channel is available.

#### Procedure

1. Send a speed message with value `0.0 km/h`.
   - Expected: The message is accepted.
2. Observe `SpeedSignalInvalid`.
   - Expected: `SpeedSignalInvalid` remains cleared.
3. Read the recorded speed value.
   - Expected: The recorded value is `0.0 km/h`.

- Pass criteria: All expected results are observed.
- Evidence: Input message, status trace, and recorded value.

### TC-002: Accept the maximum valid speed

- Requirement: REQ-001
- Test condition: Maximum valid value, `250.0 km/h`
- Test technique: Boundary Value Analysis
- Execution order: 2
- Priority: High
- Preconditions: Speed monitoring is enabled and the signal channel is available.

#### Procedure

1. Send a speed message with value `250.0 km/h`.
   - Expected: The message is accepted.
2. Observe `SpeedSignalInvalid`.
   - Expected: `SpeedSignalInvalid` remains cleared.

- Pass criteria: The maximum valid value is accepted without an invalid status.
- Evidence: Input message and status trace.

### TC-003: Reject a value above the maximum limit

- Requirement: REQ-002
- Test condition: Invalid value, `250.1 km/h`
- Test technique: Equivalence Partitioning and Boundary Value Analysis
- Execution order: 3
- Priority: High
- Preconditions: Speed monitoring is enabled.

#### Procedure

1. Send a speed message with value `250.1 km/h`.
   - Expected: The value is identified as out of range.
2. Observe `SpeedSignalInvalid`.
   - Expected: `SpeedSignalInvalid` is set.

- Pass criteria: The invalid status is set for the out-of-range value.
- Evidence: Input message and diagnostic status trace.

### TC-004: Set invalid status after signal timeout

- Requirement: REQ-003
- Test condition: No valid signal for more than `100 ms`
- Test technique: Boundary Value Analysis and Timing Analysis
- Execution order: 4
- Priority: Critical
- Preconditions: A valid speed message has been received and monitoring is active.

#### Procedure

1. Stop sending speed messages.
   - Expected: No new speed message is received.
2. Wait until the signal absence exceeds `100 ms`.
   - Expected: The timeout threshold is exceeded.
3. Observe `SpeedSignalInvalid`.
   - Expected: `SpeedSignalInvalid` is set.

- Pass criteria: The invalid status is set after the specified timeout.
- Evidence: Timestamped message trace and status trace.

### TC-005: Clear invalid status after signal recovery

- Requirement: REQ-004
- Test condition: Three consecutive valid messages after an invalid state
- Test technique: State Transition Testing
- Execution order: 5
- Priority: Critical
- Preconditions: `SpeedSignalInvalid` is set.

#### Procedure

1. Send the first valid speed message.
   - Expected: The message is accepted and `SpeedSignalInvalid` remains set.
2. Send the second consecutive valid speed message.
   - Expected: The message is accepted and `SpeedSignalInvalid` remains set.
3. Send the third consecutive valid speed message.
   - Expected: `SpeedSignalInvalid` is cleared.

- Pass criteria: The invalid status is cleared only after three consecutive valid messages.
- Evidence: Three input messages and status trace after each message.

## 3. Open decision and test gap

### ISSUE-001: Vehicle shutdown during signal timeout

- Related requirements: REQ-001, REQ-003
- Condition: Vehicle shutdown occurs while the signal timeout is active.
- Gap: The supplied SRS defines signal timeout behavior but does not define how shutdown state interacts with it, so there is no executable `TC` yet.
- Status: Decision Needed
- Recommended decision: Define whether shutdown suppresses the timeout diagnostic or preserves it.
- Testing impact: Add a dedicated `TC` after the shutdown interaction rule is approved.
