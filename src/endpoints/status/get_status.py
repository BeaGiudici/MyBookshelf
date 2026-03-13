from fastapi import APIRouter

from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusResponse
from src.services.statuses_service import get_status_by_id_service

path = "/status/get"
tags = ["status"]
router = APIRouter()


@router.get(path=path, response_model=StatusResponse, responses=error_responses, tags=tags)
async def get_status(status_id: int):
    status = get_status_by_id_service(status_id)
    return StatusResponse(status=status)

