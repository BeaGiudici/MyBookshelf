from .base import Field, SQLModel, Relationship, Optional, List  
from .book_genre_link import BookGenreLink
from .author import Author
from .genre import Genre
from .status import Status

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str
    isbn: str
    year: int
    author_id: int | None = Field(default=None, foreign_key="author.id")
    status_id: int | None = Field(default=None, foreign_key="status.id")
    author: Optional["Author"] = Relationship(back_populates="books")
    genres: Optional[List["Genre"]] = Relationship(
        back_populates="books", link_model=BookGenreLink, passive_deletes=True
    )
    status: Optional["Status"] = Relationship(back_populates="books")

class BookUpdate(SQLModel):
    id: int
    title: Optional[str] = None
    isbn: Optional[str] = None
    year: Optional[int] = Field(default=None)
    author_id: Optional[int] = Field(default=None)
    status_id: Optional[int] = Field(default=None)
