"""Command and handler to update an existing student."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class UpdateStudentCommand(BaseModel):
    name: str


class UpdateStudentCommandHandler:
    """Handler for UpdateStudentCommand."""

    @staticmethod
    def handle(command: UpdateStudentCommand, student_id: int, db: Session) -> schemas.Student:
        student = db.query(schemas.Student).filter(schemas.Student.id == student_id).first()

        if not student:
            raise Exception(f"Student with id {student_id} not found")

        student.name = command.name

        db.commit()
        db.refresh(student)

        return student
