from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ProjectStatus(str, Enum):
    active = "active"
    completed = "completed"
    archived = "archived"

class ProjectBase(BaseModel):
    name: str
    description: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: ProjectStatus | None = None

class ProjectOut(ProjectBase):
    id: int
    owner_id: int
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
