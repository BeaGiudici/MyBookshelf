from fastapi import APIRouter, HTTPException
from src.schemas.book import BookResponse, Book, BookCreate, AuthorInBookResponse
from src.schemas.book_genre_link import BookGenreLink
from src.schemas.author import Author
from src.schemas.genre import Genre
from src.schemas.status import Status
from src.utils.connection import get_session

path = "/book/create"
tags = ["book"]
router = APIRouter(prefix=path, tags=tags)


@router.post("/")
async def add_book(new_book: BookCreate) -> BookResponse:
    with get_session() as db:
        # Resolve author: find by id or name, or create by name
        if getattr(new_book.author, "id", None) is not None:
            author = db.get(Author, new_book.author.id)
        else:
            author = db.query(Author).filter(Author.name == new_book.author.name).first()
        if not author:
            author = Author(name=new_book.author.name)
            db.add(author)
            db.flush()
        author_id = author.id

        # Resolve status: find by id or name (use string name from request)
        status_name = getattr(new_book.status, "name", None) or str(new_book.status)
        status = (
            db.get(Status, new_book.status.id)
            if getattr(new_book.status, "id", None) is not None
            else db.query(Status).filter(Status.name == status_name).first()
        )
        if not status:
            raise HTTPException(
                status_code=404,
                detail=f"Status '{status_name}' not found. Create it first or use an existing status.",
            )
        status_id = status.id

        # Resolve genres: find each by id or name
        genre_ids = []
        for g in new_book.genres:
            if getattr(g, "id", None) is not None:
                genre = db.get(Genre, g.id)
            else:
                name = getattr(g, "name", None) or str(g)
                genre = db.query(Genre).filter(Genre.name == name).first()
            if not genre:
                raise HTTPException(
                    status_code=404,
                    detail=f"Genre '{getattr(g, 'name', g)}' not found. Create it first.",
                )
            genre_ids.append(genre.id)

        book = Book(
            title=new_book.title,
            isbn=new_book.isbn,
            year=new_book.year,
            author_id=author_id,
            status_id=status_id,
        )
        db.add(book)
        db.flush()
        for gid in genre_ids:
            db.add(BookGenreLink(book_id=book.id, genre_id=gid))
        db.commit()
        db.refresh(book)

        author_name = author.name
    return BookResponse(
        id=book.id,
        title=book.title,
        author=AuthorInBookResponse(name=author_name),
    )