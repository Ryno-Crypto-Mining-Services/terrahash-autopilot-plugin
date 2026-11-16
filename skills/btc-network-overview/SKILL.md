---
name: btc-network-overview
description: >-
  Read a Bitcoin network snapshot via BTC Insights MCP tool get_network_overview.
  Use for read-only network metrics. Does not change miners, pools, or wallets.
---

# BTC network overview

An agent skill (Agent Skills `SKILL.md` convention). Guidance only.

## Purpose

Call BTC Insights tool `get_network_overview` for a current network metrics
snapshot (`network:read`).

## Prerequisites

- MCP host connected per `connect-btc-insights-mcp`.
- Upstream permission `network:read` enforced server-side.

## Inputs

Typically empty object `{}` per catalog. Do not send extra fields.

## Outputs

Insights network snapshot with provenance. Disclose demo vs live.

## Examples

```json
{"tool": "get_network_overview", "arguments": {}}
```

## Failure modes

| Error category | Meaning | Recovery |
|---|---|---|
| `validation` | Unexpected fields | Send catalog-shaped input |
| `permission_denied` | Missing `network:read` | Report; stop |
| `unavailable` / timeout | Backend issues | Retry later, once |

## Safety and approval

Read-only. No approval path. Never treat this skill as operational control of
hashrate, pools, or facilities.

## Related MCP artifacts

- Tool: `get_network_overview`
- Catalog @ `b24e0a2704f697d7194785c14b3a5aa353228f7d`
- Related skill: `btc-hashprice-read`
