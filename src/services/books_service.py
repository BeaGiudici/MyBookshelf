from src.repositories.books_repo import (
    get_all_books,
    get_book_by_id,
    get_book_by_title,
    add_book as add_book_repo,
    update_book,
    delete_book,
)
from src.repositories.authors_repo import get_author_by_id
from src.database.models import Book
from src.schemas.book_schemas import BookCreate, BookUpdate
from fastapi import HTTPException


def get_all_books_service():
    books = get_all_books()
    if books is None:
        raise HTTPException(status_code=404, detail="No books found.")
    return books


def get_book_by_id_service(book_id: int):
    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found."
        )
    return book


def get_book_by_title_service(book_title: str):
    book = get_book_by_title(book_title)
    if book is None:
        raise HTTPException(
            status_code=404, detail=f"Book with title {book_title} not found."
        )
    return book


def add_book_service(new_book: BookCreate):
    if (
        new_book.title is None
        or new_book.isbn is None
        or new_book.year is None
        or new_book.author_id is None
        or new_book.status_id is None
    ):
        raise HTTPException(status_code=400, detail="Missing required fields")

    existing = get_book_by_title(new_book.title)
    if existing is not None:
        raise HTTPException(status_code=400, detail="Book already exists.")

    author = get_author_by_id(new_book.author_id)
    if author is None:
        raise HTTPException(status_code=400, detail="Author not found.")

    book = Book(
        title=new_book.title,
        isbn=new_book.isbn,
        year=new_book.year,
        author_id=new_book.author_id,
        status_id=new_book.status_id,
    )
    return add_book_repo(book)


def update_book_service(book_update: BookUpdate):
    if book_update.id is not None:
        book = get_book_by_id_service(book_update.id)
    elif book_update.title is not None:
        book = get_book_by_title_service(book_update.title)
    else:
        raise HTTPException(
            status_code=400,
            detail="Missing required fields. Provide either ID or title.",
        )

    if book_update.title is not None:
        book.title = book_update.title
    if book_update.isbn is not None:
        book.isbn = book_update.isbn
    if book_update.year is not None:
        book.year = book_update.year
    if book_update.author_id is not None:
        book.author_id = book_update.author_id
    if book_update.status_id is not None:
        book.status_id = book_update.status_id

    return update_book(book)


def delete_book_service(book_id: int):
    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    msg = delete_book(book_id)
    return msg
