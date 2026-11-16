Follow `AGENTS.md`.

- This repo is a host connector plugin (skills + MCP placeholders), not a server runtime.
- Skills are guidance only; enforcement is upstream and server-side.
- Use `${AUTOPILOT_MCP_URL}` / `${BTC_INSIGHTS_MCP_URL}` — never invent public FQDNs.
- Do not claim BTC Insights A2A runtime support or marketplace readiness.
- Run `python3 scripts/validate_skills.py`, `validate_mcp_json.py`, and `validate_pins.py` before proposing changes.
