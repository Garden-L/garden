---
name: architect
description: Use before non-trivial implementation work that crosses module, data, or process boundaries; define ownership, interfaces, and a small design before editing.
---

# Architecture

Use before implementation when the change crosses a boundary or has more than one plausible shape.

1. State the requested outcome and the smallest acceptable change.
2. Trace the callers, inputs, outputs, and owners affected by the change.
3. Sketch two plausible designs when the shape is not obvious.
4. Choose the design with the fewest owners, hidden states, and compatibility layers.
5. Record assumptions, non-goals, and the verification that will prove the design works.

Keep this skill domain-neutral. Leave automotive, web, and safety-specific decisions to the calling project workflow.
