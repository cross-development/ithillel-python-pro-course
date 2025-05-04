"""Command and handler to delete a meeting."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class DeleteMeetingCommand(BaseModel):
    id: int


class DeleteMeetingCommandHandler:
    """Handler for DeleteMeetingCommand."""

    @staticmethod
    def handle(command: DeleteMeetingCommand, db: Session) -> None:
        meeting = db.query(schemas.Meeting).filter(schemas.Meeting.id == command.id).first()

        if not meeting:
            raise Exception(f"Meeting with id {command.id} not found")

        db.delete(meeting)
        db.commit()
