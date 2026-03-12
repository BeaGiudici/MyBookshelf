from typing import Optional
from pydantic import BaseModel

class GenreUpdate(BaseModel):
    id: int
    name: Optional[str] = None