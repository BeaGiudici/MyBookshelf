# Author endpoints
from src.endpoints.author.add_author import router as add_author_router
from src.endpoints.author.get_all_authors import router as read_all_authors_router
from src.endpoints.author.get_author import router as read_author_router
from src.endpoints.author.update_author import router as update_author_router
from src.endpoints.author.delete_author import router as delete_author_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(add_author_router)
router.include_router(read_all_authors_router)
router.include_router(read_author_router)
router.include_router(update_author_router)
router.include_router(delete_author_router)