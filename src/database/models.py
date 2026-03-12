from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
import datetime

# BookGenreLink model
class BookGenreLink(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True, ondelete="CASCADE")
    genre_id: int | None = Field(default=None, foreign_key="genre.id", primary_key=True, ondelete="CASCADE")

# Book model
class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str
    isbn: str
    year: int
    author_id: int | None = Field(default=None, foreign_key="author.id", ondelete="CASCADE")
    status_id: int | None = Field(default=None, foreign_key="status.id", ondelete="CASCADE")
    author: Optional["Author"] = Relationship(back_populates="books", passive_deletes=True)
    genres: Optional[List["Genre"]] = Relationship(
        back_populates="books", link_model=BookGenreLink, passive_deletes=True
    )
    status: Optional["Status"] = Relationship(back_populates="books", passive_deletes=True)

# Author model
class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    date_of_birth: datetime.date = Field(default=datetime.date.today())
    date_of_death: datetime.date = Field(default=datetime.date.today())
    country: str = Field(default="Unknown")
    books: List["Book"] = Relationship(back_populates="author", passive_deletes=True)

# Status model
class Status(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(default="Unknown")
    books: List["Book"] = Relationship(back_populates="status", passive_deletes=True)

# Genre model
class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(default="Unknown")
    books: List["Book"] = Relationship(
        back_populates="genres", link_model=BookGenreLink, passive_deletes=True
    )

