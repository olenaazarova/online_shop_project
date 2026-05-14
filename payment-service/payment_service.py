from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    user_id: int
    payment_id: int
    amount: float
    item: str

@app.get('/')
def default_get():
    print('get')

@app.post('/')
def default_post(payment: Payment):
    print(f'{payment=}')
