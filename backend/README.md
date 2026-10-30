# Backend API

FastAPI control plane for DIH.

Initial API scaffold:
- `GET /health`: service health.
- `POST /api/sessions`: create a session record (placeholder until worker integration).
- `DELETE /api/sessions/{session_id}`: close a session record.

Before exposing this API publicly, add real user authentication, authorization,
rate limiting, CSRF/origin controls where applicable, TLS, audit logs, and session ownership.
