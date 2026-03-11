from __future__ import annotations

import os

import psycopg2
from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

_engine = create_engine(DB_URL) if DB_URL else None
_connection: psycopg2.extensions.connection | None = None


def get_connection() -> psycopg2.extensions.connection:
    """Get a raw psycopg2 connection (rarely needed in the API layer)."""
    global _connection
    if _connection is None:
        _connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
    return _connection


def close_connection() -> None:
    global _connection
    if _connection is not None:
        _connection.close()
        _connection = None


def get_session() -> Session:
    """Get a SQLModel session backed by a SQLAlchemy engine."""
    if _engine is None:
        raise RuntimeError("DB_URL is not set; cannot create SQLModel engine/session.")
    return Session(_engine)