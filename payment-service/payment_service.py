from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def default_get():
    ...

@app.post('/')
def default_post():
    ...
