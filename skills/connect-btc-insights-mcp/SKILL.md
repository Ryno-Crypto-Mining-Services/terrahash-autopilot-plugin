---
name: connect-btc-insights-mcp
description: >-
  Point a host MCP client at BTC Insights MCP using catalog tool ids. Use when
  connecting to hashprice, network, or related read tools. Do not claim A2A
  runtime support for BTC Insights.
---

# Connect BTC Insights MCP

An agent skill (Agent Skills `SKILL.md` convention). Guidance only — not an MCP
schema and not an A2A wire artifact.

## Purpose

Configure a host to call **BTC Insights** MCP tools. Capability facts live in
upstream `catalog.yaml`; this plugin must not invent tool ids.

## Upstream evidence

- Repository: `btc-insights-mcp-server`
- Evidence SHA: `b24e0a2704f697d7194785c14b3a5aa353228f7d`
- Protocol: MCP `2025-06-18`
- A2A: runtime **not implemented** (design card only) — never claim wire support

## Prerequisites

- Operator-approved `BTC_INSIGHTS_MCP_URL` (plugin variable / host config).
- Server enforces policy in `execution.py` / `security/` — skills cannot bypass.
- Demo vs live data depends on upstream configuration; preserve provenance.

## Catalog authority

Use catalog tool ids such as:

- `get_current_hashprice`, `get_hashprice`, `get_hashprice_volatility`
- `get_network_overview`

Do not hand-edit generated upstream schemas or invent aliases without a mapping
table.

## Constraints

- Skills are guidance, not approval or entitlement.
- Paid exposure / x402 paths remain default-off upstream — do not document
  unpaid origin bypass.
- No public FQDN invention in this plugin.
- GHCR image existence does not imply this plugin deploys or publishes it.

## Related skills

- `btc-hashprice-read`
- `btc-network-overview`

## Related MCP artifacts

- Host config: root `mcp.json` → server `btc-insights` → `${BTC_INSIGHTS_MCP_URL}`
- Upstream catalog: `src/btc_insights_mcp_server/catalog.yaml`
