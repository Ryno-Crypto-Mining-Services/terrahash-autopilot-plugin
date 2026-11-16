#!/usr/bin/env python3
"""Validate mcp.json placeholders against .cursor-plugin/plugin.json variables."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MCP_JSON = ROOT / "mcp.json"
PLUGIN_JSON = ROOT / ".cursor-plugin" / "plugin.json"
EXAMPLE_JSON = ROOT / "fixtures" / "mcp.example.json"

PLACEHOLDER_RE = re.compile(r"\$\{([A-Z][A-Z0-9_]*)\}")
REQUIRED_SERVERS = ("autopilot", "btc-insights")
REQUIRED_VARS = ("AUTOPILOT_MCP_URL", "BTC_INSIGHTS_MCP_URL")


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def _load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        _fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        _fail(f"invalid JSON in {path}: {exc}")


def main() -> None:
    plugin = _load_json(PLUGIN_JSON)
    mcp = _load_json(MCP_JSON)
    example = _load_json(EXAMPLE_JSON)

    if not isinstance(plugin, dict):
        _fail("plugin.json must be an object")
    if plugin.get("name") != "terrahash-autopilot":
        _fail("plugin.json name must be terrahash-autopilot")

    variables = plugin.get("variables")
    if not isinstance(variables, dict) or variables.get("type") != "object":
        _fail("plugin.json variables must be a JSON Schema object")
    properties = variables.get("properties")
    if not isinstance(properties, dict):
        _fail("plugin.json variables.properties must be an object")
    for var_name in REQUIRED_VARS:
        if var_name not in properties:
            _fail(f"plugin.json missing variable {var_name}")

    if not isinstance(mcp, dict):
        _fail("mcp.json must be an object")
    servers = mcp.get("mcpServers")
    if not isinstance(servers, dict):
        _fail("mcp.json mcpServers must be an object")
    for server_name in REQUIRED_SERVERS:
        entry = servers.get(server_name)
        if not isinstance(entry, dict):
            _fail(f"mcp.json missing server {server_name}")
        url = entry.get("url")
        if not isinstance(url, str):
            _fail(f"mcp.json {server_name}.url must be a string")
        placeholders = PLACEHOLDER_RE.findall(url)
        if not placeholders:
            _fail(f"mcp.json {server_name}.url must use a ${{VAR}} placeholder")
        for placeholder in placeholders:
            if placeholder not in properties:
                _fail(f"mcp.json uses undeclared variable {placeholder}")

    raw_mcp = MCP_JSON.read_text(encoding="utf-8")
    if "http://" in raw_mcp or "https://" in raw_mcp:
        _fail("mcp.json must not embed concrete http(s) URLs; use placeholders")

    if not isinstance(example, dict) or "mcpServers" not in example:
        _fail("fixtures/mcp.example.json must contain mcpServers")

    print("OK: mcp.json and plugin.json variables consistent")


if __name__ == "__main__":
    main()
