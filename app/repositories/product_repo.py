from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product, ProductImage
from app.schemas.product import ProductCreate


async def create_product(db: AsyncSession, *, seller_id: int, product_in: ProductCreate) -> Product:
    product = Product(
        name=product_in.name,
        description=product_in.description,
        price=product_in.price,
        stock=product_in.stock,
        seller_id=seller_id,
        category_id=product_in.category_id,
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def add_product_images(
    db: AsyncSession,
    *,
    product: Product,
    image_urls: list[str] | None = None,
) -> Product:
    if not image_urls:
        return product

    for url in image_urls:
        db.add(ProductImage(product_id=product.id, image_url=url))

    await db.commit()
    await db.refresh(product)
    return product
