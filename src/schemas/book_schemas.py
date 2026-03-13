from typing import Optional, List
from pydantic import BaseModel
from src.database.models import Book


class BooksResponse(BaseModel):
    books: List[Book]


class BookResponse(BaseModel):
    book: Book


class BookCreate(BaseModel):
    title: str
    isbn: Optional[str] = None
    year: Optional[int] = None
    author_id: Optional[int] = None
    status_id: Optional[int] = None


class BookUpdate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    isbn: Optional[str] = None
    year: Optional[int] = None
    author_id: Optional[int] = None
    status_id: Optional[int] = None
