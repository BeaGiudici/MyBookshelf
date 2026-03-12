from typing import Optional
from pydantic import BaseModel

class StatusUpdate(BaseModel):
    id: int
    name: Optional[str] = None