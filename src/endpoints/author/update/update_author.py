from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.author import Author, AuthorUpdate
from src.utils.connection import get_session
from src.endpoints.author.update.response import error_responses
from src.endpoints.author.read.read_author import get_author_by_id

path = "/author/update"
tags = ["author"]
router = APIRouter()

@router.patch(path=path, response_model=Author, responses=error_responses, tags=tags)
async def update_author(new_author: AuthorUpdate):
    with get_session() as db:
        author = await get_author_by_id(db, new_author.id)
        if author is None:
            raise HTTPException(status_code=404, detail="Author ID not found. Check if the author exists.")

        if new_author.name is not None:
            author.name = new_author.name
        if new_author.date_of_birth is not None:
            author.date_of_birth = new_author.date_of_birth
        if new_author.date_of_death is not None:
            author.date_of_death = new_author.date_of_death
        db.commit()
        db.refresh(author)
    return author