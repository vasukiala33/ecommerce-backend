from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import User
from app.repositories.user_repo import create_user, get_user_by_email, get_user_by_id, update_user_role
from app.schemas.user import Token, UserCreate, UserRead, UserRole, UserRoleAssign, UserRoleUpdate, UserSignin


async def signup(db: AsyncSession, user_in: UserCreate) -> UserRead:
    existing = await get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    hashed_password = get_password_hash(user_in.password)
    # New users default to 'customer' role
    user: User = await create_user(db, name=user_in.name, email=user_in.email, hashed_password=hashed_password, role="customer")
    return UserRead.model_validate(user)


async def signin(db: AsyncSession, credentials: UserSignin) -> Token:
    user = await get_user_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.id, expires_delta=access_token_expires)
    return Token(access_token=access_token)


async def change_user_role(db: AsyncSession, role_assign: UserRoleAssign) -> UserRead:
    # Find user by email; name is included mainly for client context and can be used for extra checks if desired
    user = await get_user_by_email(db, role_assign.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    updated = await update_user_role(db, user, role_assign.role)
    return UserRead.model_validate(updated)
