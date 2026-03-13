from src.database.models import Author
from src.database.connection import get_session


def get_all_authors():
    """Get all authors from the database"""
    with get_session() as db:
        return db.query(Author).all()


def get_author_by_id(author_id: int):
    """Get an author by their ID"""
    with get_session() as db:
        return db.query(Author).filter(Author.id == author_id).first()


def get_author_by_name(author_name: str):
    """Get an author by their name"""
    with get_session() as db:
        return db.query(Author).filter(Author.name == author_name).first()


def update_author(author: Author):
    """Update an author entry in the database"""
    with get_session() as db:
        db_author = db.merge(author)
        db.commit()
        db.refresh(db_author)
        return db_author


def add_author(author: Author):
    """Add a new author entry to the database"""
    with get_session() as db:
        db.add(author)
        db.commit()
        db.refresh(author)
        return author


def delete_author(author_id: int):
    """Delete an author entry from the database"""
    with get_session() as db:
        db.query(Author).filter(Author.id == author_id).delete()
        db.commit()
        return {"message": f"Author {author_id} deleted successfully"}

