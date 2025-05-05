"""
Database models module.

This module defines the SQLAlchemy ORM models for an Author entity
with appropriate relationships.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class Author(Base):
    """
    Author model representing book authors.

    Attributes:
        id (int): Unique identifier
        name (str): Full name of the author
        birth_date (Date): Author's date of birth
        books (List[Book]): Books written by the author
    """

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    books = relationship("Book", back_populates="author")
