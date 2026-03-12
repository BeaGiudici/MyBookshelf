from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from src.utils.connection import get_session
from src.endpoints.author.delete.response import error_responses
from src.endpoints.author.read.read_author import get_author_by_id

path = "/author/delete"
tags = ["author"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_author(author_id: int):
    with get_session() as db:
        author = await get_author_by_id(db, author_id)
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        db.execute(text("DELETE FROM author WHERE id = :id"), {"id": author_id})
        db.commit()
    return {"message": f"Author {author_id} deleted successfully"}