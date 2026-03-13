from fastapi import APIRouter

from src.endpoints.genre.response import error_responses
from src.schemas.genre_schemas import GenreResponse
from src.services.genres_service import get_genre_by_id_service

path = "/genre/get"
tags = ["genre"]
router = APIRouter()


@router.get(path=path, response_model=GenreResponse, responses=error_responses, tags=tags)
async def get_genre(genre_id: int):
    genre = get_genre_by_id_service(genre_id)
    return GenreResponse(genre=genre)

