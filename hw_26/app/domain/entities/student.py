"""Domain entity: Student."""

from dataclasses import dataclass


@dataclass
class Student:
    id: int
    name: str
