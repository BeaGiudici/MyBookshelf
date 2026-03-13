from fastapi import APIRouter

from src.endpoints.status.response import error_responses
from src.schemas.status_schemas import StatusesResponse
from src.services.statuses_service import get_all_statuses_service

path = "/status/get/all"
tags = ["status"]
router = APIRouter()


@router.get(path=path, response_model=StatusesResponse, responses=error_responses, tags=tags)
async def get_statuses():
    statuses = get_all_statuses_service()
    return StatusesResponse(statuses=statuses)

