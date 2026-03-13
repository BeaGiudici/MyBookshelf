from typing import Optional, List
from pydantic import BaseModel
from src.database.models import Status


class StatusCreate(BaseModel):
    name: str


class StatusesResponse(BaseModel):
    statuses: List[Status]


class StatusResponse(BaseModel):
    status: Status


class StatusUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None