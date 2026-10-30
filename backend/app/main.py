from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="DIH API", version="0.1.0")

# Development-only in-memory placeholder. Replace with persistent storage
# and authenticated, per-user session ownership before deployment.
sessions: dict[str, dict] = {}

class SessionCreate(BaseModel):
    label: str = Field(default="Cloud Browser", min_length=1, max_length=64)

@app.get("/health")
def health():
    return {"service": "dedicated-ip-homemade", "status": "ok"}

@app.post("/api/sessions", status_code=201)
def create_session(payload: SessionCreate):
    session_id = uuid4().hex
    sessions[session_id] = {
        "id": session_id,
        "label": payload.label,
        "status": "provisioning",
        "note": "Worker integration is not connected yet."
    }
    return sessions[session_id]

@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str):
    session = sessions.pop(session_id, None)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"id": session_id, "status": "closed"}
