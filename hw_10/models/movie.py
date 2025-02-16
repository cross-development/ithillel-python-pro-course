"""
Movie models for the Cinema Database.
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class Movie:
    """
    Data class representing a movie.
    """

    id: Optional[int] = None
    title: str = ""
    release_year: int = 0
    genre: str = ""
