from fastapi import APIRouter

from app.db.database import search_collection
from app.cache.redis_client import redis_client

import json

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search_items(q: str):

    cache_key = f"search:{q.lower()}"

    cached_data = redis_client.get(cache_key)

    if cached_data:

        print("CACHE HIT")

        return json.loads(cached_data)

    print("CACHE MISS")

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

    redis_client.setex(
        cache_key,
        60,
        json.dumps(results)
    )

    return results