from typing import Optional, List
from pydantic import BaseModel
from src.database.models import Genre


class GenreCreate(BaseModel):
    name: str


class GenresResponse(BaseModel):
    genres: List[Genre]


class GenreResponse(BaseModel):
    genre: Genre


class GenreUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None