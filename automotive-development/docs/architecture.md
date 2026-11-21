# Package architecture

`automotive-development` has three layers:

```text
automotive-development/skills/automotive-development-pipeline/SKILL.md
        ↓ selects and coordinates
automotive-development/playbooks/*.md
        ↓ reads only the named skills
skills/shared/* + automotive-development/skills/*
```

The pipeline skill owns workflow classification and gate coordination. A playbook owns stage sequencing, inputs, and outputs. A leaf skill owns one reusable behavior or one automotive-specific artifact. Shared skills must not depend on automotive standards, ECU terminology, or SRS/STS formats.

The current automotive pipeline remains available as a leaf skill for compatibility. New playbooks may compose its rules, but must not silently bypass approval, baseline, or traceability gates.
