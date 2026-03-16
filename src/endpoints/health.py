########################################################
#
# Health check endpoint
#
########################################################

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from prometheus_client import generate_latest, Counter, CONTENT_TYPE_LATEST

HEALTH_CHECK_COUNTER = Counter("health_check_total", "Number of health checks")

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

# Init Prometheus extension 
# Define a counter metric
REQUEST_COUNT = Counter(
"http_requests_total",
"Total HTTP requests",
["method", "endpoint"]
)

# Define the middleware
@router.middleware("http")
async def request_log_middleware(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
        latency_ms = int((time.perf_counter() - start) * 1000)

        status = response.status_code
        level = "info"
        error_type = None
        message = "request completed"

        if 400 <= status < 500:
            level = "warning"
            message = "client error"
            error_type = f"HTTP_{status}"

        extra = dict(
            service=SERVICE_NAME,
            endpoint=request.url.path,
            method=request.method,
            status_code=status,
            latency_ms=latency_ms,
            **trace_context(),
        )
        if error_type:
            extra["error_type"] = error_type

        logger.bind(**extra).log(level.upper(), message)
        return response
    except Exception as exc:
        latency_ms = int((time.perf_counter() - start) * 1000)
        logger.bind(
            service=SERVICE_NAME,
            endpoint=request.url.path,
            method=request.method,
            status_code=500,
            latency_ms=latency_ms,
            error_type=type(exc).__name__,
            **trace_context(),
        ).error("server error")
        return JSONResponse(status_code=500, content={"error": type(exc).__name__})

# Define the metrics endpoint
@router.get("/metrics")
def metrics():
	return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
