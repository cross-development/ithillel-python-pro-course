"""Meeting API endpoints."""

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db
from app.infrastructure.tasks.log_task import log_new_meeting
from app.presentation.websocket.websocket_routes import broadcast_message
from app.application.queries.meeting.get_meeting import GetMeetingQuery, GetMeetingQueryHandler
from app.application.queries.meeting.get_meetings import GetMeetingsQuery, GetMeetingsQueryHandler
from app.application.commands.meeting.create_meeting import CreateMeetingCommand, CreateMeetingCommandHandler
from app.application.commands.meeting.update_meeting import UpdateMeetingCommand, UpdateMeetingCommandHandler
from app.application.commands.meeting.delete_meeting import DeleteMeetingCommand, DeleteMeetingCommandHandler

router = APIRouter()


@router.post("")
def create_meeting(
        cmd: CreateMeetingCommand,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
):
    meeting = CreateMeetingCommandHandler.handle(cmd, db)
    background_tasks.add_task(log_new_meeting, cmd.topic)

    meeting_id = meeting.id
    background_tasks.add_task(broadcast_message, meeting_id,
                              f"A new student has joined the meeting {meeting_id}.")

    return meeting


@router.get("")
def get_all_meetings(
        db: Session = Depends(get_db),
):
    query = GetMeetingsQuery()
    meetings = GetMeetingsQueryHandler.handle(query, db)

    return meetings


@router.get("/{meeting_id}")
def get_meeting(
        meeting_id: int,
        db: Session = Depends(get_db),
):
    query = GetMeetingQuery(id=meeting_id)
    meeting = GetMeetingQueryHandler.handle(query, db)

    return meeting


@router.patch("/{meeting_id}")
def update_meeting(
        meeting_id: int,
        cmd: UpdateMeetingCommand,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
):
    updated_meeting = UpdateMeetingCommandHandler.handle(cmd, meeting_id, db)

    background_tasks.add_task(broadcast_message, meeting_id, f"Meeting {meeting_id} has been updated.")

    return updated_meeting


@router.delete("/{meeting_id}")
def delete_meeting(
        meeting_id: int,
        db: Session = Depends(get_db),
):
    command = DeleteMeetingCommand(id=meeting_id)
    DeleteMeetingCommandHandler.handle(command, db)

    return {"message": "Meeting deleted successfully"}
