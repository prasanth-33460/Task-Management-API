from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectOut
from app.db.models.user import User, UserRole
from app.crud.project import get_projects, get_project, create_project, update_project, delete_project

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=list[ProjectOut])
async def list_projects(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await get_projects(db, owner_id=current_user.id)

@router.post("/", response_model=ProjectOut, status_code=201)
async def create_new_project(project_data: ProjectCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.admin, UserRole.manager]:
        raise HTTPException(status_code=403, detail="Only managers or admins can create projects")
    return await create_project(db, project_data=project_data, owner_id=current_user.id)

@router.get("/{project_id}", response_model=ProjectOut)
async def read_project(project_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = await get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectOut)
async def update_existing_project(project_id: int, updates: ProjectUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = await get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.owner_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not authorized to update this project")
    return await update_project(db, project, updates)

@router.delete("/{project_id}", status_code=204)
async def remove_project(project_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = await get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.owner_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not authorized to delete this project")
    await delete_project(db, project)
    return
