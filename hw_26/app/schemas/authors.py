"""
Data validation schemas module.

This module defines the Pydantic models for request/response validation.
"""

from datetime import date

from pydantic import BaseModel


class AuthorBase(BaseModel):
    """Base schema for author data"""

    name: str
    birth_date: date


class AuthorCreate(AuthorBase):
    """Schema for author creation"""

    pass


class Author(AuthorBase):
    """Schema for author response data"""

    id: int

    class Config:
        orm_mode = True
