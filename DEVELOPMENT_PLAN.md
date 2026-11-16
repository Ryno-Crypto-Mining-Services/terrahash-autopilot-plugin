# DEVELOPMENT_PLAN — terrahash-autopilot-plugin

Repo-local milestones only (not Autopilot WP numbering).

**Upstream evidence SHAs (bump deliberately):**

| Upstream | SHA |
|---|---|
| terrahash-autopilot | `5d5fb3e952bbe2df50ea2453f9bb309f17796d72` |
| btc-insights-mcp-server | `b24e0a2704f697d7194785c14b3a5aa353228f7d` |

| Milestone | Work packages | Exit criteria |
|---|---|---|
| **P0 — Evidence baseline** | Record target + upstream SHAs; proposal approved | Elvis approval recorded |
| **P1 — Scaffold merge** | Files per proposal §4–§5; CI green on validators | Public `main` installable as Cursor plugin with placeholders; README honesty |
| **P2 — Host docs hardening** | Expand `docs/hosts.md` for Claude/ChatGPT/Hermes/OpenClaw/Grok using verified MCP/A2A client patterns only | No invented FQDNs; Tailscale pattern as operator-private |
| **P3 — Skill coverage ratchet** | Add skills only when upstream tools are stable and host-useful | Each skill cites catalog/tool id + upstream SHA; validator allowlist updated |
| **P4 — Endpoint binding** | Replace placeholders when approved FQDNs / Tunnel / Access exist | Variables documented; no unpaid origin bypass |
| **P5 — Distribution** | Marketplace / dual Agent Plugin manifest / release tags | Explicit Elvis go |

Alignment: supports founder **Phase C (dual MCP+A2A host connectors)**. Does not
implement Phase A agents, Phase B x402, or Nexus UI. Does not enable ans-registry
Helm or registry publication from this repository.
