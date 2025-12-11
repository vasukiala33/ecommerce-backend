from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/", summary="Health check")
async def health_check(current_user: User = Depends(get_current_user)) -> dict:
    return {"status": "ok"}
