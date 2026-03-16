from fastapi import APIRouter, Depends
from src.database.connection import get_session
from sqlmodel import Session

from src.endpoints.genre.response import error_responses
from src.schemas.genre_schemas import GenresResponse
from src.services.genres_service import get_all_genres_service

path = "/genre/get/all"
tags = ["genre"]
router = APIRouter()


@router.get(path=path, response_model=GenresResponse, responses=error_responses, tags=tags)
async def get_genres(session: Session = Depends(get_session)):
    genres = get_all_genres_service(session)
    return GenresResponse(genres=genres)

