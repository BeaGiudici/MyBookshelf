from fastapi import APIRouter, Depends
from fastapi import HTTPException
from src.schemas.author_schemas import AuthorResponse, AuthorUpdate
from src.endpoints.author.response import error_responses
from src.services.authors_service import update_author_service
from src.database.connection import get_session
from sqlmodel import Session

path = "/author/update"
tags = ["author"]
router = APIRouter()

@router.patch(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def update_author(session: Session = Depends(get_session), new_author: AuthorUpdate):
    author = update_author_service(session, new_author)

    return AuthorResponse(author=author)