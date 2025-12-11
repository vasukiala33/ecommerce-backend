from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.category import CategoryCreate, CategoryRead
from app.services.category_service import create_category_service, list_categories_service

router = APIRouter()


@router.post("/create-categories", response_model=CategoryRead, status_code=201)
async def create_category(category_in: CategoryCreate, db: AsyncSession = Depends(get_db)) -> CategoryRead:
    return await create_category_service(db, category_in)


@router.get("/", response_model=List[CategoryRead])
async def list_categories(db: AsyncSession = Depends(get_db)) -> List[CategoryRead]:
    return await list_categories_service(db)
