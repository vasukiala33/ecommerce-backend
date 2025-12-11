from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.category_repo import create_category, get_all_categories, get_category_by_name
from app.schemas.category import CategoryCreate, CategoryRead


async def create_category_service(db: AsyncSession, category_in: CategoryCreate) -> CategoryRead:
    existing = await get_category_by_name(db, category_in.name)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this name already exists",
        )

    category = await create_category(db, category_in)
    return CategoryRead.model_validate(category)


async def list_categories_service(db: AsyncSession) -> list[CategoryRead]:
    categories = await get_all_categories(db)
    return [CategoryRead.model_validate(cat) for cat in categories]
