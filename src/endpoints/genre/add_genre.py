from fastapi import APIRouter, Depends
from src.database.connection import get_session
from sqlmodel import Session
from src.endpoints.genre.response import error_responses
from src.schemas.genre_schemas import GenreCreate, GenreResponse
from src.services.genres_service import add_genre_service

path = "/genre/create"
tags = ["genre"]
router = APIRouter()


@router.post(path=path, response_model=GenreResponse, responses=error_responses, tags=tags)
async def add_genre(session: Session = Depends(get_session), new_genre: GenreCreate):
    genre = add_genre_service(session, new_genre)
    return GenreResponse(genre=genre)

