from fastapi import APIRouter

from .meetings import router as meetings_router
from .students import router as students_router
from .teachers import router as teachers_router

api_router = APIRouter()

api_router.include_router(meetings_router, prefix="/meetings", tags=["Meetings"])
api_router.include_router(students_router, prefix="/students", tags=["Students"])
api_router.include_router(teachers_router, prefix="/teachers", tags=["Teachers"])
