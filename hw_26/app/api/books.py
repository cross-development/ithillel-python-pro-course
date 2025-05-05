"""Books API endpoints."""

from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, Query, BackgroundTasks

from app import schemas, models
from app.background_tasks.book_notification import create_book_notification
from app.dependencies import get_db

router = APIRouter()


@router.post("", response_model=schemas.Book, summary="Create a new book")
def create_book(book: schemas.BookCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Create a new book in the database.

    Args:
        book (schemas.BookCreate): The book data to create
        background_tasks (BackgroundTasks): Background task manager
        db (Session): The database session

    Returns:
        models.Book: The created book
    """

    db_author = db.query(models.Author).filter(models.Author.id == book.author_id).first()

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    db_book = models.Book(**book.model_dump(exclude={'genre_ids'}))

    if book.genre_ids:
        genres = db.query(models.Genre).filter(models.Genre.id.in_(book.genre_ids)).all()
        db_book.genres = genres

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    background_tasks.add_task(create_book_notification, db_book.id)

    return db_book


@router.get("", response_model=List[schemas.Book], summary="Retrieve all books")
def read_books(
        skip: int = Query(0, description="Number of records to skip"),
        limit: int = Query(100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
):
    """
    Retrieve a list of all books from the database with optional pagination.

    Args:
        skip (int): Number of records to skip (for pagination)
        limit (int): Maximum number of records to return
        db (Session): The database session

    Returns:
        List[models.Book]: List of books with associated author and genres
    """

    books = db.query(models.Book).offset(skip).limit(limit).all()

    return books


@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a book by ID.

    Args:
        book_id (int): ID of the book to retrieve
        db (Session): The database session

    Returns:
        models.Book: The requested book
    """

    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return db_book


@router.patch("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update a book's information.

    Args:
        book_id (int): ID of the book to update
        book_update (schemas.BookUpdate): New book data
        db (Session): The database session

    Returns:
        models.Book: The updated book
    """

    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book_update.model_dump(exclude={'genre_ids', 'author_id'}, exclude_unset=True).items():
        setattr(db_book, key, value)

    if book_update.author_id is not None:
        db_author = db.query(models.Author).filter(models.Author.id == book_update.author_id).first()

        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")

        db_book.author = db_author

    if book_update.genre_ids is not None:
        genres = db.query(models.Genre).filter(models.Genre.id.in_(book_update.genre_ids)).all()
        db_book.genres = genres

    db.commit()
    db.refresh(db_book)

    return db_book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book from the database.

    Args:
        book_id (int): ID of the book to delete
        db (Session): The database session

    Returns:
        dict: Success message
    """

    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
