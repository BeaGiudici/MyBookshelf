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
    genres: List["Genre"] = Relationship(
        back_populates="books", link_model=BookGenreLink
    )
    status: Optional["Status"] = Relationship(back_populates="books")

class BookCreate(SQLModel):
    """Request body for creating a book."""
    title: str
    isbn: str
    year: int
    author: Author
    genres: List[Genre]
    status: Status

class AuthorInBookResponse(SQLModel):
    """Author fields included when returning a book."""
    name: str


class BookResponse(SQLModel):
    """Response schema linking book title and author."""
    id: int
    title: str
    author: AuthorInBookResponse | None = None
