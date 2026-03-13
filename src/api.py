from fastapi import FastAPI
from src.endpoints.author.router import router as author_router
from src.endpoints.book.router import router as book_router
from src.endpoints.genre.router import router as genre_router
from src.endpoints.status.router import router as status_router

app = FastAPI(name="My Bookshelf", version="0.1.0")

app.include_router(author_router)
app.include_router(book_router)
app.include_router(genre_router)
app.include_router(status_router)