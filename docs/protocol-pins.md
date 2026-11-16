# Protocol pins (mirror)

This document **mirrors** Autopilot protocol pins for host-connector consumers.
The machine-readable source of truth remains Autopilot
`protocol-lock/pins.yaml`.

## Evidence

| Field | Value |
|---|---|
| Autopilot evidence SHA | `5d5fb3e952bbe2df50ea2453f9bb309f17796d72` |
| Path | `protocol-lock/pins.yaml` |
| BTC Insights evidence SHA | `b24e0a2704f697d7194785c14b3a5aa353228f7d` |

## Pins

| Protocol | Revision | Notes |
|---|---|---|
| MCP | `2025-06-18` | Autopilot MCP adapter + BTC Insights negotiate this revision |
| A2A | `0.3.0` | Autopilot A2A adapter; BTC Insights A2A is design-only upstream |

Publication gate from Autopilot pins: **`publishable: false`**.

This plugin must not claim public catalog publication or invent registry DNS.

## Tool allowlist used by validators

Autopilot MCP (at evidence SHA): `estimate_mining_profitability`

BTC Insights catalog ids used by MVP skills:

- `get_current_hashprice`
- `get_hashprice`
- `get_hashprice_volatility` (mentioned as related; optional)
- `get_network_overview`

Bump this file and `scripts/validate_pins.py` / `validate_skills.py` together
when intentionally advancing upstream SHAs.
