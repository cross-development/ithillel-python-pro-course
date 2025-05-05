"""
Database models module.

This module defines the SQLAlchemy ORM models for Book and Genre entities
with appropriate relationships.
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

from app.database import Base

# Association table for many-to-many relationship between Book and Genre
book_genre_association = Table(
    'book_genre',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)
