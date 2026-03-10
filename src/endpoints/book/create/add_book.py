from fastapi import APIRouter
from src.schemas.book import Book
from src.utils.connection import get_session

path = "/book/create"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)

@router.post("/")
async def add_book(book: Book) -> Book:
    book = Book(
        title=book.title,
        isbn=book.isbn,
        year=book.year,
    )
    with get_session() as db:
        db.add(book)
        db.commit()
        db.refresh(book)
    return book