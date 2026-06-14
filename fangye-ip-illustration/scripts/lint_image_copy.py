#!/usr/bin/env python3
"""Lint Fangye image copy for common AI/copywriting flavor."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HARD_PHRASES = [
    "方也版",
    "鹿也",
    "粟也",
    "把研究翻译成行动",
    "递信号",
    "核心逻辑",
    "底层逻辑",
    "本质",
    "闭环",
    "一文读懂",
    "建议收藏",
]

WARN_PHRASES = [
    "真正有用",
    "真正重要",
    "研究表明",
    "专家认为",
    "不要追求满分",
    "方法论",
    "不是",
    "而是",
    "先别",
    "先把",
    "总之",
]

WARN_PATTERNS = [
    (re.compile(r"不是.+而是"), "binary contrast shell"),
    (re.compile(r"先.+再"), "route-like instruction"),
    (re.compile(r"从.+到.+"), "framework-like phrasing"),
]


def collect_text(args: argparse.Namespace) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for idx, text in enumerate(args.text or [], start=1):
        items.append((f"--text {idx}", text))
    for file_name in args.file or []:
        path = Path(file_name)
        items.append((str(path), path.read_text(encoding="utf-8")))
    return items


def lint_one(label: str, text: str) -> list[tuple[str, str, str]]:
    findings: list[tuple[str, str, str]] = []
    for phrase in HARD_PHRASES:
        if phrase in text:
            findings.append(("error", label, f"avoid `{phrase}`"))
    for phrase in WARN_PHRASES:
        if phrase in text:
            findings.append(("warn", label, f"review `{phrase}`"))
    for pattern, message in WARN_PATTERNS:
        if pattern.search(text):
            findings.append(("warn", label, message))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="append", help="Image copy string to lint")
    parser.add_argument("--file", action="append", help="UTF-8 text file to lint")
    parser.add_argument("--strict", action="store_true", help="Return non-zero on warnings too")
    args = parser.parse_args()

    items = collect_text(args)
    if not items:
        parser.error("provide --text or --file")

    all_findings: list[tuple[str, str, str]] = []
    for label, text in items:
        all_findings.extend(lint_one(label, text))

    if not all_findings:
        print("OK: Fangye image copy looks clean.")
        return 0

    for level, label, message in all_findings:
        print(f"{level.upper()}: {label}: {message}")

    has_error = any(level == "error" for level, _, _ in all_findings)
    if has_error or (args.strict and all_findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
