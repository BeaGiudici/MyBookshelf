from . import storage
from models import BookCreate

def create(book_in: BookCreate):
  return storage.create_book(book_in.author, book_in.title, book_in.isbn)

def read_all():
  pass