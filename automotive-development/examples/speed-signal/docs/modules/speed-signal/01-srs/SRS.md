# Software Requirements Specification: local speed monitor

| Field | Value |
| --- | --- |
| Document ID | SRS-SPEED-LOCAL |
| Version / status | 1 / illustrative baseline |
| Date | 2026-11-22 |
| Author / reviewer / approver | Example author / no independent agent review / illustrative decision owner only |

## 1. Purpose and scope

This SRS defines the behavior of a small local Python speed monitor, using integer tenths of km/h and integer milliseconds. It demonstrates traceability from [invented source notes](../source.md) through one recorded owner decision. ECU interfaces, bus encoding, HIL, vehicle behavior, safety qualification, and release are out of scope.

## 2. System context

The local test caller sends speed values and time ticks to the monitor and observes its invalid flag. A power-mode caller turns the monitor off and on. No hardware signal or external diagnostic service is modeled.

## 3. Users and scenarios

The test caller supplies valid and invalid speeds, lets time pass without a valid message, observes recovery after valid messages, and switches power off during a pending fault. These scenarios connect to `REQ-001` through `REQ-005`.

## 4. Requirements

| ID | Category | Requirement | Source | Priority | Acceptance condition |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | Functional | While powered on, the monitor shall accept speed values from 0 to 2500 inclusive. | SRC-1 | Must | Both endpoints leave the invalid flag clear. |
| REQ-002 | Functional | While powered on, a received speed below 0 or above 2500 shall set the invalid flag. | SRC-2 | Must | -1 and 2501 each set the flag. |
| REQ-003 | Functional / timing | After a valid speed message while powered on, more than 100 ms without another valid message shall set the invalid flag. | SRC-3 | Must | Clear at 100 ms and set at 101 ms after the last valid message. |
| REQ-004 | Functional / state | After an invalid state, the monitor shall clear the invalid flag only after three consecutive valid speed messages. | SRC-4 | Must | Set after messages one and two; clear after message three. |
| REQ-005 | Functional / power state | On power-off, the monitor shall clear the invalid flag and pending timeout and suspend monitoring until power-on. | [ISSUE-001 decision](issues.md#issue-001--power-off-during-a-timeout) resolving SRC-5 | Must | No timeout while off; after power-on, the next valid message starts a new timeout window. |

## 5. Interfaces and data

The local model accepts an integer `speed_deci_kmh`, integer `now_ms`, `power_off`, and `power_on` operations. Its observable output is a Boolean invalid flag. This is an example API, not a vehicle network interface. `REQ-001` and `REQ-002` define the speed range; `REQ-003` defines time; `REQ-005` defines power-state handling.

## 6. Constraints and assumptions

The example assumes ordered, nondecreasing timestamps and a local caller that invokes time ticks. It does not define scheduling jitter or persistence across a real vehicle power cycle. Those limits are outside this local scope rather than silently interpreted as target requirements.

## 7. Open issues and decisions

[ISSUE-001](issues.md#issue-001--power-off-during-a-timeout) records the missing power-off behavior, alternatives, illustrative owner decision, affected requirements and tests, and local verification. No open issue remains inside the declared local-model scope. A real target would need its own power-state decision and evidence.

## 8. References and glossary

[Source notes](../source.md) are the illustrative input. [STS](../02-sts/STS.md) holds executable procedures. [Traceability](../traceability.md) connects source, requirements, tests, work, code, and evidence. “Invalid flag” is the local model's Boolean validity observation.

## Revision history

| Version | Date | Change | Author |
| --- | --- | --- | --- |
| 1 | 2026-11-22 | Added `REQ-005` after the illustrative `ISSUE-001` decision | Example author |
