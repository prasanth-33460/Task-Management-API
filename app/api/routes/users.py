from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.db.models.user import User
from app.schemas.user import UserUpdate, UserOut

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserOut)
async def update_profile(update_data: UserUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if update_data.full_name:
        current_user.full_name = update_data.full_name
    if update_data.password:
        from app.core.security import get_password_hash
        current_user.hashed_password = get_password_hash(update_data.password)

    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    return current_user
