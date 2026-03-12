from typing import List
from src.database.models import Book
from src.database.connection import get_session


def get_all_books():
    with get_session() as db:
        return db.query(Book).order_by(Book.id).all()


def get_book_by_id(book_id: int):
    with get_session() as db:
        return db.query(Book).filter(Book.id == book_id).first()


def get_book_by_title(book_title: str):
    with get_session() as db:
        return db.query(Book).filter(Book.title == book_title).first()


def add_book(book: Book):
    with get_session() as db:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book


def update_book(book: Book):
    with get_session() as db:
        data = book.model_dump(exclude={"author", "genres", "status"})
        db.query(Book).filter(Book.id == book.id).update(data)
        db.commit()
        updated = db.query(Book).filter(Book.id == book.id).first()
        return updated


def delete_book(book_id: int):
    with get_session() as db:
        db.query(Book).filter(Book.id == book_id).delete()
        db.commit()
        return {"message": f"Book {book_id} deleted successfully"}
