from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from typing import Annotated

import sys
sys.path.append('../')

from our_utils.our_utils import register
register('payment')

app = FastAPI()

class Payment(BaseModel):
    user_id: int
    payment_id: int
    amount: float
    item: str

@app.get('/')
def default_get():
    print('get')

@app.post('/json/')
def default_post(payment: Payment):
    print(f'{payment=}')

@app.post('/form_type/')
def default_post(user_id: Annotated[int, Form()], payment_id: Annotated[int, Form()], amount: Annotated[float, Form()], item: Annotated[str, Form()]):
    print(user_id, payment_id, amount, item)
