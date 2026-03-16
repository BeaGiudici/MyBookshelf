from sqlmodel import Session
from src.database.models import Genre


def get_all_genres(session: Session):
    """Get all genres from the database"""
    return session.query(Genre).order_by(Genre.id).all()


def get_genre_by_id(session: Session, genre_id: int):
    """Get a genre by its ID"""
    return session.query(Genre).filter(Genre.id == genre_id).first()


def get_genre_by_name(session: Session, genre_name: str):
    """Get a genre by its name"""
    return session.query(Genre).filter(Genre.name == genre_name).first()


def update_genre(session: Session, genre: Genre):
    """Update a genre entry in the database"""
    session.merge(genre)
    session.commit()
    session.refresh(genre)
    return genre


def add_genre(session: Session, genre: Genre):
    """Add a new genre entry to the database"""
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre


def delete_genre(session: Session, genre_id: int):
    """Delete a genre entry from the database"""
    session.query(Genre).filter(Genre.id == genre_id).delete()
    session.commit()
    return {"message": f"Genre {genre_id} deleted successfully"}

