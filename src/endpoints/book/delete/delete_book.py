from fastapi import APIRouter
from sqlalchemy import text
from src.utils.connection import get_session

path = "/book/delete"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)

@router.delete("/")
async def delete_book(book_id: int) -> dict:
    with get_session() as db:
        db.execute(text("DELETE FROM book WHERE id = :id"), {"id": book_id})
        db.commit()
    return {"message": f"Book {book_id} deleted successfully"}