from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import create_seller_product

router = APIRouter()


@router.post("/seller", response_model=ProductRead, status_code=201)
async def create_product_for_seller(product_in: ProductCreate, db: AsyncSession = Depends(get_db)) -> ProductRead:
    """Create a product for a seller.

    For now, seller_id is taken from the request body. Later we can derive it from the authenticated user.
    """
    return await create_seller_product(db, product_in)
