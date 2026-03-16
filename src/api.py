from fastapi import FastAPI
from src.endpoints.author.router import router as author_router
from src.endpoints.book.router import router as book_router
from src.endpoints.genre.router import router as genre_router
from src.endpoints.status.router import router as status_router
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from src.endpoints.health import router as health_router
from prometheus_client import Counter
import time
from src.observability.logging import get_logger
from fastapi import Request
from src.observability.tracing import trace_context
from src.observability import setup_observability
from fastapi.responses import JSONResponse

setup_observability()

app = FastAPI(name="My Bookshelf", version="0.1.0")

logger = get_logger(__name__)

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
FastAPIInstrumentor.instrument_app(app)

app.include_router(health_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(genre_router)
app.include_router(status_router)

# Init Prometheus extension 
# Define a counter metric
REQUEST_COUNT = Counter(
"http_requests_total",
"Total HTTP requests",
["method", "endpoint"]
)

# Define the middleware
@app.middleware("http")
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
            service="my-bookshelf",
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
            service="my-bookshelf",
            endpoint=request.url.path,
            method=request.method,
            status_code=500,
            latency_ms=latency_ms,
            error_type=type(exc).__name__,
            error_message=str(exc),
            **trace_context(),
        ).opt(exception=True).error("server error")
        return JSONResponse(status_code=500, content={"error": type(exc).__name__, "message": str(exc)})