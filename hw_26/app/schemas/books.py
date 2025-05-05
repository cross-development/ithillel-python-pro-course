"""
Data validation schemas module.

This module defines the Pydantic models for request/response validation.
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.authors import Author

from app.schemas.genres import Genre


class BookBase(BaseModel):
    """Base schema for book data"""

    title: str
    publication_date: date
    author_id: int


class BookCreate(BookBase):
    """Schema for book creation"""

    genre_ids: List[int] = []


class Book(BookBase):
    """Schema for book response data"""

    id: int
    author: Author
    genres: List[Genre] = []

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    """Schema for book updates"""

    title: Optional[str] = None
    publication_date: Optional[date] = None
    author_id: Optional[int] = None
    genre_ids: Optional[List[int]] = None
