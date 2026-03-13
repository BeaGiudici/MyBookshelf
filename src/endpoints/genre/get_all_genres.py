from fastapi import APIRouter

from src.endpoints.genre.response import error_responses
from src.schemas.genre_schemas import GenresResponse
from src.services.genres_service import get_all_genres_service

path = "/genre/get/all"
tags = ["genre"]
router = APIRouter()


@router.get(path=path, response_model=GenresResponse, responses=error_responses, tags=tags)
async def get_genres():
    genres = get_all_genres_service()
    return GenresResponse(genres=genres)

