from fastapi import FastAPI, Request, Form, Depends, Header, HTTPException
from pydantic import BaseModel
from typing import Annotated
import json, urllib.request, os

from payment_repository import initialize_database, save_payment

app = FastAPI()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service-1:8000")

def current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing bearer token")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    req = urllib.request.Request(
        f"{AUTH_SERVICE_URL}/api/auth/validate",
        headers={"Authorization": f"Bearer {token}"},
        method="POST",
    )
    try:
        response = urllib.request.urlopen(req, timeout=5)
        payload = json.loads(response.read().decode())
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    if not payload.get("active"):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload["user"]
class Payment(BaseModel):
    user_id: int
    payment_id: int
    amount: float
    item: str

@app.on_event("startup")
def startup():
    initialize_database()

@app.get('/')
def default_get(user: dict = Depends(current_user)):
    print('get')
    return {"status": "ok", "service": "payment-service"}

@app.post('/json/')
def default_post(payment: Payment, user: dict = Depends(current_user)):
    save_payment(payment)
    return {"status": "accepted", "payment": payment}

@app.post('/form_type/')
def default_post(user_id: Annotated[int, Form()], payment_id: Annotated[int, Form()], amount: Annotated[float, Form()], item: Annotated[str, Form()], user: dict = Depends(current_user)):
    payment = Payment(user_id=user_id, payment_id=payment_id, amount=amount, item=item)
    save_payment(payment)
    return {"status": "accepted", "payment": payment}
