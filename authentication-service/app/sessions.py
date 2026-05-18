import time
from uuid import uuid4

import jwt
import redis
from redis.sentinel import Sentinel

from app.settings import settings


def redis_client():
    if settings.redis_sentinels:
        sentinels = [
            (host.strip(), int(port))
            for host, port in (node.split(":") for node in settings.redis_sentinels.split(","))
        ]
        sentinel = Sentinel(sentinels, socket_timeout=1, decode_responses=True)
        return sentinel.master_for(settings.redis_master_name, socket_timeout=1)

    return redis.from_url(settings.redis_url, decode_responses=True)


client = redis_client()


def wait_for_redis() -> None:
    for attempt in range(1, 21):
        try:
            client.ping()
            return
        except redis.RedisError:
            if attempt == 20:
                raise
            time.sleep(1.5)


def create_session(user: dict) -> dict:
    session_id = str(uuid4())
    payload = {
        "sub": user["id"],
        "email": user["email"],
        "sid": session_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + settings.jwt_ttl_seconds,
    }
    token = jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
    client.setex(f"auth-session:{session_id}", settings.jwt_ttl_seconds, user["id"])
    return {"token": token, "expires_in": settings.jwt_ttl_seconds}


def validate_session(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None

    if not client.get(f"auth-session:{payload['sid']}"):
        return None

    return {"user_id": payload["sub"], "email": payload["email"], "session_id": payload["sid"]}


def destroy_session(session_id: str) -> None:
    client.delete(f"auth-session:{session_id}")
