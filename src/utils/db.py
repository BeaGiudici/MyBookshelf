import psycopg2
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_URL = os.getenv("DB_URL")


def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created.")
    else:
        print(f"Database '{DB_NAME}' already exists.")
    cursor.close()
    conn.close()


def create_tables(engine):
    # Import models so they are registered on SQLModel.metadata
    from src.schemas import author as _author  # noqa: F401
    from src.schemas import book as _book  # noqa: F401
    from src.schemas import book_genre_link as _book_genre_link  # noqa: F401
    from src.schemas import genre as _genre  # noqa: F401
    from src.schemas import status as _status  # noqa: F401

    SQLModel.metadata.create_all(engine)


def delete_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = '{DB_NAME}' AND pid <> pg_backend_pid()
    """)
    cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' deleted.")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database", default=False)
    parser.add_argument(
        "--debug", action="store_true", default=False, help="Show debug information"
    )
    args = parser.parse_args()

    if args.reset:
        delete_database()

    create_database()
    engine = create_engine(DB_URL, echo=args.debug)
    create_tables(engine)
    print(f"Database '{DB_NAME}' ready.")
