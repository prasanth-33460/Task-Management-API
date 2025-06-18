from pydantic import BaseModel, EmailStr
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str
    role: Role = Role.user

class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None

class UserOut(UserBase):
    id: int
    role: Role
    is_active: bool

    class Config:
        from_attributes = True
