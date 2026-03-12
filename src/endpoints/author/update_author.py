from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.author_schemas import AuthorResponse, AuthorUpdate
from src.endpoints.author.response import error_responses
from src.services.authors_service import update_author_service

path = "/author/update"
tags = ["author"]
router = APIRouter()

@router.patch(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def update_author(new_author: AuthorUpdate):
    author = update_author_service(new_author)

    return AuthorResponse(author=author)