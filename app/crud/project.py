from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from collections.abc import Sequence
from app.db.models.project import Project, ProjectStatus
from app.schemas.project import ProjectCreate, ProjectUpdate

async def get_projects(db: AsyncSession, owner_id: int) -> Sequence[Project]:
    result = await db.execute(select(Project).where(Project.owner_id == owner_id))
    return result.scalars().all()

async def get_project(db: AsyncSession, project_id: int) -> Project | None:
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalar_one_or_none()

async def create_project(db: AsyncSession, project_data: ProjectCreate, owner_id: int) -> Project:
    project = Project(
        name=project_data.name,
        description=project_data.description,
        owner_id=owner_id,
        status=ProjectStatus.active
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

async def update_project(db: AsyncSession, project: Project, updates: ProjectUpdate) -> Project:
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(project, field, value)
    await db.commit()
    await db.refresh(project)
    return project

async def delete_project(db: AsyncSession, project: Project):
    await db.delete(project)
    await db.commit()
