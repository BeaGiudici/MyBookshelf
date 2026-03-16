from fastapi import APIRouter, Depends, Body
from src.database.connection import get_session
from sqlmodel import Session

from src.endpoints.genre.response import error_responses
from src.services.genres_service import delete_genre_service

path = "/genre/delete"
tags = ["genre"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_genre(session: Session = Depends(get_session), genre_id: int = Body(...)):
    msg = delete_genre_service(session, genre_id)
    return dict(msg=msg)

