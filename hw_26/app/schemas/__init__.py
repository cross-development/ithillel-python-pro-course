# Import all schemas to make them available when importing the schemas package

from app.schemas.authors import Author, AuthorCreate
from app.schemas.genres import Genre, GenreCreate
from app.schemas.books import Book, BookCreate, BookUpdate

__all__ = [
    "Author",
    "AuthorCreate",
    "Genre",
    "GenreCreate",
    "Book",
    "BookCreate",
    "BookUpdate",
]
