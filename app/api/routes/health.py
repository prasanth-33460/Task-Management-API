from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.db.models.user import User

router = APIRouter()

@router.get("/healthz/public", tags=["Health"])
async def public_health_check():
    return {"status": "ok", "message": "public check passed"}

@router.get("/healthz", tags=["Health"])
async def authenticated_health_check(current_user: User = Depends(get_current_user)):
    return {"status": "ok", "user": current_user.email}