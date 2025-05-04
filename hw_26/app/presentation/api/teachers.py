"""Teacher API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db
from app.application.queries.teacher.get_teacher import GetTeacherQuery, GetTeacherQueryHandler
from app.application.queries.teacher.get_teachers import GetTeachersQuery, GetTeachersQueryHandler
from app.application.commands.teacher.create_teacher import CreateTeacherCommand, CreateTeacherCommandHandler
from app.application.commands.teacher.update_teacher import UpdateTeacherCommand, UpdateTeacherCommandHandler
from app.application.commands.teacher.delete_teacher import DeleteTeacherCommand, DeleteTeacherCommandHandler

router = APIRouter()


@router.post("")
def create_teacher(
        cmd: CreateTeacherCommand,
        db: Session = Depends(get_db),
):
    teacher = CreateTeacherCommandHandler.handle(cmd, db)

    return teacher


@router.get("")
def get_all_teachers(
        db: Session = Depends(get_db),
):
    query = GetTeachersQuery()
    teachers = GetTeachersQueryHandler.handle(query, db)

    return teachers


@router.get("/{teacher_id}")
def get_teacher(
        teacher_id: int,
        db: Session = Depends(get_db),
):
    query = GetTeacherQuery(id=teacher_id)
    teacher = GetTeacherQueryHandler.handle(query, db)

    return teacher


@router.patch("/{teacher_id}")
def update_teacher(
        teacher_id: int,
        cmd: UpdateTeacherCommand,
        db: Session = Depends(get_db),
):
    updated_teacher = UpdateTeacherCommandHandler.handle(cmd, teacher_id, db)

    return updated_teacher


@router.delete("/{teachert_id}")
def delete_teacher(
        teacher_id: int,
        db: Session = Depends(get_db),
):
    command = DeleteTeacherCommand(id=teacher_id)
    DeleteTeacherCommandHandler.handle(command, db)

    return {"message": "Teacher deleted successfully"}
