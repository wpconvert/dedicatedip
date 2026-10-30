
from uuid import uuid4
from ipaddress import ip_address
from urllib.request import urlopen
from urllib.error import URLError
import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="DIH API", version="0.2.0")

sessions: dict[str, dict] = {}

ip_config = {
    "ip_address": None,
    "location": None,
    "status": "not_configured"
}


class SessionCreate(BaseModel):
    label: str = Field(default="Cloud Browser", min_length=1, max_length=64)


class IPConfig(BaseModel):
    ip_address: str


def lookup_ip(value: str):
    try:
        parsed = ip_address(value)

        if not parsed.is_global:
            raise ValueError("Gunakan IP publik yang valid.")

        url = f"https://ipwho.is/{parsed}"
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        if not data.get("success"):
            raise ValueError("Informasi lokasi IP tidak ditemukan.")

        return {
            "ip_address": str(parsed),
            "country": data.get("country"),
            "country_code": data.get("country_code"),
            "city": data.get("city"),
            "region": data.get("region"),
            "isp": data.get("connection", {}).get("isp")
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except (URLError, TimeoutError):
        raise HTTPException(
            status_code=502,
            detail="Layanan pemeriksaan IP tidak dapat dihubungi."
        )


@app.get("/health")
def health():
    return {
        "service": "dedicated-ip-homemade",
        "status": "ok"
    }


@app.get("/api/ip-config")
def get_ip_config():
    return ip_config


@app.post("/api/ip-config/check")
def check_ip_config(payload: IPConfig):
    return lookup_ip(payload.ip_address)


@app.put("/api/ip-config")
def save_ip_config(payload: IPConfig):
    location = lookup_ip(payload.ip_address)

    ip_config.update({
        "ip_address": location["ip_address"],
        "location": location,
        "status": "configured_not_connected"
    })

    return ip_config


@app.post("/api/sessions", status_code=201)
def create_session(payload: SessionCreate):
    session_id = uuid4().hex

    sessions[session_id] = {
        "id": session_id,
        "label": payload.label,
        "status": "provisioning",
        "note": "Browser worker integration is pending."
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
