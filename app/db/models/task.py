from sqlalchemy import String, Text, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.db.base_class import Base

class TaskStatus(PyEnum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskPriority(PyEnum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    assigned_to: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.todo)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), default=TaskPriority.medium)
    due_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    project = relationship("Project", backref="tasks")
    assignee = relationship("User", backref="assigned_tasks", foreign_keys=[assigned_to])
