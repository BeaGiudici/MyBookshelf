from .base import Field, SQLModel, Relationship, List, Optional
from .book_genre_link import BookGenreLink


class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(default="Unknown")
    books: List["Book"] = Relationship(
        back_populates="genres", link_model=BookGenreLink, passive_deletes=True
    )

def GenreUpdate(SQLModel):
    id: int
    name: Optional[str] = None
    books: Optional[List["Book"]] = None