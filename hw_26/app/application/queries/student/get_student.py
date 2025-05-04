"""Query and handler to get details of a student by their id."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetStudentQuery(BaseModel):
    id: int


class GetStudentQueryHandler:
    """Handler for GetStudentQuery."""

    @staticmethod
    def handle(query: GetStudentQuery, db: Session) -> schemas.Student:
        student = db.query(schemas.Student).filter(schemas.Student.id == query.id).first()

        if not student:
            raise Exception(f"Student with id {query.id} not found")

        return student
