from fastapi import APIRouter
from src.endpoints.book.response import error_responses
from src.services.books_service import delete_book_service

path = "/book/delete"
tags = ["book"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_book(book_id: int):
    msg = delete_book_service(book_id)
    return msg
