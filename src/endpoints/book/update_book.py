from fastapi import APIRouter
from src.schemas.book_schemas import BookResponse, BookUpdate
from src.endpoints.book.response import error_responses
from src.services.books_service import update_book_service

path = "/book/update"
tags = ["book"]
router = APIRouter()


@router.patch(path=path, response_model=BookResponse, responses=error_responses, tags=tags)
async def update_book(new_book: BookUpdate):
    book = update_book_service(new_book)
    return BookResponse(book=book)
