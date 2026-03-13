from fastapi import HTTPException

from src.database.models import Status
from src.repositories.statuses_repo import (
    add_status,
    delete_status,
    get_all_statuses,
    get_status_by_id,
    get_status_by_name,
    update_status,
)
from src.schemas.status_schemas import StatusCreate, StatusUpdate


def get_all_statuses_service():
    statuses = get_all_statuses()
    if statuses is None:
        raise HTTPException(status_code=404, detail="No statuses found.")
    return statuses


def get_status_by_id_service(status_id: int):
    status = get_status_by_id(status_id)
    if status is None:
        raise HTTPException(
            status_code=404, detail=f"Status with ID {status_id} not found."
        )
    return status


def get_status_by_name_service(status_name: str):
    status = get_status_by_name(status_name)
    if status is None:
        raise HTTPException(
            status_code=404, detail=f"Status with name {status_name} not found."
        )
    return status


def add_status_service(new_status: StatusCreate):
    if new_status.name is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    existing = get_status_by_name(new_status.name)
    if existing is not None:
        raise HTTPException(status_code=400, detail="Status already exists.")

    status = Status(name=new_status.name)
    return add_status(status)


def update_status_service(status_update: StatusUpdate):
    if status_update.id is not None:
        status = get_status_by_id_service(status_update.id)
    elif status_update.name is not None:
        status = get_status_by_name_service(status_update.name)
    else:
        raise HTTPException(
            status_code=400, detail="Missing required fields. Provide either ID or name."
        )

    if status_update.name is not None:
        status.name = status_update.name

    return update_status(status)


def delete_status_service(status_id: int):
    status = get_status_by_id(status_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found.")
    msg = delete_status(status_id)
    return msg

