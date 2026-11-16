#!/usr/bin/env python3
"""Validate docs/protocol-pins.md mirrors expected MCP/A2A revisions and SHAs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINS_DOC = ROOT / "docs" / "protocol-pins.md"

EXPECTED_MCP = "2025-06-18"
EXPECTED_A2A = "0.3.0"
# Evidence SHAs from the approved scaffold proposal (inspection baseline).
AUTOPILOT_SHA = "5d5fb3e952bbe2df50ea2453f9bb309f17796d72"
BTC_INSIGHTS_SHA = "b24e0a2704f697d7194785c14b3a5aa353228f7d"


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not PINS_DOC.is_file():
        _fail(f"missing {PINS_DOC}")
    text = PINS_DOC.read_text(encoding="utf-8")
    checks = (
        (EXPECTED_MCP, "MCP revision"),
        (EXPECTED_A2A, "A2A revision"),
        (AUTOPILOT_SHA, "Autopilot evidence SHA"),
        (BTC_INSIGHTS_SHA, "BTC Insights evidence SHA"),
        ("publishable: false", "publication gate reminder"),
    )
    for needle, label in checks:
        if needle not in text:
            _fail(f"docs/protocol-pins.md missing {label}: {needle}")
    print(f"OK: pins MCP {EXPECTED_MCP}, A2A {EXPECTED_A2A}")


if __name__ == "__main__":
    main()
