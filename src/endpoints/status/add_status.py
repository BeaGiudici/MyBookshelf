from fastapi import APIRouter

from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusCreate, StatusResponse
from src.services.statuses_service import add_status_service

path = "/status/create"
tags = ["status"]
router = APIRouter()


@router.post(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def add_status(new_status: StatusCreate):
    status = add_status_service(new_status)
    return StatusResponse(status=status)

