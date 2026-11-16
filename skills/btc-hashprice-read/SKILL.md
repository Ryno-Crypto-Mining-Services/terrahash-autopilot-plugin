---
name: btc-hashprice-read
description: >-
  Read Bitcoin mining hashprice via BTC Insights MCP tools get_current_hashprice
  and get_hashprice. Use for read-only market economics signals. Never mutates
  state and never issues approvals.
---

# BTC hashprice read

An agent skill (Agent Skills `SKILL.md` convention). Guidance for hosts — not
an MCP schema.

## Purpose

Call BTC Insights catalog tools for hashprice:

- `get_current_hashprice` — current hashprice for a hash unit
- `get_hashprice` — time series for span/bucket/currency/hashunit

Related (optional): `get_hashprice_volatility` (30-day rolling volatility).

## Prerequisites

- MCP host connected per `connect-btc-insights-mcp`.
- Caller holds upstream `market:read` (server-enforced).

## Inputs (typical)

| Tool | Fields |
|---|---|
| `get_current_hashprice` | `hashunit` (and currency where required by schema) |
| `get_hashprice` | `span`, `bucket`, `currency`, `hashunit` |

Exact schemas come from upstream generated artifacts — do not invent fields.

## Outputs

Insights payloads with provenance. Preserve provider/demo labels in answers.

## Examples

```json
{"tool": "get_current_hashprice", "arguments": {"currency": "USD", "hashunit": "PH"}}
```

## Failure modes

| Error category | Meaning | Recovery |
|---|---|---|
| `validation` | Bad arguments | Fix to catalog schema |
| `permission_denied` | Missing `market:read` | Report; do not forge principal |
| `rate_limited` / `timeout` / `unavailable` | Upstream trouble | Retry later, once |
| demo-only data | Fixture/demo mode | Disclose provenance; do not claim live |

## Safety and approval

Read-only (`approval: none` in catalog). Skills never approve privileged
actions.

## Related MCP artifacts

- Tools: `get_current_hashprice`, `get_hashprice`, `get_hashprice_volatility`
- Catalog @ `b24e0a2704f697d7194785c14b3a5aa353228f7d`
