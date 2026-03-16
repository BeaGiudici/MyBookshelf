from fastapi import APIRouter, Depends, Body
from src.schemas.author_schemas import AuthorResponse, AuthorCreate
from src.endpoints.author.response import error_responses
from src.services.authors_service import add_author_service
from src.database.connection import get_session
from sqlmodel import Session

path = "/author/create"
tags = ["author"]
router = APIRouter()

@router.post(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def add_author(session: Session = Depends(get_session), new_author: AuthorCreate = Body(...)):
    author = add_author_service(session, new_author)
    return AuthorResponse(author=author)