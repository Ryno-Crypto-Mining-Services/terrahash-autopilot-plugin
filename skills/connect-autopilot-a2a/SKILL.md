---
name: connect-autopilot-a2a
description: >-
  Connect an A2A 0.3.0 client to Autopilot's private/local profitability
  adapter using message/send and tasks/get. Use for dual MCP+A2A host wiring.
  Not a public agent card publication path.
---

# Connect Autopilot A2A

An agent skill (Agent Skills `SKILL.md` convention). Guidance for hosts — not
an MCP schema and not a publishable agent-card artifact.

## Purpose

Use Autopilot's minimal A2A **0.3.0** JSON-RPC adapter for read-only
`profitability-advisor` invocations from A2A-capable clients.

## Upstream evidence

- Repository: `terrahash-autopilot` / `apps/autopilot-a2a`
- Evidence SHA: `5d5fb3e952bbe2df50ea2453f9bb309f17796d72`
- Protocol pin: A2A `0.3.0` (`protocol-lock/pins.yaml`)
- Registration: `publishable: false`

## Prerequisites

- Autopilot A2A listening on an operator-approved URL (local default
  `http://127.0.0.1:18101/`).
- Client speaks A2A 0.3.0 JSON-RPC.
- Card may be available at `/.well-known/agent-card.json` for **local/private**
  smoke only — not a public listing.

## Methods

| Method | Role |
|---|---|
| `message/send` | Submit a user message (e.g. data part with `hashrate_ths`) |
| `tasks/get` | Fetch task status / result |

## Example (local smoke)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [{"kind": "data", "data": {"hashrate_ths": 9.0}}],
      "messageId": "smoke-1"
    }
  }
}
```

## Constraints

- Private/local only until publication gates open.
- Read-only; Phase 1 denies payments and `publish_agent_card`.
- Do **not** confuse with BTC Insights — that project's A2A runtime is **not**
  implemented; design cards only.
- Do not invent public well-known catalog URLs.

## Failure modes

| Error category | Meaning | Recovery |
|---|---|---|
| connection refused | Adapter not running | Start local serve or fix private URL |
| method not found | Wrong protocol / path | Use A2A 0.3.0 methods only |
| task error | Advisor/invocation failure | Inspect task; do not retry blindly |

## Related skills

- `connect-autopilot-mcp` — MCP sibling surface
- `estimate-mining-profitability` — profitability semantics
