"""Command and handler to create a teacher."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class CreateTeacherCommand(BaseModel):
    name: str


class CreateTeacherCommandHandler:
    """Handler for CreateTeacherCommand."""

    @staticmethod
    def handle(command: CreateTeacherCommand, db: Session) -> schemas.Teacher:
        teacher = schemas.Teacher(name=command.name)

        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        return teacher
