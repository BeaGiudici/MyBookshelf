from fastapi import APIRouter
from src.schemas.author import Author
from src.utils.connection import get_session

path = "/author/get/all"
tags = ["author"]
router = APIRouter()

@router.get(path=path, response_model=list[Author], tags=tags)
async def get_authors():
    with get_session() as db:
        authors = db.query(Author).order_by(Author.id).all()
        if authors is None:
            raise HTTPException(status_code=404, detail="No authors found.")
    return authors