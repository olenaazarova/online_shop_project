from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from typing import Annotated

from payment_repository import initialize_database, save_payment

app = FastAPI()

class Payment(BaseModel):
    user_id: int
    payment_id: int
    amount: float
    item: str

@app.on_event("startup")
def startup():
    initialize_database()

@app.get('/')
def default_get():
    print('get')
    return {"status": "ok", "service": "payment-service"}

@app.post('/json/')
def default_post(payment: Payment):
    save_payment(payment)
    return {"status": "accepted", "payment": payment}

@app.post('/form_type/')
def default_post(user_id: Annotated[int, Form()], payment_id: Annotated[int, Form()], amount: Annotated[float, Form()], item: Annotated[str, Form()]):
    payment = Payment(user_id=user_id, payment_id=payment_id, amount=amount, item=item)
    save_payment(payment)
    return {"status": "accepted", "payment": payment}
