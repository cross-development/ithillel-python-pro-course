from fastapi import FastAPI
from fastapi.applications import Lifespan
from contextlib import asynccontextmanager

from .consumers import run_consumer_in_thread


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan:
    """
    FastAPI lifespan context for startup and shutdown events.

    Starts the RabbitMQ consumer in a background thread on startup.

    Yields:
        Lifespan: Control back to FastAPI after startup tasks.
    """

    run_consumer_in_thread()
    yield


app: FastAPI = FastAPI(
    title="Notification Service",
    lifespan=lifespan
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        dict[str, str]: Service status.
    """

    return {"status": "ok"}
