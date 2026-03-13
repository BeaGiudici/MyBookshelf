from fastapi import APIRouter

from src.endpoints.status.response import error_responses
from src.services.statuses_service import delete_status_service

path = "/status/delete"
tags = ["status"]
router = APIRouter()


@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_status(status_id: int):
    msg = delete_status_service(status_id)
    return dict(msg=msg)

