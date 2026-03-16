from fastapi import APIRouter, Body, Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusCreate, StatusResponse
from src.services.statuses_service import add_status_service

path = "/status/create"
tags = ["status"]
router = APIRouter()


@router.post(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def add_status(session: Session = Depends(get_session), new_status: StatusCreate = Body(...)):
    status = add_status_service(session, new_status)
    return StatusResponse(status=status)
