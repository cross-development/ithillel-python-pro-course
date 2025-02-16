"""
Actor models for the Cinema Database.
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class Actor:
    """
    Data class representing an actor.
    """

    id: Optional[int] = None
    name: str = ""
    birth_year: int = 0
