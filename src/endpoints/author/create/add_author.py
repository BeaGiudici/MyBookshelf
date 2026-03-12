from fastapi import APIRouter, HTTPException
from src.schemas.author import Author
from src.utils.connection import get_session
from src.endpoints.author.create.response import error_responses

path = "/author/create"
tags = ["author"]
router = APIRouter()

@router.post(path=path, response_model=Author, responses=error_responses, tags=tags)
async def add_author(new_author: Author):
    # Assert required fields are present
    if new_author.id is None or new_author.name is None or new_author.date_of_birth is None or new_author.date_of_death is None or new_author.country is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    with get_session() as db:
        # Assert author does not already exist
        a = await get_author_by_name(db, new_author.name)
        if a is not None:
            raise HTTPException(status_code=400, detail="Author already exists")

        # Add author to database
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
    return new_author