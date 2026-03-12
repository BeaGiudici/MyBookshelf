from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.book import Book
from src.utils.connection import get_session

path = "/book/update"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)

@router.put("/")
async def update_book(new_book: Book) -> Book:
    with get_session() as db:
        existing_book = db.get(Book, new_book.id)
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")
        existing_book.title = new_book.title
        existing_book.isbn = new_book.isbn
        existing_book.year = new_book.year
        db.commit()
        db.refresh(existing_book)
    return existing_book