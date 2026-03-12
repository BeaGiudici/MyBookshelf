from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.genre import Genre, GenreUpdate
from src.utils.connection import get_session
from src.endpoints.genre.update.response import error_responses
from src.endpoints.genre.read.read_genre import get_genre_by_id

path = "/genre/update"
tags = ["genre"]
router = APIRouter()

@router.patch(path=path, response_model=Genre, responses=error_responses, tags=tags)
async def update_genre(new_genre: GenreUpdate):
    with get_session() as db:
        genre = await get_genre_by_id(db, new_genre.id)
        if genre is None:
            raise HTTPException(status_code=404, detail="Genre ID not found. Check if the genre exists.")

        if new_genre.name is not None:
            genre.name = new_genre.name
        if new_genre.books is not None:
            genre.books = new_genre.books
        db.commit()
        db.refresh(genre)
    return genre