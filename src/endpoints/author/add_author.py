from fastapi import APIRouter, HTTPException
from src.schemas.author_schemas import AuthorResponse, AuthorUpdate
from src.endpoints.author.response import error_responses
from src.services.authors_service import add_author_service

path = "/author/create"
tags = ["author"]
router = APIRouter()

@router.post(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def add_author(new_author: AuthorUpdate):
    author = add_author_service(new_author)
    return author