from fastapi import APIRouter
from src.schemas.book_schemas import BooksResponse
from src.services.books_service import get_all_books_service
from src.endpoints.book.response import error_responses

path = "/book/get/all"
tags = ["book"]
router = APIRouter()


@router.get(path=path, response_model=BooksResponse, responses=error_responses, tags=tags)
async def get_books():
    books = get_all_books_service()
    return BooksResponse(books=books)
