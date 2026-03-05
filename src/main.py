from models.book import Book
from models.author import Author

from sqlmodel import SQLModel, create_engine

db_url = "postgresql://postgres:postgres@localhost:5432/bookshelf"
engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)