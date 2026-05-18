from fastapi import Depends, FastAPI, Header, HTTPException

from app.auth_client import validate_token
from app.database import initialize_database
from app.schemas import CreateProfileRequest, UpdateProfileRequest
from app.service import change_user_profile, create_user_profile, get_user_profile
from app.settings import settings

app = FastAPI(title="User Service")


def current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    return validate_token(token)


@app.on_event("startup")
def startup() -> None:
    initialize_database()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "user-service"}


@app.post("/internal/users", status_code=201)
def internal_create_user(
    payload: CreateProfileRequest,
    x_internal_api_key: str | None = Header(default=None),
) -> dict:
    if x_internal_api_key != settings.internal_api_key:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"user": create_user_profile(payload)}


@app.get("/api/users/me")
def current_profile(user: dict = Depends(current_user)) -> dict:
    return {"user": get_user_profile(user["id"])}


@app.patch("/api/users/me")
def update_profile(payload: UpdateProfileRequest, user: dict = Depends(current_user)) -> dict:
    return {"user": change_user_profile(user["id"], payload)}
