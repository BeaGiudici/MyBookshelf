from fastapi import APIRouter, HTTPException
from src.schemas.status import Status
from src.utils.connection import get_session

path = "/status/get/all"
tags = ["status"]
router = APIRouter(prefix=path, tags=tags)


@router.get("/")
async def get_statuses() -> list[Status]:
    with get_session() as db:
        statuses = db.query(Status).order_by(Status.id).all()
        if statuses is None:
            raise HTTPException(status_code=404, detail="No statuses found.")
    return statuses