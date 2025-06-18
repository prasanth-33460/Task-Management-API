from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.models.user import User, UserRole
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.crud.task import (
    get_tasks_by_project,
    get_task,
    create_task,
    update_task,
    delete_task,
    assign_task,
)

router = APIRouter(prefix="/projects/{project_id}/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskOut])
async def list_tasks(project_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await get_tasks_by_project(db, project_id)

@router.post("/", response_model=TaskOut, status_code=201)
async def create_new_task(project_id: int, task_data: TaskCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await create_task(db, project_id=project_id, task_data=task_data)

@router.get("/{task_id}", response_model=TaskOut)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
async def update_existing_task(task_id: int, updates: TaskUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.assigned_to != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")
    return await update_task(db, task, updates)

@router.delete("/{task_id}", status_code=204)
async def remove_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.assigned_to != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
    await delete_task(db, task)

@router.put("/{task_id}/assign", response_model=TaskOut)
async def assign_task_to_user(task_id: int, user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.manager, UserRole.admin]:
        raise HTTPException(status_code=403, detail="Only managers or admins can assign tasks")
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await assign_task(db, task, user_id)
