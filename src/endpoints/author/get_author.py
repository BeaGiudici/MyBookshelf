from fastapi import APIRouter, HTTPException
from src.schemas.author_schemas import AuthorResponse
from src.services.authors_service import get_author_by_id_service
from src.endpoints.author.response import error_responses

### Endpoint description ###

path = "/author/get"

tags = ["author"]

########

# Initialize router
router = APIRouter()

@router.get(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def get_author(author_id: int):
    author = get_author_by_id_service(author_id)
    return AuthorResponse(author=author)