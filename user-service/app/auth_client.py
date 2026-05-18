import json
import urllib.request

from fastapi import HTTPException

from app.settings import settings


def validate_token(token: str) -> dict:
    request = urllib.request.Request(
        f"{settings.auth_service_url}/api/auth/validate",
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
