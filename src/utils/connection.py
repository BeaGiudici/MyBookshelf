# Utils for connection to the database

from sqlmodel import Session
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

connection: psycopg2.extensions.connection | None = None

def get_connection() -> psycopg2.extensions.connection:
    """Get a connection to the database"""
    global connection
    if connection is None:
        connection = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT, url=DB_URL)
        print(f"Connected to database: {DB_URL}")
    return connection
    
def close_connection() -> None:
    """Close the connection to the database"""
    global connection
    if connection is not None:
        connection.close()
        connection = None
        print("Disconnected from database")
    
def get_session() -> Session:
    """Get a session to the database"""
    connection = get_connection()
    return Session(connection)