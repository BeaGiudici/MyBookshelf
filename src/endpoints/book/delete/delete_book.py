from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from src.utils.connection import get_session
from src.endpoints.book.delete.response import error_responses
from src.endpoints.book.read.read_book import get_book_by_id

path = "/book/delete"
tags = ["book"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_book(book_id: int):
    with get_session() as db:
        book = await get_book_by_id(db, book_id)
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        db.execute(text("DELETE FROM book WHERE id = :id"), {"id": book_id})
        db.commit()
    return {"message": f"Book {book_id} deleted successfully"}