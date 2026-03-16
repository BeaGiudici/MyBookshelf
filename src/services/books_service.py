from src.repositories.books_repo import (
    get_all_books,
    get_book_by_id,
    get_book_by_title,
    add_book as add_book_repo,
    update_book,
    delete_book,
)
from src.repositories.authors_repo import get_author_by_id
from src.database.models import Book
from src.schemas.book_schemas import BookCreate, BookUpdate
from fastapi import HTTPException
from src.observability.metrics import get_books_updated_counter, get_books_retrieved_counter, get_books_deleted_counter, get_books_created_counter
from src.observability.tracing import get_tracer
from src.observability.logging import get_logger

tracer = get_tracer(__name__)
logger = get_logger(__name__)


def get_all_books_service():
    with tracer.start_as_current_span("get_all_books_service"):
        books = get_all_books()
        logger.info(f"Books retrieved successfully: {len(books)}")
        if books is None:
            logger.error("No books found.")
            raise HTTPException(status_code=404, detail="No books found.")
        logger.info(f"Books retrieved successfully: {len(books)}")
        get_books_retrieved_counter().add(len(books))
        return books


def get_book_by_id_service(book_id: int):
    with tracer.start_as_current_span("get_book_by_id_service", attributes={"book_id": book_id}):
        book = get_book_by_id(book_id)
        if book is None:
            logger.error(f"Book with ID {book_id} not found.")
            raise HTTPException(
                status_code=404, detail=f"Book with ID {book_id} not found."
            )
        logger.info(f"Book retrieved successfully: {book}")
        get_books_retrieved_counter().add(1)
        return book


def get_book_by_title_service(book_title: str):
    with tracer.start_as_current_span("get_book_by_title_service", attributes={"book_title": book_title}):
        book = get_book_by_title(book_title)
        if book is None:
            logger.error(f"Book with title {book_title} not found.")
            raise HTTPException(
                status_code=404, detail=f"Book with title {book_title} not found."
            )
        get_books_retrieved_counter().add(1)
        return book


def add_book_service(new_book: BookCreate):
    with tracer.start_as_current_span("add_book_service", attributes={"new_book": new_book}):
        if (
            new_book.title is None
            or new_book.isbn is None
            or new_book.year is None
            or new_book.author_id is None
            or new_book.status_id is None
        ):
            logger.error("Missing required fields")
            raise HTTPException(status_code=400, detail="Missing required fields")

        existing = get_book_by_title(new_book.title)
        if existing is not None:
            logger.error(f"Book {new_book.title} already exists.")
            raise HTTPException(status_code=400, detail="Book already exists.")

        author = get_author_by_id(new_book.author_id)
        if author is None:
            logger.error(f"Author {new_book.author_id} not found.")
            raise HTTPException(status_code=400, detail="Author not found.")

        book = Book(
            title=new_book.title,
            isbn=new_book.isbn,
            year=new_book.year,
            author_id=new_book.author_id,
            status_id=new_book.status_id,
        )
        logger.info(f"Book created successfully: {book}")
        get_books_created_counter().add(1)
        return add_book_repo(book)


def update_book_service(book_update: BookUpdate):
    with tracer.start_as_current_span("update_book_service", attributes={"book_update": book_update}):
        if book_update.id is not None:
            book = get_book_by_id_service(book_update.id)
        elif book_update.title is not None:
            book = get_book_by_title_service(book_update.title)
        else:
            logger.error("Missing required fields. Provide either ID or title.")
            raise HTTPException(
                status_code=400,
                detail="Missing required fields. Provide either ID or title.",
            )

        if book_update.title is not None:
            book.title = book_update.title
        if book_update.isbn is not None:
            book.isbn = book_update.isbn
        if book_update.year is not None:
            book.year = book_update.year
        if book_update.author_id is not None:
            book.author_id = book_update.author_id
        if book_update.status_id is not None:
            book.status_id = book_update.status_id

        logger.info(f"Book updated successfully: {book}")
        get_books_updated_counter().add(1)
        return update_book(book)


def delete_book_service(book_id: int):
    with tracer.start_as_current_span("delete_book_service", attributes={"book_id": book_id}):
        book = get_book_by_id(book_id)
        if book is None:
            logger.error(f"Book with ID {book_id} not found.")
            raise HTTPException(status_code=404, detail="Book not found.")
        logger.info(f"Book deleted successfully: {book}")
        get_books_deleted_counter().add(1)
        msg = delete_book(book_id)
        return msg
