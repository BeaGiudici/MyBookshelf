from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusResponse
from src.services.statuses_service import get_status_by_id_service

path = "/status/get"
tags = ["status"]
router = APIRouter()


@router.get(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def get_status(status_id: int, session: Session = Depends(get_session)):
    status = get_status_by_id_service(session, status_id)
    return StatusResponse(status=status)
