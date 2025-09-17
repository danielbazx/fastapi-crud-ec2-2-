from sqlmodel import Session, select
from app.models import User, Book
from app.schemas import UserCreate, BookCreate

# User CRUD
def create_user(session: Session, user: UserCreate):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_users(session: Session):
    return session.exec(select(User)).all()

# Book CRUD
def create_book(session: Session, book: BookCreate):
    db_book = Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def get_books(session: Session):
    return session.exec(select(Book)).all()
