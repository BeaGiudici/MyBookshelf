from src.database.connection import get_session
from src.database.models import Genre


def get_all_genres():
    """Get all genres from the database"""
    with get_session() as db:
        return db.query(Genre).order_by(Genre.id).all()


def get_genre_by_id(genre_id: int):
    """Get a genre by its ID"""
    with get_session() as db:
        return db.query(Genre).filter(Genre.id == genre_id).first()


def get_genre_by_name(genre_name: str):
    """Get a genre by its name"""
    with get_session() as db:
        return db.query(Genre).filter(Genre.name == genre_name).first()


def update_genre(genre: Genre):
    """Update a genre entry in the database"""
    with get_session() as db:
        db_genre = db.merge(genre)
        db.commit()
        db.refresh(db_genre)
        return db_genre


def add_genre(genre: Genre):
    """Add a new genre entry to the database"""
    with get_session() as db:
        db.add(genre)
        db.commit()
        db.refresh(genre)
        return genre


def delete_genre(genre_id: int):
    """Delete a genre entry from the database"""
    with get_session() as db:
        db.query(Genre).filter(Genre.id == genre_id).delete()
        db.commit()
        return {"message": f"Genre {genre_id} deleted successfully"}

