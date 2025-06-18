from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.comment import CommentCreate, CommentOut
from app.crud.comment import get_comments_by_task, create_comment

router = APIRouter(prefix="/tasks/{task_id}/comments", tags=["Comments"])

@router.get("/", response_model=list[CommentOut])
async def list_comments(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await get_comments_by_task(db, task_id)

@router.post("/", response_model=CommentOut, status_code=201)
async def add_comment(task_id: int, comment_data: CommentCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await create_comment(db, task_id=task_id, user_id=current_user.id, comment_data=comment_data)
