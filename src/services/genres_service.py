from fastapi import HTTPException

from src.database.models import Genre
from src.repositories.genres_repo import (
    add_genre,
    delete_genre,
    get_all_genres,
    get_genre_by_id,
    get_genre_by_name,
    update_genre,
)
from src.schemas.genre_schemas import GenreCreate, GenreUpdate


def get_all_genres_service():
    genres = get_all_genres()
    if genres is None:
        raise HTTPException(status_code=404, detail="No genres found.")
    return genres


def get_genre_by_id_service(genre_id: int):
    genre = get_genre_by_id(genre_id)
    if genre is None:
        raise HTTPException(
            status_code=404, detail=f"Genre with ID {genre_id} not found."
        )
    return genre


def get_genre_by_name_service(genre_name: str):
    genre = get_genre_by_name(genre_name)
    if genre is None:
        raise HTTPException(
            status_code=404, detail=f"Genre with name {genre_name} not found."
        )
    return genre


def add_genre_service(new_genre: GenreCreate):
    if new_genre.name is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    existing = get_genre_by_name(new_genre.name)
    if existing is not None:
        raise HTTPException(status_code=400, detail="Genre already exists.")

    genre = Genre(name=new_genre.name)
    return add_genre(genre)


def update_genre_service(genre_update: GenreUpdate):
    if genre_update.id is not None:
        genre = get_genre_by_id_service(genre_update.id)
    elif genre_update.name is not None:
        genre = get_genre_by_name_service(genre_update.name)
    else:
        raise HTTPException(
            status_code=400, detail="Missing required fields. Provide either ID or name."
        )

    if genre_update.name is not None:
        genre.name = genre_update.name

    # Relationship updates (Genre.books via BookGenreLink) should be handled by
    # dedicated endpoints to avoid accidental link table corruption.
    return update_genre(genre)


def delete_genre_service(genre_id: int):
    genre = get_genre_by_id(genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found.")
    msg = delete_genre(genre_id)
    return msg

