from datetime import date
from typing import Optional, List
from pydantic import BaseModel
from src.database.models import Author


class AuthorCreate(BaseModel):
    name: str
    date_of_birth: date
    date_of_death: date | None = None
    country: str

class AuthorsResponse(BaseModel):
    authors: List[Author]

class AuthorResponse(BaseModel):
    author: Author


class AuthorUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    date_of_death: Optional[date] = None
    country: Optional[str] = None