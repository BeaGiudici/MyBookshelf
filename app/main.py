from fastapi import FastAPI
from .models import Book, BookCreate, BookUpdate

app = FastAPI(title='My Bookshelf', version='0.1.0')

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
