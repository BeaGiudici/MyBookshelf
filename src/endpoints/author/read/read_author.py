from fastapi import APIRouter, HTTPException
from src.schemas.book import Author
from src.utils.connection import get_session
from src.endpoints.author.read.response import error_responses
from sqlmodel import Session

path = "/author/get"
tags = ["author"]
router = APIRouter()
async def get_author_by_name(db: Session, author_name: str):
    author = db.query(Author).filter(Author.name == author_name).first()
    return author

async def get_author_by_id(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.get(path=path, response_model=Author, responses=error_responses, tags=tags)
async def get_author(author_id: int):
    with get_session() as db:
        author = get_author_by_id(db, author_id)
    return author