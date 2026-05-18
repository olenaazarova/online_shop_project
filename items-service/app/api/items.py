from fastapi import APIRouter, Depends, Header, HTTPException
from app.auth_client import validate_token
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.services.item_service import ItemService

router = APIRouter(tags=["Items"])


def current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing bearer token")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Missing bearer token")
    return validate_token(token)


@router.get("/", response_model=list[ItemResponse])
async def get_items():
    return await ItemService.get_all_items()

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    return await ItemService.get_item_by_id(item_id)


@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, user: dict = Depends(current_user)):
    return await ItemService.create_item(item)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: ItemCreate, user: dict = Depends(current_user)):
    return await ItemService.update_item(item_id, item)


@router.delete("/{item_id}")
async def delete_item(item_id: str, user: dict = Depends(current_user)):
    return await ItemService.delete_item(item_id)