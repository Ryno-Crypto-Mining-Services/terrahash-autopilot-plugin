---
name: connect-autopilot-mcp
description: >-
  Configure a host MCP client for TerraHash Autopilot's read-only MCP adapter.
  Use when connecting Cursor or another MCP host to Autopilot profitability
  tools. Placeholders only; no public FQDN claims.
---

# Connect Autopilot MCP

An agent skill (Agent Skills `SKILL.md` convention). It is guidance for a host
agent, not an MCP schema and not an A2A wire artifact.

## Purpose

Point an MCP host at Autopilot's thin read-only MCP adapter and call only the
verified tool surface. Do not stand up a second MCP server in this plugin repo.

## Upstream evidence

- Repository: `terrahash-autopilot` / `apps/autopilot-mcp`
- Evidence SHA: `5d5fb3e952bbe2df50ea2453f9bb309f17796d72`
- Protocol: MCP `2025-06-18` (`protocol-lock/pins.yaml`)
- Registration artifacts: `publishable: false`

## Prerequisites

- Autopilot MCP is reachable on an **operator-supplied** URL.
- Plugin / host variable `AUTOPILOT_MCP_URL` is set (see root `mcp.json`).
- Prefer loopback for local demos: `http://127.0.0.1:18100/mcp`.
- Tailscale MagicDNS is an operator pattern only:
  `http://terrahash-autopilot-mcp.<tailnet>:18100/mcp`.

## Verified tool surface (at evidence SHA)

| Tool | Agent backend |
|---|---|
| `estimate_mining_profitability` | `profitability-advisor` |

Default invoke mode upstream is **in-process**; HTTP loopback is for hosts.

## Constraints

- Read-only. No writes, payments, miner/pool control, or `publish_agent_card`.
- Demo/fixture data with provenance labels — do not relabel as live.
- Skills do not authorize calls; upstream policy does.
- Never invent public Cloudflare / internet FQDNs in config.

## Related skills

- `estimate-mining-profitability` — call shape and failure modes
- `connect-autopilot-a2a` — sibling A2A adapter (not this MCP server)

## Related MCP artifacts

- Host config: root `mcp.json` → server `autopilot` → `${AUTOPILOT_MCP_URL}`
- Example filled values: `fixtures/mcp.example.json`
