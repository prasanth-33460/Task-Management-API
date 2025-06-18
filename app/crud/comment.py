from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import Select
from collections.abc import Sequence
from app.db.models.task_comment import TaskComment
from app.schemas.comment import CommentCreate
from typing import Tuple

async def get_comments_by_task(db: AsyncSession, task_id: int) -> Sequence[TaskComment]:
    stmt: Select[Tuple[TaskComment]] = select(TaskComment).where(TaskComment.task_id == task_id)
    result = await db.execute(stmt)
    return result.scalars().all()

async def create_comment(db: AsyncSession, task_id: int, user_id: int, comment_data: CommentCreate) -> TaskComment:
    comment = TaskComment(
        task_id=task_id,
        user_id=user_id,
        comment_text=comment_data.comment_text
    )
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment
