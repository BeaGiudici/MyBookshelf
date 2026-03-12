from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.book import Book, BookUpdate
from src.utils.connection import get_session
from src.endpoints.book.update.response import error_responses
from src.endpoints.book.read.read_book import get_book_by_id

path = "/book/update"
tags = ["book"]
router = APIRouter()

@router.patch(path=path, response_model=Book, responses=error_responses, tags=tags)
async def update_book(new_book: BookUpdate):
    with get_session() as db:
        book = await get_book_by_id(db, new_book.id)
        if book is None:
            raise HTTPException(status_code=404, detail="Book ID not found. Check if the book exists.")

        if new_book.title is not None:
            book.title = new_book.title
        if new_book.isbn is not None:
            book.isbn = new_book.isbn
        if new_book.year is not None:
            book.year = new_book.year
        if new_book.author_id is not None:
            book.author_id = new_book.author_id
        if new_book.status_id is not None:
            book.status_id = new_book.status_id
        db.commit()
        db.refresh(book)
    return book