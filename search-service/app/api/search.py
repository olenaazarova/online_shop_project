from fastapi import APIRouter

from app.db.database import search_collection

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search_items(q: str):

    results = []

    cursor = search_collection.find(
        {
            "title": {
                "$regex": q,
                "$options": "i"
            }
        }
    )

    for item in cursor:

        item["_id"] = str(item["_id"])

        results.append(item)

    return results