from datetime import datetime
from .base import Field, SQLModel, Relationship, Optional, List


class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    date_of_birth: datetime = Field(default=datetime.now())
    date_of_death: datetime = Field(default=datetime.now())
    country: str = Field(default="Unknown")
    books: List["Book"] = Relationship(back_populates="author")
