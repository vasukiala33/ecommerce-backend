from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.product_repo import add_product_images, create_product
from app.schemas.product import ProductCreate, ProductRead


async def create_seller_product(
    db: AsyncSession,
    *,
    seller_id: int,
    product_in: ProductCreate,
    image_urls: list[str] | None = None,
) -> ProductRead:
    product = await create_product(db, seller_id=seller_id, product_in=product_in)
    product = await add_product_images(db, product=product, image_urls=image_urls)
    return ProductRead.model_validate(product)
