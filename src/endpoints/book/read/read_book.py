from fastapi import APIRouter, HTTPException
from src.schemas.book import Book
from src.utils.connection import get_session
from src.endpoints.book.read.response import error_responses
from sqlmodel import Session

path = "/book/get"
tags = ["book"]
router = APIRouter()


async def get_book_by_id(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get(path=path, response_model=Book, responses=error_responses, tags=tags)
async def get_book(book_id: int):
    with get_session() as db:
        book = get_book_by_id(db, book_id)
    return book