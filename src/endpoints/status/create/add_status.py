from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from src.schemas.status import Status
from src.utils.connection import get_session
from src.endpoints.status.create.response import error_responses

path = "/status/create"
tags = ["status"]
router = APIRouter()

def get_status_by_name(db: Session, status_name: str):
    status = db.query(Status).filter(Status.name == status_name).first()
    return status

@router.post(path=path, response_model=Status, responses=error_responses, tags=tags)
async def add_status(new_status: Status):
    # Assert required fields are present
    if new_status.id is None or new_status.name is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    with get_session() as db:
        # Assert status does not already exist
        s = get_status_by_name(db, new_status.name)
        if s is not None:
            raise HTTPException(status_code=400, detail="Status already exists")
        # Add status to database
        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        return new_status