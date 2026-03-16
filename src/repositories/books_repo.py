from typing import List
from src.database.models import Book
from src.database.connection import get_session
from sqlmodel import Session

def get_all_books(session: Session):
    return session.query(Book).order_by(Book.id).all()


def get_book_by_id(session: Session, book_id: int):
    return session.query(Book).filter(Book.id == book_id).first()


def get_book_by_title(session: Session, book_title: str):
    return session.query(Book).filter(Book.title == book_title).first()


def add_book(session: Session, book: Book):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def update_book(session: Session, book: Book):
    data = book.model_dump(exclude={"author", "genres", "status"})
    session.query(Book).filter(Book.id == book.id).update(data)
    session.commit()
    updated = session.query(Book).filter(Book.id == book.id).first()
    return updated


def delete_book(session: Session, book_id: int):
    session.query(Book).filter(Book.id == book_id).delete()
    session.commit()
    return {"message": f"Book {book_id} deleted successfully"}
