from src.database.models import Author
from sqlmodel import Session

def get_all_authors(session: Session):
    """Get all authors from the database"""
    return session.query(Author).all()


def get_author_by_id(session: Session, author_id: int):
    """Get an author by their ID"""
    return session.query(Author).filter(Author.id == author_id).first()


def get_author_by_name(session: Session, author_name: str):
    """Get an author by their name"""
    return session.query(Author).filter(Author.name == author_name).first()


def update_author(session: Session, author: Author):
    """Update an author entry in the database"""
    session.merge(author)
    session.commit()
    session.refresh(author)
    return author


def add_author(session: Session, author: Author):
    """Add a new author entry to the database"""
    session.add(author)
    session.commit()
    session.refresh(author)
    return author


def delete_author(session: Session, author_id: int):
    """Delete an author entry from the database"""
    
    session.query(Author).filter(Author.id == author_id).delete()
    session.commit()
    return {"message": f"Author {author_id} deleted successfully"}

