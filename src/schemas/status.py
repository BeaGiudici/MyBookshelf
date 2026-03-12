from typing import Optional

from .base import Field, SQLModel, Relationship, List


class Status(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(default="Unknown")
    books: List["Book"] = Relationship(back_populates="status")

class StatusUpdate(SQLModel):
    id: int
    name: Optional[str] = None