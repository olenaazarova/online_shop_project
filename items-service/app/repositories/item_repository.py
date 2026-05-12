from bson import ObjectId
from app.db.database import items_collection


class ItemRepository:

    @staticmethod
    async def create(item_data):
        item = item_data.model_dump()

        result = await items_collection.insert_one(item)

        item["id"] = str(result.inserted_id)
        item.pop("_id", None)

        return item

    @staticmethod
    async def get_all():
        items = []

        async for item in items_collection.find():
            item["id"] = str(item["_id"])
            item.pop("_id", None)  # 🔥 IMPORTANT FIX
            items.append(item)

        return items

    @staticmethod
    async def get_by_id(item_id: str):

        item = await items_collection.find_one({
            "_id": ObjectId(item_id)
        })

        if not item:
            return None

        item["id"] = str(item["_id"])
        item.pop("_id", None)  # 🔥 IMPORTANT FIX

        return item

    @staticmethod
    async def delete(item_id: str):

        return await items_collection.delete_one({
            "_id": ObjectId(item_id)
        })

    @staticmethod
    async def update(item_id: str, new_data):

        update_data = new_data.model_dump(exclude_unset=True)

        await items_collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": update_data}
        )

        item = await items_collection.find_one({
            "_id": ObjectId(item_id)
        })

        if not item:
            return None

        item["id"] = str(item["_id"])
        item.pop("_id", None)

        return item