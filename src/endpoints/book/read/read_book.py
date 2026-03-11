from fastapi import APIRouter, HTTPException
from src.schemas.book import Book, BookResponse, AuthorInBookResponse
from src.utils.connection import get_session

path = "/book/get"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)


@router.get("/")
async def get_book(book_id: int) -> BookResponse:
    with get_session() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        author = (
            AuthorInBookResponse(name=book.author.name)
            if book.author
            else None
        )
        return BookResponse(title=book.title, author=author)