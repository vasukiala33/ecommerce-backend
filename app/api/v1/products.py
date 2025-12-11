from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import create_seller_product

router = APIRouter()


@router.post("/seller", response_model=ProductRead, status_code=201)
async def create_product_for_seller(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ProductRead:
    """Create a product for the authenticated seller.

    The seller_id is taken from the JWT token (current user), not from the request body.
    """

    if current_user.role != "seller":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only sellers can create products",
        )

    # Use the authenticated user's id as seller_id
    return await create_seller_product(db, seller_id=current_user.id, product_in=product_in)
