import os
from opentelemetry.sdk.resources import Resource
from src.observability.metrics import setup_metrics
from src.observability.tracing import setup_tracing
from src.observability.logging import setup_logging

_DEFAULT_ENDPOINT = "http://localhost:4317"
_DEFAULT_SERVICE_NAME = "my-bookshelf"

def setup_observability() -> None:
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", _DEFAULT_ENDPOINT)
    service_name = os.getenv("OTEL_SERVICE_NAME", _DEFAULT_SERVICE_NAME)
    log_level = os.getenv("OTEL_LOG_LEVEL", "INFO")

    resource = Resource.create(
        {
            "service.name": service_name,
            "service.version": os.getenv("APP_VERSION", "0.1.0"),
        }
    )

    setup_metrics(resource, endpoint)
    setup_tracing(resource, endpoint)
    setup_logging()