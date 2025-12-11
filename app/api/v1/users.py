from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.user import UserRead, UserRoleAssign
from app.services.auth_service import change_user_role

router = APIRouter()


@router.post("/role", response_model=UserRead)
async def assign_user_role(role_assign: UserRoleAssign, db: AsyncSession = Depends(get_db)) -> UserRead:
    """Assign or change a user's role (customer/admin/seller) using name, email, and role in the body."""
    return await change_user_role(db, role_assign)
