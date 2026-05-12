from fastapi import FastAPI

from app.api.items import router as items_router

app = FastAPI(
    title="Items Service"
)

app.include_router(items_router)


@app.get("/")
def root():
    return {
        "message": "Items Service Running"
    }