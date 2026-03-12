from fastapi import APIRouter
from src.schemas.book import Book
from src.utils.connection import get_session

path = "/book/get/all"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)


@router.get("/")
async def get_books() -> list[Book]:
    with get_session() as db:
        books = db.query(Book).order_by(Book.id).all()
    return books