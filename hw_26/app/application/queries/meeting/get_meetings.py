"""Query and handler to get all meetings."""

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.database import schemas


class GetMeetingsQuery(BaseModel):
    pass


class GetMeetingsQueryHandler:
    """Handler for GetMeetingsQuery."""

    @staticmethod
    def handle(query: GetMeetingsQuery, db: Session) -> list[schemas.Meeting]:
        meetings = db.query(schemas.Meeting).all()

        return meetings
