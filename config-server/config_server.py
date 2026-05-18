from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
config = {}

class Register(BaseModel):
    name: str
    port: int

@app.post('/')
def register_service(register: Register, request: Request):

    addr = request.scope['client'][0]
    name = register.name

    full_addr = f'{addr}:{register.port}'
    if name not in config:
        config[name] = [full_addr]
    elif name in config and full_addr not in config[name]:
        config[name].append(full_addr)

@app.get('/{name}')
def get_addr(name: str):
    return config[name]

@app.get('/')
def dafult_get():
    return config
