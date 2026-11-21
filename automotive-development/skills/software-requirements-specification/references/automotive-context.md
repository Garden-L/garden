# Automotive SRS considerations

Use the shared `spec-requirements` [format](../../../../skills/spec-requirements/formats/srs.md) only as a structural example. The SRS may use prose, lists, tables, or diagrams as needed.

- Preserve the original source sentence, source location, or source ID for each derived `REQ` so changes can be checked against the input.
- Describe vehicle operating conditions only when they affect the requirement: parked/driving, ignition or power mode, signal validity, timing, faults, and recovery are common examples.
- Separate supplied requirements from assumptions and open decisions. When two sources conflict, identify both and leave the resulting behavior open until resolved.
- For standards or external documents, record the applicable version and provision. Check cited material before claiming that a requirement is covered.
- Add a Mermaid or other flow only when a condition, sequence, or state change becomes clearer through a diagram. Keep unknown branches visibly open and connect relevant `REQ` IDs.
- Keep requirement-level acceptance conditions in the SRS. Put setup, procedure, and evidence details in the STS.

See the [automotive SRS example](example.md) for one possible presentation.
