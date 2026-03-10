from typing import TYPE_CHECKING
from . import Field, SQLModel, Relationship, List
from .book_genre_link import BookGenreLink

if TYPE_CHECKING:
    from .book import Book


class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    books: List["Book"] = Relationship(
        back_populates="genres", link_model=BookGenreLink
    )
