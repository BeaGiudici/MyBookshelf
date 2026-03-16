from fastapi import APIRouter, Body, Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusResponse, StatusUpdate
from src.services.statuses_service import update_status_service

path = "/status/update"
tags = ["status"]
router = APIRouter()


@router.patch(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def update_status(session: Session = Depends(get_session), new_status: StatusUpdate = Body(...)):
    status = update_status_service(session, new_status)
    return StatusResponse(status=status)
