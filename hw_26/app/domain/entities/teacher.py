"""Domain entity: Teacher."""

from dataclasses import dataclass


@dataclass
class Teacher:
    id: int
    name: str
