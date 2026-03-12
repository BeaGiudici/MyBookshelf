from fastapi import APIRouter, HTTPException
from src.schemas.book import Book
from src.utils.connection import get_session
from src.endpoints.book.create.response import error_responses

path = "/book/create"
tags = ["book"]
router = APIRouter()

async def get_book_by_title(db: Session, book_title: str):
    book = db.query(Book).filter(Book.title == book_title).first()
    return book

@router.post(path=path, response_model=Book, responses=error_responses, tags=tags)
async def add_book(new_book: Book):
    # Assert required fields are present
    if new_book.id is None or new_book.title is None or new_book.isbn is None or new_book.year is None or new_book.author_id is None or new_book.status_id is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    with get_session() as db:
        # Assert book does not already exist
        b = await get_book_by_title(db, new_book.title)
        if b is not None:
            print(b)
            print(new_book)
        if False:
            # Assert author exists
            if await get_author_by_id(db, new_book.author_id) is None:
                raise HTTPException(status_code=400, detail="Author not found")

            # Assert status exists
            if await get_status_by_id(db, new_book.status_id) is None:
                raise HTTPException(status_code=400, detail="Status not found")
        
        # Add book to database
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book