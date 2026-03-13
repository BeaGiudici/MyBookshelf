from fastapi import APIRouter

from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusResponse, StatusUpdate
from src.services.statuses_service import update_status_service

path = "/status/update"
tags = ["status"]
router = APIRouter()


@router.patch(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def update_status(new_status: StatusUpdate):
    status = update_status_service(new_status)
    return StatusResponse(status=status)

