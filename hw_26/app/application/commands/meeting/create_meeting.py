"""Command and handler to create a meeting."""

from typing import List
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class CreateMeetingCommand(BaseModel):
    topic: str
    datetime: datetime
    teacher_id: int
    student_ids: List[int]


class CreateMeetingCommandHandler:
    """Handler for CreateMeetingCommand."""

    @staticmethod
    def handle(command: CreateMeetingCommand, db: Session) -> schemas.Meeting:
        teacher = db.query(schemas.Teacher).get(command.teacher_id)
        students = db.query(schemas.Student).filter(schemas.Student.id.in_(command.student_ids)).all()

        meeting = schemas.Meeting(
            topic=command.topic,
            datetime=command.datetime,
            teacher=teacher,
            students=students,
        )

        db.add(meeting)
        db.commit()
        db.refresh(meeting)

        return meeting
