# Illustrative source notes: speed signal

These are invented inputs for teaching the workflow. They are not an automotive standard or a real stakeholder approval.

- `SRC-1`: Accept integer speed values from 0 to 2500 tenths of km/h, inclusive.
- `SRC-2`: Set the invalid flag for any received value outside that range.
- `SRC-3`: After a valid message, set the invalid flag if no subsequent valid message arrives for more than 100 ms.
- `SRC-4`: After an invalid state, clear it only after three consecutive valid messages.
- `SRC-5`: The original notes do not say what power-off does to a pending timeout or invalid flag. This is [ISSUE-001](01-srs/issues.md#issue-001--power-off-during-a-timeout). The illustrative owner decision is recorded there and becomes `REQ-005`.

The required target for this example is a local Python model. Behavior on an ECU, HIL bench, or vehicle is not specified or verified here.
