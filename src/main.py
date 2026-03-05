from models.book import Book
from models.author import Author

from sqlmodel import SQLModel, create_engine

db_filename = "bookshelf.db"
db_url = f"sqlite:///{db_filename}"
engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)