"""Main application entrypoint."""

from fastapi import FastAPI

from app.infrastructure.database.schemas import Base
from app.infrastructure.database.session import engine
from app.presentation.websocket import websocket_routes
from app.presentation.api.router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meeting Scheduler", version="0.1.0")

app.include_router(api_router)
app.include_router(websocket_routes.router)
