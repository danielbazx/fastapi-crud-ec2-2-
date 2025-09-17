from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.database import get_session
from app import crud
from app.schemas import UserCreate, UserRead, BookCreate, BookRead

router = APIRouter()

# Rutas Users
@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user)

@router.get("/users/", response_model=List[UserRead])
def read_users(session: Session = Depends(get_session)):
    return crud.get_users(session)

# Rutas Books
@router.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    return crud.create_book(session, book)

@router.get("/books/", response_model=List[BookRead])
def read_books(session: Session = Depends(get_session)):
    return crud.get_books(session)
