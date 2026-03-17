from fastapi import APIRouter, Depends, Query
from src.endpoints.book.response import error_responses
from src.services.books_service import delete_book_service
from src.database.connection import get_session
from sqlmodel import Session

path = "/book/delete"
tags = ["book"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_book(session: Session = Depends(get_session), book_id: int = Query(...)):
    msg = delete_book_service(session, book_id)
    return dict(msg=msg)
