from fastapi import FastAPI

# Import all models so SQLAlchemy mappers (and relationships) are registered
from src.database.models import Author, Book, BookGenreLink, Genre, Status  # noqa: F401

# Book endpoints
from src.endpoints.book.router import router as book_router

# Status endpoints
from src.endpoints.status.create.add_status import router as add_status_router
from src.endpoints.status.read.read_all import router as read_all_statuses_router
from src.endpoints.status.read.read_status import router as read_status_router
from src.endpoints.status.update.update_status import router as update_status_router
from src.endpoints.status.delete.delete_status import router as delete_status_router

# Genre endpoints
from src.endpoints.genre.create.add_genre import router as add_genre_router
from src.endpoints.genre.read.read_all import router as read_all_genres_router
from src.endpoints.genre.read.read_genre import router as read_genre_router
from src.endpoints.genre.update.update_genre import router as update_genre_router
from src.endpoints.genre.delete.delete_genre import router as delete_genre_router

app = FastAPI(name="My Bookshelf", version="0.1.0")

# Include the necessary routers
# Book endpoints
app.include_router(book_router)



# Status endpoints
app.include_router(add_status_router)
app.include_router(read_all_statuses_router)
app.include_router(read_status_router)
app.include_router(update_status_router)
app.include_router(delete_status_router)

# Genre endpoints
app.include_router(add_genre_router)
app.include_router(read_all_genres_router)
app.include_router(read_genre_router)
app.include_router(update_genre_router)
app.include_router(delete_genre_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
