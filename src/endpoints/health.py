########################################################
#
# Health check endpoint
#
########################################################

from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from prometheus_client import generate_latest, Counter, CONTENT_TYPE_LATEST

HEALTH_CHECK_COUNTER = Counter("health_check_total", "Number of health checks")

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

