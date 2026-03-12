from .base import Field, SQLModel


class BookGenreLink(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True, ondelete="CASCADE")
    genre_id: int | None = Field(default=None, foreign_key="genre.id", primary_key=True, ondelete="CASCADE")
