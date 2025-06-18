from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority = TaskPriority.medium
    due_date: datetime | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: TaskPriority | None = None
    status: TaskStatus | None = None
    due_date: datetime | None = None

class TaskOut(TaskBase):
    id: int
    project_id: int
    assigned_to: int | None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
