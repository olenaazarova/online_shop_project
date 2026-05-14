from fastapi import FastAPI, Form
import time

time.sleep(2)

import sys
sys.path.append('../')

from our_utils.our_utils import discover
payment_urls = discover('payment')
print(f'{payment_urls=}')

app = FastAPI()

@app.get('/')
def default_get():
    print('get')

