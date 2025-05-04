"""Command and handler to create a student."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class CreateStudentCommand(BaseModel):
    name: str


class CreateStudentCommandHandler:
    """Handler for CreateStudentCommand."""

    @staticmethod
    def handle(command: CreateStudentCommand, db: Session) -> schemas.Student:
        student = schemas.Student(name=command.name)

        db.add(student)
        db.commit()
        db.refresh(student)

        return student
