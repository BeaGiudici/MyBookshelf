from fastapi import APIRouter, HTTPException, Depends
from src.schemas.author_schemas import AuthorResponse
from src.services.authors_service import get_author_by_id_service
from src.endpoints.author.response import error_responses
from src.database.connection import get_session
from sqlmodel import Session

### Endpoint description ###

path = "/author/get"

tags = ["author"]

########

# Initialize router
router = APIRouter()

@router.get(path=path, response_model=AuthorResponse, responses=error_responses, tags=tags)
async def get_author(session: Session = Depends(get_session), author_id: int):
    author = get_author_by_id_service(session, author_id)
    return AuthorResponse(author=author)