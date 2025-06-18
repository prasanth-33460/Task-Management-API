from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from collections.abc import Sequence
from app.db.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

async def get_tasks_by_project(db: AsyncSession, project_id: int) -> Sequence[Task]:
    result = await db.execute(select(Task).where(Task.project_id == project_id))
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()

async def create_task(db: AsyncSession, project_id: int, task_data: TaskCreate) -> Task:
    task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        due_date=task_data.due_date,
        project_id=project_id
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def update_task(db: AsyncSession, task: Task, updates: TaskUpdate) -> Task:
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task: Task):
    await db.delete(task)
    await db.commit()

async def assign_task(db: AsyncSession, task: Task, user_id: int) -> Task:
    task.assigned_to = user_id
    await db.commit()
    await db.refresh(task)
    return task
