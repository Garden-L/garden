#!/usr/bin/env python3
"""완료된 자동차 모듈 묶음의 구조적 연결을 확인한다.

요구사항, 코드, 관찰 결과의 의미상 정확성은 판단하지 않는다.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from pathlib import Path
from urllib.parse import unquote


REQUIRED = (
    "README.md",
    "01-srs/SRS.md",
    "01-srs/issues.md",
    "01-srs/review.md",
    "02-sts/STS.md",
    "02-sts/issues.md",
    "02-sts/review.md",
    "03-readiness/readiness-report.md",
    "04-implementation/implementation-report.md",
    "traceability.md",
    "05-verification/completion-report.md",
    "05-verification/verification.md",
)
LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
REQ = re.compile(r"\bREQ-\d+\b")
TC = re.compile(r"\bTC-\d+\b")
ISSUE = re.compile(r"\bISSUE-\d+\b")
ROW = re.compile(r"^\|\s*[^|]+\|\s*(REQ-\d+)\s*\|\s*(TC-\d+)\s*\|\s*([^|]+)\|\s*(WORK-\d+)\s*\|", re.MULTILINE)


def read(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"파일 누락: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def check_links(path: Path, errors: list[str]) -> None:
    for raw in LINK.findall(path.read_text(encoding="utf-8")):
        if "://" in raw or raw.startswith("mailto:"):
            continue
        target, _, anchor = unquote(raw).partition("#")
        destination = path.parent / target if target else path
        if not destination.exists():
            errors.append(f"끊어진 링크: {path}: {raw}")
        elif anchor and destination.suffix == ".md":
            headings = HEADING.findall(destination.read_text(encoding="utf-8"))
            slugs = {
                re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", heading.lower())).strip("-")
                for heading in headings
            }
            if anchor not in slugs:
                errors.append(f"끊어진 제목 앵커: {path}: {raw}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("module_dir", type=Path, help="docs/modules/<module> 디렉터리")
    args = parser.parse_args()
    module = args.module_dir.resolve()
    errors: list[str] = []

    texts = {name: read(module / name, errors) for name in REQUIRED}
    work_files = sorted((module / "04-implementation").glob("WORK-*.md"))
    if not work_files:
        errors.append(f"작업 패킷 누락: {module / '04-implementation' / 'WORK-<id>.md'}")

    requirements = set(REQ.findall(texts["01-srs/SRS.md"]))
    cases = set(TC.findall(texts["02-sts/STS.md"]))
    issues = set(ISSUE.findall(texts["01-srs/issues.md"]))
    work = {path.stem for path in work_files}
    for label, found in (("REQ", requirements), ("TC", cases), ("WORK", work)):
        if not found:
            errors.append(f"선언된 {label} ID 없음: {module}")

    rows = ROW.findall(texts["traceability.md"])
    if not rows:
        errors.append(f"추적성 행 없음: {module / 'traceability.md'}")
    row_requirements = {req for req, _, _, _ in rows}
    row_cases = {tc for _, tc, _, _ in rows}
    row_work = {packet for _, _, _, packet in rows}
    row_issues = {issue for _, _, cell, _ in rows for issue in re.findall(r"ISSUE-\d+", cell)}

    for label, declared, mapped in (
        ("REQ", requirements, row_requirements),
        ("TC", cases, row_cases),
        ("ISSUE", issues, row_issues),
        ("WORK", work, row_work),
    ):
        for ident in sorted(declared - mapped):
            errors.append(f"{label} 추적성에서 누락: {ident}")
        for ident in sorted(mapped - declared):
            errors.append(f"추적성이 선언되지 않은 ID를 참조: {label}: {ident}")

    for path in sorted(module.rglob("*.md")):
        check_links(path, errors)

    if "Verified" not in texts["README.md"]:
        errors.append("README.md에 최종 Verified 판단이 없음. 전체 인계 검사는 검증 후 사용한다")
    if not LINK.search(texts["05-verification/verification.md"]):
        errors.append("05-verification/verification.md에 근거 링크가 없음")

    if all((module / name).is_file() for name in REQUIRED):
        with TemporaryDirectory() as temporary:
            generated = Path(temporary) / "completion-report.md"
            language = "ko" if texts["05-verification/completion-report.md"].startswith("# 모듈") else "en"
            command = [
                sys.executable,
                str(Path(__file__).with_name("report-module-coverage.py")),
                str(module),
                "--project-root",
                str(module.parents[2]),
                "--lang",
                language,
                "--output",
                str(generated),
            ]
            result = subprocess.run(command, text=True, capture_output=True)
            if result.returncode:
                errors.append(f"완료 보고서 생성 실패: {result.stderr.strip()}")
            elif generated.read_text(encoding="utf-8") != texts["05-verification/completion-report.md"]:
                errors.append("05-verification/completion-report.md가 오래됨. 현재 기록에서 다시 생성한다")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"모듈 인계 구조: 실패 ({len(errors)}개 오류)", file=sys.stderr)
        return 1
    print(
        "모듈 인계 구조: 정상 "
        f"({len(requirements)} REQ, {len(cases)} TC, {len(issues)} ISSUE, {len(work)} WORK)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
