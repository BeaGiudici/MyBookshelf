from src.repositories.authors_repo import get_all_authors, get_author_by_id, get_author_by_name, update_author, delete_author
from fastapi import HTTPException

def get_all_authors_service():
    authors = get_all_authors()
    if authors is None:
        raise HTTPException(status_code=404, detail="No authors found.")
    return authors

def get_author_by_id_service(author_id: int):
    author = get_author_by_id(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author

def get_author_by_name_service(author_name: str):
    author = get_author_by_name(author_name)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author

def update_author_service(new_author):
    author = get_author_by_id(new_author.id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    if new_author.name is not None:
        author.name = new_author.name
    if new_author.date_of_birth is not None:
        author.date_of_birth = new_author.date_of_birth
    if new_author.date_of_death is not None:
        author.date_of_death = new_author.date_of_death

    author = update_author(author)
    return author

def add_author_service(new_author):
    # Assert required fields are present
    if new_author.id is None or new_author.name is None or new_author.date_of_birth is None or new_author.date_of_death is None or new_author.country is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    author = get_author_by_name(new_author.name)
    # Assert author does not already exist
    if author is not None:
        raise HTTPException(status_code=400, detail="Author already exists.")

    # Add author to database
    author = add_author(new_author)
    return author

def delete_author_service(author_id: int):
    author = get_author_by_id(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    msg = delete_author(author_id)
    return msg