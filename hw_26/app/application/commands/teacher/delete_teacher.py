"""Command and handler to delete a teacher."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class DeleteTeacherCommand(BaseModel):
    id: int


class DeleteTeacherCommandHandler:
    """Handler for DeleteTeacherCommand."""

    @staticmethod
    def handle(command: DeleteTeacherCommand, db: Session) -> None:
        teacher = db.query(schemas.Teacher).filter(schemas.Teacher.id == command.id).first()

        if not teacher:
            raise Exception(f"Teacher with id {command.id} not found")

        db.delete(teacher)
        db.commit()
