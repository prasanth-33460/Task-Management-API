from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    comment_text: str

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    id: int
    task_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
