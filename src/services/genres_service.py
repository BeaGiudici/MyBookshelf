from fastapi import HTTPException
from sqlmodel import Session
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

from src.observability.metrics import get_genres_updated_counter, get_genres_retrieved_counter, get_genres_deleted_counter, get_genres_created_counter
from src.observability.tracing import get_tracer
from src.observability.logging import get_logger

tracer = get_tracer(__name__)
logger = get_logger(__name__)

def get_all_genres_service(session: Session):
    with tracer.start_as_current_span("get_all_genres_service"):
        genres = get_all_genres(session)
        if genres is None:
            logger.error("No genres found.")
            raise HTTPException(status_code=404, detail="No genres found.")
        logger.info(f"Genres retrieved successfully: {genres}")
        get_genres_retrieved_counter().add(len(genres))
        return genres


def get_genre_by_id_service(session: Session, genre_id: int):
    with tracer.start_as_current_span("get_genre_by_id_service", attributes={"genre_id": genre_id}):
        genre = get_genre_by_id(session, genre_id)
        if genre is None:
            logger.error(f"Genre with ID {genre_id} not found.")
            raise HTTPException(
                status_code=404, detail=f"Genre with ID {genre_id} not found."
            )
        logger.info(f"Genre retrieved successfully: {genre}")
        get_genres_retrieved_counter().add(1)
        return genre


def get_genre_by_name_service(session: Session, genre_name: str):
    genre = get_genre_by_name(session, genre_name)
    if genre is None:
        raise HTTPException(
            status_code=404, detail=f"Genre with name {genre_name} not found."
        )
    return genre


def add_genre_service(session: Session, new_genre: GenreCreate):
    with tracer.start_as_current_span("add_genre_service"):
        if new_genre.name is None:
            logger.error("Missing required fields")
            raise HTTPException(status_code=400, detail="Missing required fields")

        existing = get_genre_by_name(session, new_genre.name)
        if existing is not None:
            logger.error(f"Genre {new_genre.name} already exists.")
            raise HTTPException(status_code=400, detail="Genre already exists.")

        genre = Genre(name=new_genre.name)
        logger.info(f"Genre created successfully: {genre}")
        get_genres_created_counter().add(1)
        return add_genre(session, genre)


def update_genre_service(session: Session, genre_update: GenreUpdate):
    with tracer.start_as_current_span("update_genre_service"):
        if genre_update.id is not None:
            genre = get_genre_by_id(session, genre_update.id)
        elif genre_update.name is not None:
            genre = get_genre_by_name(session, genre_update.name)
        else:
            logger.error("Missing required fields. Provide either ID or name.")
            raise HTTPException(
                status_code=400, detail="Missing required fields. Provide either ID or name."
            )

        if genre_update.name is not None:
            genre.name = genre_update.name

        logger.info(f"Genre updated successfully: {genre}")
        get_genres_updated_counter().add(1)
        return update_genre(session, genre)


def delete_genre_service(session: Session, genre_id: int):
    with tracer.start_as_current_span("delete_genre_service", attributes={"genre_id": genre_id}):
        genre = get_genre_by_id(session, genre_id)
        if genre is None:
            logger.error(f"Genre with ID {genre_id} not found.")
            raise HTTPException(status_code=404, detail="Genre not found.")
        logger.info(f"Genre deleted successfully: {genre}")
        get_genres_deleted_counter().add(1)
        msg = delete_genre(session, genre_id)
        return msg

