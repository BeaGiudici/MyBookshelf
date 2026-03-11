from .base import Field, SQLModel, Relationship, List
from .book_genre_link import BookGenreLink


class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(default="Unknown")
    books: List["Book"] = Relationship(
        back_populates="genres", link_model=BookGenreLink
    )
