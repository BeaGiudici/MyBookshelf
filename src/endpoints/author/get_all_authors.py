from fastapi import APIRouter
from src.schemas.author_schemas import AuthorsResponse
from src.services.authors_service import get_all_authors_service
from src.endpoints.author.response import error_responses

### Endpoint description ###

path = "/author/get/all"

tags = ["author"]

########

# Initialize router
router = APIRouter()

@router.get(path=path, response_model=AuthorsResponse, responses=error_responses, tags=tags)
async def get_authors():
    authors = get_all_authors_service()
    return AuthorsResponse(authors=authors)