from fastapi import APIRouter
from fastapi import HTTPException
from src.schemas.status import Status, StatusUpdate
from src.utils.connection import get_session
from src.endpoints.status.update.response import error_responses
from src.endpoints.status.read.read_status import get_status_by_id

path = "/status/update"
tags = ["status"]
router = APIRouter()

@router.patch(path=path, response_model=Status, responses=error_responses, tags=tags)
async def update_status(new_status: StatusUpdate):
    with get_session() as db:
        status = get_status_by_id(db, new_status.id)
        if status is None:
            raise HTTPException(status_code=404, detail="Status ID not found. Check if the status exists.")

        if new_status.name is not None:
            status.name = new_status.name
        db.commit()
        db.refresh(status)
    return status