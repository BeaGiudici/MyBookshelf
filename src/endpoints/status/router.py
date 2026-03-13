# Status endpoints
from fastapi import APIRouter

from src.endpoints.status.add_status import router as add_status_router
from src.endpoints.status.delete_status import router as delete_status_router
from src.endpoints.status.get_all_statuses import router as get_all_statuses_router
from src.endpoints.status.get_status import router as get_status_router
from src.endpoints.status.update_status import router as update_status_router

router = APIRouter()

router.include_router(add_status_router)
router.include_router(get_all_statuses_router)
router.include_router(get_status_router)
router.include_router(update_status_router)
router.include_router(delete_status_router)

