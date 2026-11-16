# Agent guidelines — terrahash-autopilot-plugin

Canonical instructions for humans and coding agents working in this repository.

## What this repo is

A **Cursor Plugin + portable Agent Skills** package that teaches host agents how
to connect to TerraHash Autopilot MCP/A2A and BTC Insights MCP.

It is a **host connector** package (founder Phase C), not an agent runtime, not
a second MCP/A2A server, and not a deployable container/Helm chart.

## What this repo is not

- Not a FastMCP / A2A / Worker application (`src/` runtime belongs upstream).
- Not marketplace-published until explicitly approved.
- Not authority for tool catalogs — Autopilot apps and BTC Insights
  `catalog.yaml` win on conflict.
- Not a place to invent public FQDNs, enable registries, or ship secrets.

## Upstream evidence (inspection baseline)

| Upstream | Evidence SHA | Role |
|---|---|---|
| `terrahash-autopilot` | `5d5fb3e952bbe2df50ea2453f9bb309f17796d72` | MCP/A2A adapters + `protocol-lock/pins.yaml` |
| `btc-insights-mcp-server` | `b24e0a2704f697d7194785c14b3a5aa353228f7d` | Catalog-driven MCP tools; A2A runtime **not** implemented |

Protocol pins: MCP `2025-06-18`, A2A `0.3.0`, `publishable: false`. See
`docs/protocol-pins.md`.

## Principles

1. **Skills are guidance, not enforcement.** Server-side policy and approvals
   live upstream (`execution.py` / Autopilot Phase 1 policy). Never treat a
   skill or prompt as authorization.
2. **Read-only Phase 1.** No miner/pool writes, trading, withdrawals, payment
   routes, `publish_agent_card`, or shell-as-product tools via this plugin.
3. **Placeholders only for URLs.** Use `${AUTOPILOT_MCP_URL}` /
   `${BTC_INSIGHTS_MCP_URL}`. Document loopback and Tailscale MagicDNS
   **patterns**; never invent public hostnames.
4. **Evidence over assumption.** Do not claim public connectivity, marketplace
   readiness, BTC Insights A2A wire support, or live endpoints you did not
   verify.
5. **Upstream wins.** If a skill disagrees with Autopilot or BTC Insights
   source/tests, fix the skill — do not relax the skill to “paper over” drift.
6. **Minimal allowlists.** Validators may pin tool ids; do not vendor full
   upstream catalogs.

## Drift control

- `AGENTS.md` is the single source of truth in this repo.
- Thin mirrors only: `CLAUDE.md`, `.github/copilot-instructions.md`,
  `rules/terrahash-boundaries.mdc` — point here; do not duplicate policy.
- Skills use Agent Skills `SKILL.md` convention (same shape as
  `terrahash-mcp-server-template`).

## Validation

```bash
python3 --version   # expect >= 3.12
python3 scripts/validate_skills.py
python3 scripts/validate_mcp_json.py
python3 scripts/validate_pins.py
```

CI runs the same three validators plus `detect-secrets` against
`.secrets.baseline`. No live MCP calls in default CI.

## Forbidden in incidental PRs

- LICENSE/CODEOWNERS changes beyond already-approved Apache-2.0 (no guessed owners).
- CD, Docker, GHCR, Helm, marketplace submission assets.
- Root Agent Plugins `plugin.json` (Cursor-first; dual manifest deferred).
- Enabling ans-registry / mcp-gateway-registry publication from this repo.
- Concrete secrets, customer data, or unpaid origin bypass instructions.
