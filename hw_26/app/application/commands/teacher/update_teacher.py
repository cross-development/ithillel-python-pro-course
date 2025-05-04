"""Command and handler to update an existing teacher."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class UpdateTeacherCommand(BaseModel):
    name: str


class UpdateTeacherCommandHandler:
    """Handler for UpdateTeacherCommand."""

    @staticmethod
    def handle(command: UpdateTeacherCommand, teacher_id: int, db: Session) -> schemas.Teacher:
        teacher = db.query(schemas.Teacher).filter(schemas.Teacher.id == teacher_id).first()

        if not teacher:
            raise Exception(f"Teacher with id {teacher_id} not found")

        teacher.name = command.name

        db.commit()
        db.refresh(teacher)

        return teacher
