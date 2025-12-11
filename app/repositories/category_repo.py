from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.schemas.category import CategoryCreate


async def get_category_by_name(db: AsyncSession, name: str) -> Category | None:
    result = await db.execute(select(Category).where(Category.name == name))
    return result.scalar_one_or_none()


async def get_all_categories(db: AsyncSession) -> list[Category]:
    result = await db.execute(select(Category))
    return list(result.scalars().all())


async def create_category(db: AsyncSession, category_in: CategoryCreate) -> Category:
    category = Category(name=category_in.name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category
