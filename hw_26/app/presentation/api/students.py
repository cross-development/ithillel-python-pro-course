"""Student API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db
from app.application.queries.student.get_student import GetStudentQuery, GetStudentQueryHandler
from app.application.queries.student.get_students import GetStudentsQuery, GetStudentsQueryHandler
from app.application.commands.student.create_student import CreateStudentCommand, CreateStudentCommandHandler
from app.application.commands.student.update_student import UpdateStudentCommand, UpdateStudentCommandHandler
from app.application.commands.student.delete_student import DeleteStudentCommand, DeleteStudentCommandHandler

router = APIRouter()


@router.post("")
def create_student(
        cmd: CreateStudentCommand,
        db: Session = Depends(get_db),
):
    student = CreateStudentCommandHandler.handle(cmd, db)

    return student


@router.get("")
def get_all_students(
        db: Session = Depends(get_db),
):
    query = GetStudentsQuery()
    students = GetStudentsQueryHandler.handle(query, db)

    return students


@router.get("/{student_id}")
def get_student(
        student_id: int,
        db: Session = Depends(get_db),
):
    query = GetStudentQuery(id=student_id)
    student = GetStudentQueryHandler.handle(query, db)

    return student


@router.patch("/{student_id}")
def update_student(
        student_id: int,
        cmd: UpdateStudentCommand,
        db: Session = Depends(get_db),
):
    updated_student = UpdateStudentCommandHandler.handle(cmd, student_id, db)

    return updated_student


@router.delete("/{student_id}")
def delete_student(
        student_id: int,
        db: Session = Depends(get_db),
):
    command = DeleteStudentCommand(id=student_id)
    DeleteStudentCommandHandler.handle(command, db)

    return {"message": "Student deleted successfully"}
