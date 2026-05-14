from fastapi import Depends, FastAPI, Header, HTTPException

from app.database import initialize_database
from app.schemas import LoginRequest, RegisterRequest
from app.service import login, logout, register, validate_token
from app.sessions import wait_for_redis

app = FastAPI(title="Authentication Service")


def bearer_token(authorization: str | None = Header(default=None)) -> str:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    return token


@app.on_event("startup")
def startup() -> None:
    initialize_database()
    wait_for_redis()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "auth-service"}


@app.post("/api/auth/register", status_code=201)
def register_user(payload: RegisterRequest) -> dict:
    return register(payload)


@app.post("/api/auth/login")
def login_user(payload: LoginRequest) -> dict:
    return login(payload)


@app.post("/api/auth/logout", status_code=204)
def logout_user(token: str = Depends(bearer_token)) -> None:
    logout(token)


@app.get("/api/auth/me")
def current_auth_user(token: str = Depends(bearer_token)) -> dict:
    state = validate_token(token)
    if not state:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"user": state["user"]}


@app.post("/api/auth/validate")
def validate_current_token(token: str = Depends(bearer_token)) -> dict:
    state = validate_token(token)
    if not state:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"active": True, "user": {"id": state["user"]["id"], "email": state["user"]["email"]}}
