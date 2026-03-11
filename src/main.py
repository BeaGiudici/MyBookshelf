from fastapi import FastAPI

# Import all models so SQLAlchemy mappers (and relationships) are registered
from src.schemas import Author, Book, BookGenreLink, Genre, Status  # noqa: F401

from src.endpoints.book.create.add_book import router as add_book_router
from src.endpoints.book.read.read_all import router as read_all_books_router
from src.endpoints.book.read.read_book import router as read_book_router
from src.endpoints.book.delete.delete_book import router as delete_book_router
from src.endpoints.book.update.update_book import router as update_book_router

app = FastAPI(name="My Bookshelf", version="0.1.0")

# Include the necessary routers
app.include_router(add_book_router)
app.include_router(read_all_books_router)
app.include_router(read_book_router)
app.include_router(delete_book_router)
app.include_router(update_book_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
