# DEDICATED IP HOMEMADE (DIH)

Cloud-browser project scaffold.

## Architecture
- `panel/`: static dashboard hosted on GitHub Pages.
- `backend/`: FastAPI control API.
- `browser-engine/`: isolated Chromium worker container.
- `database/`: database schema and migrations.
- `infra/`: deployment configuration and operational notes.

## Important
The dashboard is only the user interface. A cloud server must run the backend and browser engine.
A target IP address is not itself a proxy. To make browser traffic exit through a particular public IP,
DIH must use a proxy/VPN gateway that you own or are authorized to use.

This scaffold is a starting structure, not a production-ready deployment. Before public use,
configure authentication, TLS, session limits, network isolation, outbound destination controls,
secret storage, logging, and resource limits.

## Local development
See `backend/README.md` and `browser-engine/README.md`.
