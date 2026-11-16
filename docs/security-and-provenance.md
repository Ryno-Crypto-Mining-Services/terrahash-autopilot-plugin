# Security and provenance

## Skills are untrusted for safety

Host skills in this repository are **guidance**. They do not grant permissions,
approve actions, or bypass upstream policy. Autopilot Phase 1 authorization and
BTC Insights `execution.py` / `security/` remain authoritative.

Never add a skill that “issues approvals” or accepts a caller-supplied approval
boolean as truth.

## Demo versus live

Autopilot MCP profitability results may carry **demo/fixture** provenance labels.
BTC Insights may run against demo datasets or approved live sources depending on
operator configuration. Skills must preserve provenance language from tool
results and must not relabel demo data as live market truth.

## Secrets

- No secrets in git. `.env` is gitignored.
- Plugin variables declare names only; values are set in the host dashboard.
- `mcp.json` uses `${AUTOPILOT_MCP_URL}` and `${BTC_INSIGHTS_MCP_URL}` only.
- CI runs `detect-secrets` against `.secrets.baseline`.

## Endpoints

Do not invent public FQDNs. Document:

- Loopback examples (`127.0.0.1`)
- Tailscale MagicDNS **patterns** for enrolled operators

Public Cloudflare / internet hostnames remain out of scope until separately
named and approved.

## Read-only Phase 1

Deny via guidance and upstream policy: miner/pool control, trading, withdrawals,
payment routes, `publish_agent_card`, and arbitrary shell as a product tool.
