from src.repositories.authors_repo import (
    get_all_authors,
    get_author_by_id,
    get_author_by_name,
    update_author,
    add_author,
    delete_author,
)
from fastapi import HTTPException
from src.database.models import Author
from src.schemas.author_schemas import AuthorUpdate


def get_all_authors_service():
    authors = get_all_authors()
    if authors is None:
        raise HTTPException(status_code=404, detail="No authors found.")
    return authors


def get_author_by_id_service(author_id: int):
    author = get_author_by_id(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail=f"Author with ID {author_id} not found.")
    return author


def get_author_by_name_service(author_name: str):
    author = get_author_by_name(author_name)
    if author is None:
        raise HTTPException(status_code=404, detail=f"Author with name {author_name} not found.")
    return author


def update_author_service(new_author: AuthorUpdate):
    """Update an author entry in the database service"""

    if new_author.id is not None:
        author = get_author_by_id_service(new_author.id)
    elif new_author.name is not None:
        author = get_author_by_name_service(new_author.name)
    else:
        raise HTTPException(
            status_code=400, detail="Missing required fields. Provide either ID or name."
        )

    if new_author.date_of_birth is not None:
        author.date_of_birth = new_author.date_of_birth
    if new_author.date_of_death is not None:
        author.date_of_death = new_author.date_of_death
    if new_author.country is not None:
        author.country = new_author.country

    updated_author = update_author(author)
    return updated_author


def add_author_service(new_author):
    """Add a new author entry to the database service"""
    if (
        new_author.name is None
        or new_author.date_of_birth is None
        or new_author.country is None
    ):
        raise HTTPException(status_code=400, detail="Missing required fields")

    existing_author = get_author_by_name(new_author.name)
    if existing_author is not None:
        raise HTTPException(status_code=400, detail="Author already exists.")

    author = Author(
        name=new_author.name,
        date_of_birth=new_author.date_of_birth,
        date_of_death=new_author.date_of_death,
        country=new_author.country,
    )

    created_author = add_author(author)
    return created_author


def delete_author_service(author_id: int):
    """Delete an author entry from the database service"""
    author = get_author_by_id(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    msg = delete_author(author_id)
    return msg