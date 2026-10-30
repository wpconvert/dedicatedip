# Database

Planned tables:
- users
- browser_sessions
- proxy_gateways (references/secrets stored securely, not plaintext)
- session_events

Use migrations and enforce that users can access only their own sessions.
