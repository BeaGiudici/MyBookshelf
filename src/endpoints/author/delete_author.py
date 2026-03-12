from fastapi import APIRouter, HTTPException
from src.endpoints.author.response import error_responses
from src.services.authors_service import delete_author_service

path = "/author/delete"
tags = ["author"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_author(author_id: int):
    msg = delete_author_service(author_id)
    return dict(msg=msg)