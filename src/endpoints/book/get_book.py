from fastapi import APIRouter, Depends
from src.schemas.book_schemas import BookResponse
from src.services.books_service import get_book_by_id_service
from src.endpoints.book.response import error_responses
from src.database.connection import get_session
from sqlmodel import Session

path = "/book/get"
tags = ["book"]
router = APIRouter()


@router.get(path=path, response_model=BookResponse, responses=error_responses, tags=tags)
async def get_book(session: Session = Depends(get_session), book_id: int):
    book = get_book_by_id_service(session, book_id)
    return BookResponse(book=book)
