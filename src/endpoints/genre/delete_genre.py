from fastapi import APIRouter

from src.endpoints.genre.response import error_responses
from src.services.genres_service import delete_genre_service

path = "/genre/delete"
tags = ["genre"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_genre(genre_id: int):
    msg = delete_genre_service(genre_id)
    return dict(msg=msg)

