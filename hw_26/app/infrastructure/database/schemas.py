"""SQLAlchemy models for database persistence."""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

student_meeting = Table(
    "student_meeting",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("meeting_id", Integer, ForeignKey("meetings.id")),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    topic = Column(String, nullable=False)
    datetime = Column(DateTime)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher")
    students = relationship("Student", secondary=student_meeting, backref="meetings")
