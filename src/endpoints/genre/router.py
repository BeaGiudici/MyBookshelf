# Genre endpoints
from fastapi import APIRouter

from src.endpoints.genre.add_genre import router as add_genre_router
from src.endpoints.genre.delete_genre import router as delete_genre_router
from src.endpoints.genre.get_all_genres import router as get_all_genres_router
from src.endpoints.genre.get_genre import router as get_genre_router
from src.endpoints.genre.update_genre import router as update_genre_router

router = APIRouter()

router.include_router(add_genre_router)
router.include_router(get_all_genres_router)
router.include_router(get_genre_router)
router.include_router(update_genre_router)
router.include_router(delete_genre_router)

