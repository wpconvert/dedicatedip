# Infrastructure

Deployment target: a Linux VPS or cloud VM with Docker support.

Do not deploy the scaffold publicly as-is. Before launch:
- Put the API behind HTTPS and an authenticated reverse proxy.
- Keep Redis, browser workers, and browser-control ports private.
- Add firewall rules and outbound network restrictions.
- Configure per-user quotas, CPU/RAM limits, session expiry and cleanup.
- Store proxy credentials in a secret manager or protected environment.
- Monitor cost, abuse, crashes and resource usage.
