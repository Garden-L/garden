#!/usr/bin/env python3
"""Summarize recorded requirement/test/work/evidence coverage for one module.

The report is an index of records, not independent proof that tests passed or
that the vehicle target behaves correctly. Review verification.md for that.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


REQ = re.compile(r"\bREQ-\d+\b")
TC = re.compile(r"\bTC-\d+\b")
TRACE = re.compile(
    r"^\|\s*[^|]+\|\s*(REQ-\d+)\s*\|\s*(TC-\d+)\s*\|"
    r"\s*[^|]+\|\s*(WORK-\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|",
    re.MULTILINE,
)
RESULT = re.compile(
    r"^\|\s*(REQ-\d+)\s*\|\s*(TC-\d+)\s*\|\s*(Pass|Fail|Blocked|Not run)\s*\|",
    re.MULTILINE | re.IGNORECASE,
)
BACKTICK_PATH = re.compile(r"`([^`]+)`")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("module_dir", type=Path)
    parser.add_argument("--output", type=Path, help="default: <module_dir>/05-verification/completion-report.md")
    parser.add_argument("--lang", choices=("en", "ko"), default="en")
    parser.add_argument(
        "--project-root", type=Path, help="default: inferred from <project>/docs/modules/<module>"
    )
    args = parser.parse_args()
    module = args.module_dir.resolve()
    project = args.project_root.resolve() if args.project_root else module.parents[2]
    output = args.output or module / "05-verification" / "completion-report.md"

    srs = (module / "01-srs" / "SRS.md").read_text(encoding="utf-8")
    sts = (module / "02-sts" / "STS.md").read_text(encoding="utf-8")
    trace = (module / "traceability.md").read_text(encoding="utf-8")
    verification = (module / "05-verification" / "verification.md").read_text(encoding="utf-8")
    requirements = sorted(set(REQ.findall(srs)))
    test_cases = set(TC.findall(sts))
    results = {(req, tc): status.title() for req, tc, status in RESULT.findall(verification)}

    mapped: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)
    for req, tc, work, code_cell, evidence_cell in TRACE.findall(trace):
        mapped[req].append((tc, work, code_cell.strip(), evidence_cell.strip()))

    ko = args.lang == "ko"
    lines = [
        "# 모듈 완료·커버리지 보고서" if ko else "# Module completion and coverage report",
        "",
        (
            "[SRS](../01-srs/SRS.md), [STS](../02-sts/STS.md), [추적성](../traceability.md), [검증](verification.md)에서 "
            "생성했다. 기록된 연결과 상태를 요약할 뿐 코드 동작이나 대상 환경 실행을 독립적으로 증명하지 않는다."
            if ko
            else "Generated from [SRS](../01-srs/SRS.md), [STS](../02-sts/STS.md), [traceability](../traceability.md), "
            "and [verification](verification.md). This reports recorded links and statuses; "
            "it does not independently prove code behavior or target execution."
        ),
        "",
        (
            "| REQ | STS 사례 | WORK | 코드·시험 파일 | 기록된 실행 | 근거 파일 | 공백 |"
            if ko
            else "| REQ | STS case | WORK | Code/test files | Recorded run | Evidence file | Gap |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    complete = 0
    for req in requirements:
        entries = mapped.get(req, [])
        if not entries:
            lines.append(
                f"| {req} | — | — | — | "
                f"{'연결 없음' if ko else 'Not mapped'} | — | "
                f"{'추적성 행 없음' if ko else 'No traceability row'} |"
            )
            continue
        for tc, work, code_cell, evidence_cell in entries:
            gaps = []
            if tc not in test_cases:
                gaps.append("STS에 TC 없음" if ko else "TC absent from STS")
            if not (module / "04-implementation" / f"{work}.md").is_file():
                gaps.append("WORK 패킷 없음" if ko else "WORK packet missing")
            paths = BACKTICK_PATH.findall(code_cell)
            code_ok = len(paths) >= 2 and all((project / p).is_file() for p in paths[:2])
            if not code_ok:
                gaps.append("코드 또는 시험 경로 없음" if ko else "code or test path missing")
            evidence_paths = BACKTICK_PATH.findall(evidence_cell)
            evidence_ok = bool(evidence_paths) and all(
                (project / p).is_file() for p in evidence_paths
            )
            if not evidence_ok:
                gaps.append("근거 경로 없음" if ko else "evidence path missing")
            status = results.get((req, tc), "Not recorded")
            if status != "Pass":
                gaps.append(f"{'시험 상태' if ko else 'test status'}: {status}")
            if not gaps:
                complete += 1
            lines.append(
                f"| {req} | {tc} | {work} | "
                f"{('존재' if ko else 'Present') if code_ok else ('누락' if ko else 'Missing')} | "
                f"{status} | "
                f"{('존재' if ko else 'Present') if evidence_ok else ('누락' if ko else 'Missing')} | "
                f"{'; '.join(gaps) or ('기록된 공백 없음' if ko else 'None recorded')} |"
            )

    lines.extend(
        [
            "",
            (
                f"**기록된 요구사항:** {len(requirements)}. "
                f"**시험 통과와 경로 존재가 기록된 추적성 행:** {complete}/{sum(len(v) for v in mapped.values())}. "
                f"**연결 없는 요구사항:** {len(set(requirements) - set(mapped))}."
                if ko
                else f"**Recorded requirements:** {len(requirements)}. "
                f"**Trace rows with passing test and present paths:** {complete}/{sum(len(v) for v in mapped.values())}. "
                f"**Unmapped requirements:** {len(set(requirements) - set(mapped))}."
            ),
            "",
            (
                "**검토 범위:** `Pass` 값은 verification.md에서 옮겼다. 검토자는 실제 실행을 확인하고 "
                "그 환경이 모듈의 목표를 충족하는지 판단해야 한다. 최종 판단은 모듈 README에 있다."
                if ko
                else "**Review boundary:** A `Pass` value is copied from verification.md. "
                "A reviewer must inspect the actual run and decide whether its environment "
                "satisfies the module's intended target. See the module README for the final verdict."
            ),
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {output} ({complete} recorded passing trace rows)")


if __name__ == "__main__":
    main()
