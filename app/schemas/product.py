from datetime import datetime

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int = 0


class ProductCreate(ProductBase):
    seller_id: int
    category_id: int


class ProductRead(ProductBase):
    id: int
    seller_id: int
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True
