from fastapi import APIRouter, Body, Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.endpoints.status.response import error_responses
from src.services.statuses_service import delete_status_service

path = "/status/delete"
tags = ["status"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_status(session: Session = Depends(get_session), status_id: int = Body(...)):
    msg = delete_status_service(session, status_id)
    return dict(msg=msg)
