from fastapi import APIRouter, Depends
from src.schemas.book_schemas import BooksResponse
from src.services.books_service import get_all_books_service
from src.endpoints.book.response import error_responses
from src.database.connection import get_session
from sqlmodel import Session

path = "/book/get/all"
tags = ["book"]
router = APIRouter()


@router.get(path=path, response_model=BooksResponse, responses=error_responses, tags=tags)
async def get_books(session: Session = Depends(get_session)):
    books = get_all_books_service(session)
    return BooksResponse(books=books)
