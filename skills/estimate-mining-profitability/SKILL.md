---
name: estimate-mining-profitability
description: >-
  Call Autopilot MCP tool estimate_mining_profitability for a read-only daily
  mining revenue estimate. Use when a host needs profitability-advisor metrics
  with demo/fixture provenance. Never mutates miners, pools, or wallets.
---

# Estimate mining profitability

An agent skill (Agent Skills `SKILL.md` convention). Guidance only — not an MCP
schema and not authorization.

## Purpose

Invoke Autopilot MCP tool `estimate_mining_profitability`, backed by the
`profitability-advisor` agent.

## Prerequisites

- MCP host is connected per `connect-autopilot-mcp`.
- Upstream Autopilot MCP is running (local `serve --transport http` on
  `127.0.0.1:18100` or an approved private URL).

## Inputs

| Field | Type | Rules |
|---|---|---|
| `hashrate_ths` | number \| omit | Optional hashrate in TH/s; omit only if upstream accepts defaults |
| `request_id` | string \| omit | Optional correlation id for the invocation |

## Outputs

JSON `AgentResult` (string payload from the MCP tool) including metrics and
evidence with **provenance labels** (demo BTC Insights or local-fixture
fallback). Treat provenance as authoritative.

Upstream skill-manifest note: advisor may be `fixture-economics` /
`production_ready: false` — match that honesty in user-facing answers.

## Examples

```json
{"tool": "estimate_mining_profitability", "arguments": {"hashrate_ths": 9.0}}
```

## Failure modes

| Error category | Meaning | Recovery |
|---|---|---|
| `validation` | Bad or extra arguments | Fix inputs; do not invent fields |
| `permission_denied` | Upstream authorizer denied | Report; do not retry with forged identity |
| `unavailable` / timeout | MCP or advisor unreachable | Check `AUTOPILOT_MCP_URL` and local serve |
| empty / missing provenance | Unexpected payload | Do not fabricate metrics; report failure |

## Safety and approval

Read-only. Needs no approval prompt. Never use this skill path for payments,
pool changes, or wallet moves.

## Related MCP artifacts

- Tool: `estimate_mining_profitability`
- Adapter: `terrahash-autopilot` `apps/autopilot-mcp` @
  `5d5fb3e952bbe2df50ea2453f9bb309f17796d72`
