# Book endpoints
from src.endpoints.book.add_book import router as add_book_router
from src.endpoints.book.get_all_books import router as read_all_books_router
from src.endpoints.book.get_book import router as read_book_router
from src.endpoints.book.update_book import router as update_book_router
from src.endpoints.book.delete_book import router as delete_book_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(add_book_router)
router.include_router(read_all_books_router)
router.include_router(read_book_router)
router.include_router(update_book_router)
router.include_router(delete_book_router)
