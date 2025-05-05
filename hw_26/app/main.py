"""
FastAPI application module.
"""

import logging

from fastapi import FastAPI

from app.database import engine, Base
from app.api.router import api_router
from app.websockets.websocket_endpoints import router as websocket_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Author-Book-Genre Management System",
    description="A FastAPI project demonstrating CRUD operations, database relationships, and Docker deployment",
    version="1.0.0"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(api_router)
app.include_router(websocket_router)
