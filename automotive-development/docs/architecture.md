# Package architecture

`automotive-development` has three layers:

```text
automotive-development/skills/automotive-engineering/SKILL.md
        ↓ selects and coordinates
automotive-development/skills/automotive-engineering/playbooks/*.md
        ↓ reads only the named skills
skills/* + automotive-development/skills/*
```

The engineering skill owns request classification and workflow selection. Its co-located `playbooks/` directory owns stage sequencing, inputs, and outputs. Small leaf skills own one reusable behavior or one automotive-specific artifact. Top-level skills must remain domain-neutral.

The current automotive pipeline remains available as a leaf skill for compatibility. New playbooks may compose its rules, but must not silently bypass approval, baseline, or traceability gates.
