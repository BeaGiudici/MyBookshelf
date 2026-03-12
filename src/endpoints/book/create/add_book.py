from fastapi import APIRouter, HTTPException
from src.schemas.book import Book
from src.schemas.book_genre_link import BookGenreLink
from src.schemas.author import Author
from src.schemas.genre import Genre
from src.schemas.status import Status
from src.utils.connection import get_session

path = "/book/create"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)


@router.post("/")
async def add_book(new_book: Book) -> dict:
    with get_session() as db:
        db.add(new_book)
        db.commit()
    return {'message': 'Book created successfully'}