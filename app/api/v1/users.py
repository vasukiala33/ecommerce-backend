from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.user import UserRead, UserRoleAssign
from app.services.auth_service import change_user_role

router = APIRouter()


@router.post("/role", response_model=UserRead)
async def assign_user_role(
    role_assign: UserRoleAssign,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> UserRead:
    """Assign or change a user's role (customer/admin/seller) using name, email, and role in the body.

    Any authenticated user can call this. In production you may want to restrict to admins only.
    """

    return await change_user_role(db, role_assign)
