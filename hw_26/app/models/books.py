"""
Database models module.

This module defines the SQLAlchemy ORM models for a Book entity
with appropriate relationships.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.database import Base
from app.models.book_genre import book_genre_association


class Book(Base):
    """
    Book model representing published books.

    Attributes:
        id (int): Unique identifier
        title (str): Title of the book
        publication_date (Date): Date when book was published
        author_id (int): Foreign key to the author
        author (Author): Reference to the book's author
        genres (List[Genre]): Genres associated with the book
    """

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    publication_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre_association, back_populates="books")
