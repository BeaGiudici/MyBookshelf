from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from src.database.models import Author

class AuthorsResponse(BaseModel):
    authors: List[Author]

class AuthorResponse(BaseModel):
    author: Author

# AuthorUpdate schema
class AuthorUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    date_of_death: Optional[datetime] = None
    country: Optional[str] = None