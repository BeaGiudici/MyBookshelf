from fastapi import APIRouter, Depends
from src.database.connection import get_session
from sqlmodel import Session

from src.endpoints.genre.response import error_responses
from src.schemas.genre_schemas import GenreResponse, GenreUpdate
from src.services.genres_service import update_genre_service

path = "/genre/update"
tags = ["genre"]
router = APIRouter()


@router.patch(path=path, response_model=GenreResponse, responses=error_responses, tags=tags)
async def update_genre(session: Session = Depends(get_session), new_genre: GenreUpdate):
    genre = update_genre_service(session, new_genre)
    return GenreResponse(genre=genre)

