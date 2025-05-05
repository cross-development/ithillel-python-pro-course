"""
Database models module.

This module defines the SQLAlchemy ORM models for a Genre entity
with appropriate relationships.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from app.database import Base
from app.models.book_genre import book_genre_association


class Genre(Base):
    """
    Genre model representing book genres.

    Attributes:
        id (int): Unique identifier
        name (str): Name of the genre
        books (List[Book]): Books associated with this genre
    """

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre_association, back_populates="genres")
