from .models import Book
import threading

_books = {}
_lock = threading.Lock()

def create_book(author: str, title: str, isbn: str):
  """
  Create a Book entry
  """
  book = Book(title=title, author=author, isbn=isbn)
  with _lock:
    _books[book.isbn] = book
  return book