import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_db
from app.core.config import settings
from app.models.user import User
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import create_seller_product

router = APIRouter()


@router.post("/seller", response_model=ProductRead, status_code=201)
async def create_product_for_seller(
    name: str = Form(...),
    description: str | None = Form(None),
    price: float = Form(...),
    stock: int = Form(0),
    category_id: int = Form(...),
    images: List[UploadFile] | None = File(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ProductRead:
    if current_user.role != "seller":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only sellers can create products",
        )

    product_in = ProductCreate(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id,
    )

    media_root = os.path.join(os.getcwd(), "media", "products")
    os.makedirs(media_root, exist_ok=True)

    image_urls: List[str] = []
    if images:
        for image in images:
            filename = f"{uuid.uuid4().hex}_{image.filename}"
            file_path = os.path.join(media_root, filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await image.read())

            public_url = f"/media/products/{filename}"
            image_urls.append(public_url)

    return await create_seller_product(
        db,
        seller_id=current_user.id,
        product_in=product_in,
        image_urls=image_urls,
    )
