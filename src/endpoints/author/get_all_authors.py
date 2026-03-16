from fastapi import APIRouter, Depends
from src.schemas.author_schemas import AuthorsResponse
from src.services.authors_service import get_all_authors_service
from src.endpoints.author.response import error_responses
from src.database.connection import get_session
from sqlmodel import Session

### Endpoint description ###

path = "/author/get/all"

tags = ["author"]

########

# Initialize router
router = APIRouter()

@router.get(path=path, response_model=AuthorsResponse, responses=error_responses, tags=tags)
async def get_authors(session: Session = Depends(get_session)):
    authors = get_all_authors_service(session)
    return AuthorsResponse(authors=authors)