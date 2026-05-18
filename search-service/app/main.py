from fastapi import FastAPI
import threading

from app.api.search import router as search_router
from app.consumers.item_consumer import start_consumer

app = FastAPI(
    title="Search Service"
)

app.include_router(search_router)


@app.on_event("startup")
def startup_event():

    thread = threading.Thread(target=start_consumer)
    thread.start()


@app.get("/")
def root():
    return {
        "message": "Search Service Running"
    }