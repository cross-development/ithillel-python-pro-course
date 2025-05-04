"""Query and handler to get all teachers."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetTeachersQuery(BaseModel):
    pass


class GetTeachersQueryHandler:
    """Handler for GetTeachersQuery."""

    @staticmethod
    def handle(query: GetTeachersQuery, db: Session) -> list[schemas.Teacher]:
        teachers = db.query(schemas.Teacher).all()

        return teachers
