"""Command and handler to delete a student."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class DeleteStudentCommand(BaseModel):
    id: int


class DeleteStudentCommandHandler:
    """Handler for DeleteStudentCommand."""

    @staticmethod
    def handle(command: DeleteStudentCommand, db: Session) -> None:
        student = db.query(schemas.Student).filter(schemas.Student.id == command.id).first()

        if not student:
            raise Exception(f"Student with id {command.id} not found")

        db.delete(student)
        db.commit()
