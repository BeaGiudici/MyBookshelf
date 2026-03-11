from fastapi import APIRouter
from src.schemas.book import Book, BookResponse, AuthorInBookResponse
from src.utils.connection import get_session

path = "/book/get"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)


@router.get("/")
async def get_books() -> list[BookResponse]:
    with get_session() as db:
        books = db.query(Book).order_by(Book.id).all()
        return [
            BookResponse(
                title=book.title,
                author=(
                    AuthorInBookResponse(name=book.author.name)
                    if book.author
                    else None
                ),
            )
            for book in books
        ]