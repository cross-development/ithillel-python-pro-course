"""
Data validation schemas module.

This module defines the Pydantic models for request/response validation.
"""

from pydantic import BaseModel


class GenreBase(BaseModel):
    """Base schema for genre data"""

    name: str


class GenreCreate(GenreBase):
    """Schema for genre creation"""

    pass


class Genre(GenreBase):
    """Schema for genre response data"""

    id: int

    class Config:
        orm_mode = True
