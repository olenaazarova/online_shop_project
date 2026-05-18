import requests, json, sys

def load_conf():
    with open('../conf.txt') as file:
        con = file.read()
    return con

config_addr = 'http://' + load_conf()

def register(name):
    port = sys.argv[-1]
    assert port.isnumeric()
    requests.post(config_addr, json={'name': name, 'port': port})

def discover(name):
    return json.loads(requests.get(f"{config_addr}/{name}")._content.decode())
