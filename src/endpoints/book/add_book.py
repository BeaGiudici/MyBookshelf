from fastapi import APIRouter
from src.schemas.book_schemas import BookResponse, BookCreate
from src.endpoints.book.response import error_responses
from src.services.books_service import add_book_service

path = "/book/create"
tags = ["book"]
router = APIRouter()


@router.post(path=path, response_model=BookResponse, responses=error_responses, tags=tags)
async def add_book(new_book: BookCreate):
    book = add_book_service(new_book)
    return BookResponse(book=book)
