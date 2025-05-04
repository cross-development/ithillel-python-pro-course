"""Command and handler to update an existing meeting."""

from datetime import datetime

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class UpdateMeetingCommand(BaseModel):
    topic: str
    datetime: datetime


class UpdateMeetingCommandHandler:
    """Handler for UpdateMeetingCommand."""

    @staticmethod
    def handle(command: UpdateMeetingCommand, meeting_id: int, db: Session) -> schemas.Meeting:
        meeting = db.query(schemas.Meeting).filter(schemas.Meeting.id == meeting_id).first()

        if not meeting:
            raise Exception(f"Meeting with id {meeting_id} not found")

        meeting.topic = command.topic
        meeting.datetime = command.datetime

        db.commit()
        db.refresh(meeting)

        return meeting
