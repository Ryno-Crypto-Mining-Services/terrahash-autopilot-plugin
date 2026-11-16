# Security Policy

## Supported versions

This repository publishes guidance and Cursor plugin assets only (no network
server). Treat the default branch as the supported surface.

## Reporting a vulnerability

Prefer **GitHub private vulnerability reporting** on this repository
(Security → Report a vulnerability) when available.

Do not open a public issue with secrets, credentials, customer data, or
exploit detail. Do not invent an email contact in this file.

## Scope notes

- Skills and prompts are **not** authorization. Upstream Autopilot / BTC Insights
  enforce policy server-side.
- Never commit `.env` files, API keys, tokens, or private endpoint credentials.
- MCP URLs in-repo are placeholders or documented patterns only.
