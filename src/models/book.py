from typing import TYPE_CHECKING
from . import Field, SQLModel, Relationship, Optional

if TYPE_CHECKING:
    from .author import Author
    from .genre import Genre
    from .status import Status


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str
    isbn: str
    year: int
    author_id: int | None = Field(default=None, foreign_key="author.id")
    genre_id: int | None = Field(default=None, foreign_key="genre.id")
    status_id: int | None = Field(default=None, foreign_key="status.id")
    author: Optional["Author"] = Relationship(back_populates="books")
    genres: Optional["Genre"] = Relationship(back_populates="books")
    status: Optional["Status"] = Relationship(back_populates="books")
