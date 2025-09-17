from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    books: List["Book"] = Relationship(back_populates="owner")


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    owner_id: int = Field(default=None, foreign_key="user.id")

    owner: Optional[User] = Relationship(back_populates="books")
