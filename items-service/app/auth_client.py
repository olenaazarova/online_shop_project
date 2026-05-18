import json
import urllib.request
import os

from fastapi import HTTPException


AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service-1:8000")


def validate_token(token: str) -> dict:
    request = urllib.request.Request(
        f"{AUTH_SERVICE_URL}/api/auth/validate",
        headers={"Authorization": f"Bearer {token}"},
        method="POST",
    )
    try:
        response = urllib.request.urlopen(request, timeout=5)
        payload = json.loads(response.read().decode())
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    if not payload.get("active"):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload["user"]