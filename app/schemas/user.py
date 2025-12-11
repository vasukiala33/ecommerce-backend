from typing import Literal

from pydantic import BaseModel, EmailStr


UserRole = Literal["admin", "seller", "customer"]


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserSignin(BaseModel):
    email: EmailStr
    password: str


class UserRead(UserBase):
    id: int
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserRoleUpdate(BaseModel):
    role: UserRole


class UserRoleAssign(BaseModel):
    name: str
    email: EmailStr
    role: UserRole
