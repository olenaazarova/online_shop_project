import urllib.request
import json

import psycopg
from fastapi import HTTPException

from app import repository
from app.passwords import hash_password, verify_password
from app.schemas import LoginRequest, RegisterRequest
from app.sessions import create_session, destroy_session, validate_session
from app.settings import settings


def register(payload: RegisterRequest) -> dict:
    if repository.find_by_email(payload.email):
        raise HTTPException(status_code=409, detail="Email already registered")

    user = repository.create_credentials(payload.email, hash_password(payload.password))

    try:
        create_profile(
            {
                "auth_user_id": user["id"],
                "email": user["email"],
                "first_name": payload.first_name,
                "last_name": payload.last_name,
                "phone": payload.phone,
            }
        )
    except Exception:
        repository.delete_by_id(user["id"])
        raise

    return {"user": user, **create_session(user)}


def login(payload: LoginRequest) -> dict:
    user = repository.find_by_email(payload.email)
    if not user or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    public_user = {"id": user["id"], "email": user["email"], "created_at": user["created_at"]}
    return {"user": public_user, **create_session(public_user)}


def validate_token(token: str) -> dict | None:
    session = validate_session(token)
    if not session:
        return None

    user = repository.find_by_id(session["user_id"])
    if not user:
        return None

    return {"session": session, "user": user}


def logout(token: str) -> None:
    session = validate_session(token)
    if session:
        destroy_session(session["session_id"])


def create_profile(profile: dict) -> None:
    data = json.dumps(profile).encode()
    request = urllib.request.Request(
        f"{settings.user_service_url}/internal/users",
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-Internal-Api-Key": settings.internal_api_key,
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(request, timeout=5)
    except urllib.error.HTTPError as error:
        if error.code == 409:
            raise HTTPException(status_code=409, detail="User profile already exists")
        raise HTTPException(status_code=502, detail="User service rejected profile creation")
    except urllib.error.URLError:
        raise HTTPException(status_code=502, detail="User service unavailable")
