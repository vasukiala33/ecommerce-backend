from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

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
        # Still make sure images relationship is loaded eagerly
        stmt = (
            select(Product)
            .options(selectinload(Product.images))
            .where(Product.id == product.id)
        )
        result = await db.execute(stmt)
        return result.scalar_one()

    for url in image_urls:
        db.add(ProductImage(product_id=product.id, image_url=url))

    await db.commit()

    stmt = (
        select(Product)
        .options(selectinload(Product.images))
        .where(Product.id == product.id)
    )
    result = await db.execute(stmt)
    product_with_images = result.scalar_one()
    return product_with_images


async def get_products_by_category(
    db: AsyncSession,
    *,
    category_id: int,
) -> list[Product]:
    stmt = (
        select(Product)
        .options(selectinload(Product.images))
        .where(Product.category_id == category_id)
    )
    result = await db.execute(stmt)
    products = result.scalars().all()
    return list(products)
