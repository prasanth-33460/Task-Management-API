import asyncio
from app.db.session import get_db
from app.db.models.user import User, UserRole
from sqlalchemy import select
from app.core.security import get_password_hash

async def create_admin_user():
    async for db in get_db():
        result = await db.execute(select(User).where(User.email == "admin@example.com"))
        existing = result.scalar_one_or_none()
        if not existing:
            admin = User(
                email="admin@example.com",
                hashed_password=get_password_hash("admin123"),
                full_name="Admin User",
                role=UserRole.admin
            )
            db.add(admin)
            await db.commit()
            print("Admin user created")

if __name__ == "__main__":
    asyncio.run(create_admin_user())
