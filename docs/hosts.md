# Host support matrix

Honest MVP support for connecting hosts to Autopilot / BTC Insights. Packaging
formats beyond Cursor are **docs-only** until verified separately.

| Host | MVP support | Mechanism |
|---|---|---|
| **Cursor** | Primary | `.cursor-plugin/plugin.json` + `skills/` + `rules/` + `mcp.json` variables |
| **Claude Code** | Secondary | Clone or copy `skills/`; follow `AGENTS.md` / `CLAUDE.md`. No root Agent Plugins `plugin.json` in MVP |
| **ChatGPT** | Docs-only | Configure as a generic MCP client against operator-supplied URLs |
| **Hermes** | Docs-only | Same: MCP/A2A client config from skills; no Hermes-specific package here |
| **OpenClaw** | Docs-only | Same as Hermes |
| **Grok / xAI** | Docs-only | Generic MCP client notes only; no proprietary packaging verified |

Autopilot Nexus (LibreChat) web UI is **out of MVP** (founder Phase D deferred).

## Cursor

1. Install this Git repository as a Cursor plugin.
2. Set `AUTOPILOT_MCP_URL` and `BTC_INSIGHTS_MCP_URL` under Plugins → Configure.
3. Prefer loopback during local development:
   - Autopilot MCP: `http://127.0.0.1:18100/mcp`
   - Autopilot A2A (not via mcp.json): `http://127.0.0.1:18101/`
4. Tailscale MagicDNS pattern (operator-private, not a claimed live host):
   `http://terrahash-autopilot-mcp.<tailnet>:18100/mcp`

## Claude Code

Copy or submodule the `skills/` tree into a project that Claude Code can load.
Keep `AGENTS.md` as the policy pointer. Dual Agent Plugins root manifest is
deferred (Cursor-first).

## Generic MCP clients (ChatGPT / Hermes / OpenClaw / Grok)

Point the client's MCP HTTP transport at the same operator-approved URLs. Use
skill docs for tool names and provenance rules. Do not assume marketplace
install paths or proprietary auth headers unless documented upstream.

## A2A clients

Autopilot A2A listens separately (local default `:18101`). Use the
`connect-autopilot-a2a` skill. Do **not** treat BTC Insights as an A2A agent —
upstream documents design cards only; runtime is not implemented.
