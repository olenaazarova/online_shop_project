from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    price: float
    quantity: int


class ItemResponse(ItemCreate):
    id: str