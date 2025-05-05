"""Genres API endpoints."""

from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, Query

from app import schemas, models
from app.dependencies import get_db

router = APIRouter()


@router.post("", response_model=schemas.Genre, summary="Create a new genre")
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    """
    Create a new genre in the database.

    Args:
        genre (schemas.GenreCreate): The genre data to create
        db (Session): The database session

    Returns:
        models.Genre: The created genre
    """

    db_genre = models.Genre(**genre.model_dump())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)

    return db_genre


@router.get("", response_model=List[schemas.Genre], summary="Retrieve all genres")
def read_genres(
        skip: int = Query(0, description="Number of records to skip"),
        limit: int = Query(100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
):
    """
    Retrieve a list of all genres from the database with optional pagination.

    Args:
        skip (int): Number of records to skip (for pagination)
        limit (int): Maximum number of records to return
        db (Session): The database session

    Returns:
        List[models.Genre]: List of genres
    """

    genres = db.query(models.Genre).offset(skip).limit(limit).all()

    return genres


@router.get("/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a genre by ID.

    Args:
        genre_id (int): ID of the genre to retrieve
        db (Session): The database session

    Returns:
        models.Genre: The requested genre
    """

    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()

    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    return db_genre


@router.patch("/{genre_id}", response_model=schemas.Genre)
def update_genre(genre_id: int, genre_update: schemas.GenreCreate, db: Session = Depends(get_db)):
    """
    Update a genre's information.

    Args:
        genre_id (int): ID of the genre to update
        genre_update (GenreCreate): New genre data
        db (Session): The database session

    Returns:
        models.Genre: The updated genre
    """

    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()

    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    for key, value in genre_update.model_dump().items():
        setattr(db_genre, key, value)

    db.commit()
    db.refresh(db_genre)

    return db_genre


@router.delete("/{genre_id}")
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Delete a genre from the database.

    Args:
        genre_id (int): ID of the genre to delete
        db (Session): The database session

    Returns:
        dict: Success message
    """

    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()

    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    db.delete(db_genre)
    db.commit()

    return {"message": "Genre deleted successfully"}
