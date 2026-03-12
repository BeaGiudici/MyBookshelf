from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from src.utils.connection import get_session
from src.endpoints.genre.delete.response import error_responses
from src.endpoints.genre.read.read_genre import get_genre_by_id

path = "/genre/delete"
tags = ["genre"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_genre(genre_id: int):
    with get_session() as db:
        genre = await get_genre_by_id(db, genre_id)
        if genre is None:
            raise HTTPException(status_code=404, detail="Genre not found")
        db.execute(text("DELETE FROM genre WHERE id = :id"), {"id": genre_id})
        db.commit()
    return {"message": f"Genre {genre_id} deleted successfully"}