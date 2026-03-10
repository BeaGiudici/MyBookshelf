from fastapi import FastAPI
from src.endpoints.book.create.add_book import router as add_book_router
from src.endpoints.book.read.read_books import router as read_books_router

app = FastAPI(name="My Bookshelf", version="0.1.0")

# Include the necessary routers
app.include_router(add_book_router)
app.include_router(read_books_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
