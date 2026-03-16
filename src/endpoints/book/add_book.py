from fastapi import APIRouter, Depends, Body
from src.schemas.book_schemas import BookResponse, BookCreate
from src.endpoints.book.response import error_responses
from src.services.books_service import add_book_service
from src.database.connection import get_session
from sqlmodel import Session

path = "/book/create"
tags = ["book"]
router = APIRouter()


@router.post(path=path, response_model=BookResponse, responses=error_responses, tags=tags)
async def add_book(session: Session = Depends(get_session), new_book: BookCreate = Body(...)):
    book = add_book_service(session, new_book)
    return BookResponse(book=book)
