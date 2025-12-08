from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.user import Token, UserCreate, UserRead, UserSignin
from app.services import auth_service

router = APIRouter()


@router.post("/signup", response_model=UserRead, status_code=201)
async def signup(user_in: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    return await auth_service.signup(db, user_in)


@router.post("/signin", response_model=Token)
async def signin(credentials: UserSignin, db: AsyncSession = Depends(get_db)) -> Token:
    return await auth_service.signin(db, credentials)
