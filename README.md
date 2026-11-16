# terrahash-autopilot-plugin

Cursor Plugin and portable Agent Skills for connecting host agents to the
**TerraHash Autopilot** multi-agent suite and **BTC Insights** MCP services.

This repository is a **host connector** package: Markdown skills, a thin Cursor
rule, and `mcp.json` with URL **placeholders**. It does **not** ship an MCP or
A2A server, container image, Helm chart, or marketplace listing.

## What you get

| Surface | Purpose |
|---|---|
| `.cursor-plugin/plugin.json` | Cursor Plugin manifest (`terrahash-autopilot`) + URL variables |
| `skills/*/SKILL.md` | How to configure and call verified Autopilot / BTC Insights tools |
| `mcp.json` | `${AUTOPILOT_MCP_URL}` / `${BTC_INSIGHTS_MCP_URL}` only |
| `docs/` | Host matrix, security/provenance, protocol pin mirror |
| `scripts/validate_*.py` | Structure, JSON, and pin consistency gates |

## What this is not

- Not a second Autopilot or BTC Insights runtime (`src/` lives upstream).
- Not public product DNS or registry enablement.
- Not Cursor / Claude marketplace publication (deferred).
- Not BTC Insights A2A wire support (upstream A2A runtime is not implemented).

## Install (Cursor, from Git)

1. Install this public Git repository as a Cursor plugin (see
   [Cursor Plugins](https://cursor.com/docs/reference/plugins)).
2. Configure plugin variables under **Plugins → Configure**:
   - `AUTOPILOT_MCP_URL` — e.g. `http://127.0.0.1:18100/mcp` for local Autopilot MCP
   - `BTC_INSIGHTS_MCP_URL` — operator-approved BTC Insights MCP URL
3. Use the skills; they are guidance for hosts, not authorization.

Example filled config (loopback / patterns only): `fixtures/mcp.example.json`.

Tailscale operators may use MagicDNS **patterns** such as
`http://terrahash-autopilot-mcp.<tailnet>:18100/mcp`. This README does not claim
a live host or public Cloudflare FQDN.

## Skills (MVP)

| Skill | Upstream surface |
|---|---|
| `connect-autopilot-mcp` | Autopilot MCP adapter |
| `estimate-mining-profitability` | Tool `estimate_mining_profitability` |
| `connect-autopilot-a2a` | Autopilot A2A 0.3.0 (`message/send`, `tasks/get`) |
| `connect-btc-insights-mcp` | BTC Insights MCP (catalog authority) |
| `btc-hashprice-read` | `get_current_hashprice` / `get_hashprice` |
| `btc-network-overview` | `get_network_overview` |

## Protocol pins

Mirrored from Autopilot `protocol-lock/pins.yaml` @
`5d5fb3e952bbe2df50ea2453f9bb309f17796d72`:

- MCP `2025-06-18`
- A2A `0.3.0`
- `publishable: false`

BTC Insights evidence SHA: `b24e0a2704f697d7194785c14b3a5aa353228f7d`.

Details: [`docs/protocol-pins.md`](docs/protocol-pins.md).

## Hosts

See [`docs/hosts.md`](docs/hosts.md) for Cursor (primary), Claude Code (skills
clone), and docs-only notes for ChatGPT / Hermes / OpenClaw / Grok.

## Validate locally

```bash
python3 --version   # >= 3.12
python3 scripts/validate_skills.py
python3 scripts/validate_mcp_json.py
python3 scripts/validate_pins.py
```

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).

## Security

See [`SECURITY.md`](SECURITY.md) and
[`docs/security-and-provenance.md`](docs/security-and-provenance.md).
