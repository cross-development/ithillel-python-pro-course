"""Query and handler to get all students."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetStudentsQuery(BaseModel):
    pass


class GetStudentsQueryHandler:
    """Handler for GetStudentsQuery."""

    @staticmethod
    def handle(query: GetStudentsQuery, db: Session) -> list[schemas.Student]:
        students = db.query(schemas.Student).all()

        return students
