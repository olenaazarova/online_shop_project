from fastapi import HTTPException

from app.events.producer import EventProducer
from app.repositories.item_repository import ItemRepository


class ItemService:

    @staticmethod
    async def create_item(item_data):

        if item_data.price < 0:
            raise HTTPException(
                status_code=400,
                detail="Price cannot be negative"
            )

        if item_data.quantity < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity cannot be negative"
            )

        item = await ItemRepository.create(item_data)

        EventProducer.publish_event(
            "ITEM_CREATED",
            item
        )

        return item

    @staticmethod
    async def get_all_items():
        return await ItemRepository.get_all()

    @staticmethod
    async def get_item_by_id(item_id: str):

        item = await ItemRepository.get_by_id(item_id)

        if not item:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        return item

    @staticmethod
    async def delete_item(item_id: str):

        existing_item = await ItemRepository.get_by_id(item_id)

        if not existing_item:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        result = await ItemRepository.delete(item_id)

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=500,
                detail="Failed to delete item"
            )

        EventProducer.publish_event(
            "ITEM_DELETED",
            {
                "id": item_id
            }
        )

        return {
            "message": "Item deleted successfully"
        }

    @staticmethod
    async def update_item(item_id: str, item_data):

        existing_item = await ItemRepository.get_by_id(item_id)

        if not existing_item:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        if item_data.price < 0:
            raise HTTPException(
                status_code=400,
                detail="Price cannot be negative"
            )

        updated_item = await ItemRepository.update(
            item_id,
            item_data
        )

        EventProducer.publish_event(
            "ITEM_UPDATED",
            updated_item
        )

        return updated_item