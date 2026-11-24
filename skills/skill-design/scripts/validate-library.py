#!/usr/bin/env python3
"""활성 스킬의 메타데이터와 로컬 Markdown 링크를 확인한다."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")
FIELD = re.compile(r"^(name|description):\s*(.+)$", re.MULTILINE)


def skill_files(root: Path) -> list[Path]:
    shared = sorted((root / "skills").glob("*/SKILL.md"))
    package = root / "garden-beam" / "SKILL.md"
    return shared + ([package] if package.is_file() else [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[3]
    )
    root = parser.parse_args().root.resolve()
    errors: list[str] = []
    skills = skill_files(root)

    if not skills:
        errors.append(f"스킬을 찾지 못함: {root}")
    for path in skills:
        body = path.read_text(encoding="utf-8")
        if not body.startswith("---\n") or "\n---\n" not in body[4:]:
            errors.append(f"잘못된 frontmatter: {path}")
            continue
        frontmatter = body.split("\n---\n", 1)[0][4:]
        fields = dict(FIELD.findall(frontmatter))
        if fields.get("name") != path.parent.name:
            errors.append(f"스킬 이름과 디렉터리가 다름: {path}")
        if not fields.get("description"):
            errors.append(f"스킬 설명 없음: {path}")

    markdown = [root / "README.md"] if (root / "README.md").exists() else []
    for directory in (root / "skills", root / "garden-beam"):
        if directory.exists():
            markdown.extend(directory.rglob("*.md"))
    for path in markdown:
        for raw in LINK.findall(path.read_text(encoding="utf-8")):
            if raw.startswith("#") or "://" in raw or raw.startswith("mailto:"):
                continue
            target = unquote(raw.split("#", 1)[0])
            if target and not (path.parent / target).exists():
                errors.append(f"끊어진 로컬 링크: {path} -> {raw}")

    if errors:
        for error in errors:
            print(f"오류: {error}", file=sys.stderr)
        return 1
    print(f"스킬 라이브러리 구조: 정상 ({len(skills)} 활성 스킬)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
