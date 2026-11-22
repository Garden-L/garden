#!/usr/bin/env python3
"""Check active skill metadata and local Markdown links in the library."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")
FIELD = re.compile(r"^(name|description):\s*(.+)$", re.MULTILINE)


def skill_files(root: Path) -> list[Path]:
    return sorted((root / "skills").glob("*/SKILL.md")) + sorted(
        (root / "automotive-development" / "skills").glob("*/SKILL.md")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[3]
    )
    root = parser.parse_args().root.resolve()
    errors: list[str] = []
    skills = skill_files(root)

    if not skills:
        errors.append(f"no skills found under {root}")
    for path in skills:
        body = path.read_text(encoding="utf-8")
        if not body.startswith("---\n") or "\n---\n" not in body[4:]:
            errors.append(f"invalid frontmatter: {path}")
            continue
        frontmatter = body.split("\n---\n", 1)[0][4:]
        fields = dict(FIELD.findall(frontmatter))
        if fields.get("name") != path.parent.name:
            errors.append(f"skill name does not match directory: {path}")
        if not fields.get("description"):
            errors.append(f"missing skill description: {path}")

    markdown = [root / "README.md"] if (root / "README.md").exists() else []
    for directory in (root / "skills", root / "automotive-development"):
        if directory.exists():
            markdown.extend(directory.rglob("*.md"))
    for path in markdown:
        for raw in LINK.findall(path.read_text(encoding="utf-8")):
            if raw.startswith("#") or "://" in raw or raw.startswith("mailto:"):
                continue
            target = unquote(raw.split("#", 1)[0])
            if target and not (path.parent / target).exists():
                errors.append(f"broken local link: {path} -> {raw}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"skill library structure: OK ({len(skills)} active skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
