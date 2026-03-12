from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from src.utils.connection import get_session
from src.endpoints.status.delete.response import error_responses
from src.endpoints.status.read.read_status import get_status_by_id

path = "/status/delete"
tags = ["status"]
router = APIRouter()

@router.delete(path=path, response_model=dict, responses=error_responses, tags=tags)
async def delete_status(status_id: int):
    with get_session() as db:
        status = get_status_by_id(db, status_id)
        if status is None:
            raise HTTPException(status_code=404, detail="Status not found")
        db.execute(text("DELETE FROM status WHERE id = :id"), {"id": status_id})
        db.commit()
    return {"message": f"Status {status_id} deleted successfully"}