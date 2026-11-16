#!/usr/bin/env python3
"""Validate skill frontmatter and allowlisted MCP tool ids."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_SKILLS = (
    "connect-autopilot-mcp",
    "estimate-mining-profitability",
    "connect-autopilot-a2a",
    "connect-btc-insights-mcp",
    "btc-hashprice-read",
    "btc-network-overview",
)

# Minimal allowlist synced to upstream evidence SHAs in docs/protocol-pins.md.
ALLOWED_TOOL_IDS = frozenset(
    {
        "estimate_mining_profitability",
        "get_current_hashprice",
        "get_hashprice",
        "get_hashprice_volatility",
        "get_network_overview",
    }
)

FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
# MCP-style tool ids referenced in backticks.
TOOL_ID_RE = re.compile(r"`((?:estimate|get)_[a-z0-9_]+)`")


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def _parse_frontmatter(text: str, path: Path) -> str:
    match = FRONTMATTER_RE.match(text)
    if match is None:
        _fail(f"{path}: missing YAML frontmatter")
    body = match.group("body")
    name_match = NAME_RE.search(body)
    desc_match = DESC_RE.search(body)
    if name_match is None or desc_match is None:
        _fail(f"{path}: frontmatter requires name and description")
    name = name_match.group(1).strip().strip("\"'")
    description = desc_match.group(1).strip()
    if not name or not description:
        _fail(f"{path}: name/description must be non-empty")
    return name


def main() -> None:
    if not SKILLS_DIR.is_dir():
        _fail(f"missing skills directory: {SKILLS_DIR}")

    found: list[str] = []
    for skill_name in REQUIRED_SKILLS:
        skill_path = SKILLS_DIR / skill_name / "SKILL.md"
        if not skill_path.is_file():
            _fail(f"missing required skill: {skill_path}")
        text = skill_path.read_text(encoding="utf-8")
        name = _parse_frontmatter(text, skill_path)
        if name != skill_name:
            _fail(f"{skill_path}: frontmatter name {name!r} != directory {skill_name!r}")
        for candidate in TOOL_ID_RE.findall(text):
            if candidate not in ALLOWED_TOOL_IDS:
                _fail(f"{skill_path}: tool id not in allowlist: {candidate!r}")
        found.append(skill_name)

    extras = sorted(
        p.name
        for p in SKILLS_DIR.iterdir()
        if p.is_dir() and (p / "SKILL.md").is_file() and p.name not in REQUIRED_SKILLS
    )
    if extras:
        _fail(f"unexpected skill directories (update REQUIRED_SKILLS intentionally): {extras}")

    print(f"OK: {len(found)} skills validated")


if __name__ == "__main__":
    main()
