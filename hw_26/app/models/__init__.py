# Import all models to make them available when importing the models package

from app.models.authors import Author
from app.models.genres import Genre
from app.models.books import Book

__all__ = [
    "Author",
    "Genre",
    "Book",
]
