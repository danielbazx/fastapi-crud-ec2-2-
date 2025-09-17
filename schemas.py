from typing import Optional, List
from sqlmodel import SQLModel

# User Schemas
class UserBase(SQLModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    books: List["BookRead"] = []

# Book Schemas
class BookBase(SQLModel):
    title: str
    author: str

class BookCreate(BookBase):
    user_id: int

class BookRead(BookBase):
    id: int
    user_id: int


UserRead.model_rebuild()
