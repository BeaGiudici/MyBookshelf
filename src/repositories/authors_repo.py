from typing import List
from src.database.models import Author
from src.database.connection import get_session

def get_all_authors():
    with get_session() as db:
        return db.query(Author).all()

def get_author_by_id(author_id: int):
    with get_session() as db:
        return db.query(Author).filter(Author.id == author_id).first()

def get_author_by_name(author_name: str):
    with get_session() as db:
        return db.query(Author).filter(Author.name == author_name).first()

def update_author(new_author: Author):
    with get_session() as db:
        db.query(Author).filter(Author.id == new_author.id).update(new_author.model_dump())
        db.commit()
        db.refresh(new_author)
        return new_author

def delete_author(author_id: int):
    with get_session() as db:
        db.query(Author).filter(Author.id == author_id).delete()
        db.commit()
        return {"message": f"Author {author_id} deleted successfully"}

