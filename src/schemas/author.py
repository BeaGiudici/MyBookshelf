from datetime import datetime
from .base import Field, SQLModel, Relationship, Optional, List


class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    date_of_birth: datetime
    date_of_death: Optional[datetime] = None
    country: str
    books: List["Book"] = Relationship(back_populates="author")
