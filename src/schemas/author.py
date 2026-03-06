from typing import TYPE_CHECKING
from datetime import datetime
from . import Field, SQLModel, Relationship, Optional, List

if TYPE_CHECKING:
    from .book import Book


class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    date_of_birth: datetime
    date_of_death: Optional[datetime] = None
    country: str
    books: List["Book"] = Relationship(back_populates="author")
