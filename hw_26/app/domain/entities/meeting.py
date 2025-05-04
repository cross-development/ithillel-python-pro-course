"""Domain entity: Meeting."""

from typing import List
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Meeting:
    id: int
    topic: str
    datetime: datetime
    teacher_id: int
    student_ids: List[int]
