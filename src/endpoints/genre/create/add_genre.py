from fastapi import APIRouter, HTTPException
from src.schemas.genre import Genre
from src.utils.connection import get_session
from src.endpoints.genre.create.response import error_responses

path = "/genre/create"
tags = ["genre"]
router = APIRouter()

async def get_genre_by_name(db: Session, genre_name: str):
    genre = db.query(Genre).filter(Genre.name == genre_name).first()
    return genre

@router.post(path=path, response_model=Genre, responses=error_responses, tags=tags)
async def add_genre(new_genre: Genre):
    # Assert required fields are present
    if new_genre.id is None or new_genre.name is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    with get_session() as db:
        # Assert book does not already exist
        g = await get_genre_by_name(db, new_genre.name)
        if b is not None:
            raise HTTPException(status_code=400, detail="Genre already exists")
        
        # Add genre to database
        db.add(new_genre)
        db.commit()
        db.refresh(new_genre)
        return new_genre