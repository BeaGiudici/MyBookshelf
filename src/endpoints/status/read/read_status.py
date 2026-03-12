from fastapi import APIRouter, HTTPException
from src.schemas.status import Status
from src.utils.connection import get_session
from src.endpoints.status.read.response import error_responses
from sqlmodel import Session

path = "/status/get"
tags = ["status"]
router = APIRouter()


def get_status_by_id(db: Session, status_id: int):
    status = db.query(Status).filter(Status.id == status_id).first()
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@router.get(path=path, response_model=Status, responses=error_responses, tags=tags)
async def get_status(status_id: int):
    with get_session() as db:
        status = get_status_by_id(db, status_id)
    return status