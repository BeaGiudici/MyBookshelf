from fastapi import FastAPI
from src.endpoints.author.router import router as author_router
from src.endpoints.book.router import router as book_router
from src.endpoints.genre.router import router as genre_router
from src.endpoints.status.router import router as status_router
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from src.endpoints.health import router as health_router

app = FastAPI(name="My Bookshelf", version="0.1.0")

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
FastAPIInstrumentor.instrument_app(app)

app.include_router(health_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(genre_router)
app.include_router(status_router)