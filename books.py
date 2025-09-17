from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import Book
from app.database import get_session

router = APIRouter()


@router.post("/")
def create_book(book: Book, session: Session = Depends(get_session)):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@router.get("/")
def get_books(session: Session = Depends(get_session)):
    books = session.exec(select(Book)).all()
    return books
