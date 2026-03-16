from fastapi import APIRouter, HTTPException, Depends, Body
from src.endpoints.author.response import error_responses
from src.services.authors_service import delete_author_service
from src.database.connection import get_session
from sqlmodel import Session

path = "/author/delete"
tags = ["author"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_author(session: Session = Depends(get_session), author_id: int = Body(...)):
    msg = delete_author_service(session, author_id)
    return dict(msg=msg)