from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate


async def create_product(db: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(
        name=product_in.name,
        description=product_in.description,
        price=product_in.price,
        stock=product_in.stock,
        seller_id=product_in.seller_id,
        category_id=product_in.category_id,
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product
