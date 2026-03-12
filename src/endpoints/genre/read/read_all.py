from fastapi import APIRouter, HTTPException
from src.schemas.genre import Genre
from src.utils.connection import get_session

path = "/genre/get/all"
tags = ["genre"]
router = APIRouter(prefix=path, tags=tags)


@router.get("/")
async def get_genres() -> list[Genre]:
    with get_session() as db:
        genres = db.query(Genre).order_by(Genre.id).all()
        if genres is None:
            raise HTTPException(status_code=404, detail="No genres found.")
    return genres