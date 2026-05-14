from fastapi import FastAPI, Form

app = FastAPI()

@app.get('/')
def default_get():
    print('get')

