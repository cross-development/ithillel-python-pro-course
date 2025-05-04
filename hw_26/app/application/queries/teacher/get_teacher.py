"""Query and handler to get details of a teacher by their id."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetTeacherQuery(BaseModel):
    id: int


class GetTeacherQueryHandler:
    """Handler for GetTeacherQuery."""

    @staticmethod
    def handle(query: GetTeacherQuery, db: Session) -> schemas.Teacher:
        teacher = db.query(schemas.Teacher).filter(schemas.Teacher.id == query.id).first()

        if not teacher:
            raise Exception(f"Teacher with id {query.id} not found")

        return teacher
