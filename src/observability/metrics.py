########################################################
#
# OpenTelemetry metrics: counters
#
########################################################

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Defining counters for the metrics
_meter: metrics.Meter | None = None

_books_created_counter: metrics.Counter | None = None
_books_deleted_counter: metrics.Counter | None = None
_books_updated_counter: metrics.Counter | None = None
_books_retrieved_counter: metrics.Counter | None = None
_authors_created_counter: metrics.Counter | None = None
_authors_deleted_counter: metrics.Counter | None = None
_authors_retrieved_counter: metrics.Counter | None = None
_authors_updated_counter: metrics.Counter | None = None
_genres_created_counter: metrics.Counter | None = None
_genres_deleted_counter: metrics.Counter | None = None
_genres_retrieved_counter: metrics.Counter | None = None
_genres_updated_counter: metrics.Counter | None = None

def setup_metrics(resource: Resource, otlp_endpoint: str) -> None:
    global _meter
    exporter = OTLPMetricExporter(endpoint=otlp_endpoint, insecure=True)
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=15000)
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(provider)
    _meter = metrics.get_meter("my-bookshelf")
    _register_instruments()


def _register_instruments() -> None:
    global _books_created_counter, _books_deleted_counter, _books_updated_counter, _books_retrieved_counter, _authors_created_counter, _authors_deleted_counter, _authors_updated_counter, _authors_retrieved_counter, _genres_created_counter, _genres_deleted_counter, _genres_updated_counter, _genres_retrieved_counter

    assert _meter is not None

    _books_created_counter = _meter.create_counter(
        name="books.created",
        description="Number of books created",
        unit="1",
    )
    _books_deleted_counter = _meter.create_counter(
        name="books.deleted",
        description="Number of books deleted",
        unit="1",
    )
    _books_updated_counter = _meter.create_counter(
        name="books.updated",
        description="Number of books updated",
        unit="1",
    )
    _books_retrieved_counter = _meter.create_counter(
        name="books.retrieved",
        description="Number of books retrieved",
        unit="1",
    )

    _authors_created_counter = _meter.create_counter(
        name="authors.created",
        description="Number of authors created",
        unit="1",
    )
    _authors_deleted_counter = _meter.create_counter(
        name="authors.deleted",
        description="Number of authors deleted",
        unit="1",
    )
    _authors_updated_counter = _meter.create_counter(
        name="authors.updated",
        description="Number of authors updated",
        unit="1",
    )
    _authors_retrieved_counter = _meter.create_counter(
        name="authors.retrieved",
        description="Number of authors retrieved",
        unit="1",
    )

    _genres_created_counter = _meter.create_counter(
        name="genres.created",
        description="Number of genres created",
        unit="1",
    )
    _genres_deleted_counter = _meter.create_counter(
        name="genres.deleted",
        description="Number of genres deleted",
        unit="1",
    )
    _genres_updated_counter = _meter.create_counter(
        name="genres.updated",
        description="Number of genres updated",
        unit="1",
    )
    _genres_retrieved_counter = _meter.create_counter(
        name="genres.retrieved",
        description="Number of genres retrieved",
        unit="1",
    )


def get_books_created_counter() -> metrics.Counter:
    assert _books_created_counter is not None
    return _books_created_counter


def get_books_deleted_counter() -> metrics.Counter:
    assert _books_deleted_counter is not None
    return _books_deleted_counter


def get_books_updated_counter() -> metrics.Counter:
    assert _books_updated_counter is not None
    return _books_updated_counter


def get_books_retrieved_counter() -> metrics.Counter:
    assert _books_retrieved_counter is not None
    return _books_retrieved_counter


def get_authors_created_counter() -> metrics.Counter:
    assert _authors_created_counter is not None
    return _authors_created_counter


def get_authors_deleted_counter() -> metrics.Counter:
    assert _authors_deleted_counter is not None
    return _authors_deleted_counter


def get_authors_updated_counter() -> metrics.Counter:
    assert _authors_updated_counter is not None
    return _authors_updated_counter

def get_authors_retrieved_counter() -> metrics.Counter:
    assert _authors_retrieved_counter is not None
    return _authors_retrieved_counter

def get_genres_created_counter() -> metrics.Counter:
    assert _genres_created_counter is not None
    return _genres_created_counter


def get_genres_deleted_counter() -> metrics.Counter:
    assert _genres_deleted_counter is not None
    return _genres_deleted_counter


def get_genres_updated_counter() -> metrics.Counter:
    assert _genres_updated_counter is not None
    return _genres_updated_counter

def get_genres_retrieved_counter() -> metrics.Counter:
    assert _genres_retrieved_counter is not None
    return _genres_retrieved_counter