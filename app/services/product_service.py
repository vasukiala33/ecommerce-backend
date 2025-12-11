from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.product_repo import create_product
from app.schemas.product import ProductCreate, ProductRead


async def create_seller_product(db: AsyncSession, *, seller_id: int, product_in: ProductCreate) -> ProductRead:
    product = await create_product(db, seller_id=seller_id, product_in=product_in)
    return ProductRead.model_validate(product)
