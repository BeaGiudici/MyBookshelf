from fastapi import APIRouter, HTTPException
from src.schemas.genre import Genre
from src.utils.connection import get_session
from src.endpoints.genre.read.response import error_responses
from sqlmodel import Session

path = "/genre/get"
tags = ["genre"]
router = APIRouter()


async def get_genre_by_id(db: Session, genre_id: int):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.get(path=path, response_model=Genre, responses=error_responses, tags=tags)
async def get_genre(genre_id: int):
    with get_session() as db:
        genre = get_genre_by_id(db, genre_id)
    return genre