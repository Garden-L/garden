# Package architecture

`automotive-development` has three layers:

```text
automotive-development/skills/automotive-engineering/SKILL.md
        ↓ selects and coordinates
automotive-development/skills/automotive-engineering/playbooks/*.md
        ↓ resolves names through the central skill registry and reads only those needed
skills/* + automotive-development/skills/*
```

The engineering skill owns request classification and workflow selection. Its co-located `playbooks/` directory owns stage sequencing, inputs, and outputs. Shared skills own reusable SRS/STS principles and reference formats; automotive leaf skills add vehicle context, applicable sources, target considerations, and lifecycle gates.

The current automotive pipeline remains available as a leaf skill for compatibility. New playbooks may compose its rules, but must not silently bypass approval, baseline, or traceability gates.
