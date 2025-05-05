# API router

from fastapi import APIRouter

from app.api.authors import router as authors_router
from app.api.books import router as books_router
from app.api.genres import router as genres_router

api_router = APIRouter()

api_router.include_router(books_router, prefix="/books", tags=["Books"])
api_router.include_router(authors_router, prefix="/authors", tags=["Authors"])
api_router.include_router(genres_router, prefix="/genres", tags=["Genres"])
