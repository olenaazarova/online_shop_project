from fastapi import APIRouter

from app.schemas.item_schema import (
    ItemCreate,
    ItemResponse
)

from app.services.item_service import ItemService

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post(
    "/",
    response_model=ItemResponse
)
async def create_item(item: ItemCreate):
    return await ItemService.create_item(item)


@router.get(
    "/",
    response_model=list[ItemResponse]
)
async def get_items():
    return await ItemService.get_all_items()


@router.get(
    "/{item_id}",
    response_model=ItemResponse
)
async def get_item(item_id: str):
    return await ItemService.get_item_by_id(item_id)


@router.put(
    "/{item_id}",
    response_model=ItemResponse
)
async def update_item(
    item_id: str,
    item: ItemCreate
):
    return await ItemService.update_item(
        item_id,
        item
    )


@router.delete("/{item_id}")
async def delete_item(item_id: str):
    return await ItemService.delete_item(item_id)