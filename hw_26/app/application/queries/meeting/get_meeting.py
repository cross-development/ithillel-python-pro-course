"""Query and handler to get details of a meeting by its id."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetMeetingQuery(BaseModel):
    id: int


class GetMeetingQueryHandler:
    """Handler for GetMeetingQuery."""

    @staticmethod
    def handle(query: GetMeetingQuery, db: Session) -> schemas.Meeting:
        meeting = db.query(schemas.Meeting).filter(schemas.Meeting.id == query.id).first()

        if not meeting:
            raise Exception(f"Meeting with id {query.id} not found")

        return meeting
