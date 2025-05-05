"""Authors API endpoints."""

from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, Query

from app import schemas, models
from app.dependencies import get_db

router = APIRouter()


@router.post("", response_model=schemas.Author, summary="Create a new author")
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Create a new author in the database.

    Args:
        author (schemas.AuthorCreate): The author data to create
        db (Session): The database session

    Returns:
        models.Author: The created author
    """

    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


@router.get("", response_model=List[schemas.Author], summary="Retrieve all authors")
def read_authors(
        skip: int = Query(0, description="Number of records to skip"),
        limit: int = Query(100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
):
    """
    Retrieve a list of all authors from the database with optional pagination.

    Args:
        skip (int): Number of records to skip (for pagination)
        limit (int): Maximum number of records to return
        db (Session): The database session

    Returns:
        List[models.Author]: List of authors
    """

    authors = db.query(models.Author).offset(skip).limit(limit).all()

    return authors


@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an author by ID.

    Args:
        author_id (int): ID of the author to retrieve
        db (Session): The database session

    Returns:
        models.Author: The requested author
    """

    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return db_author


@router.patch("/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author_update: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Update an author's information.

    Args:
        author_id (int): ID of the author to update
        author_update (schemas.AuthorCreate): New author data
        db (Session): The database session

    Returns:
        models.Author: The updated author
    """

    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    for key, value in author_update.model_dump().items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)

    return db_author


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """
    Delete an author from the database.

    Args:
        author_id (int): ID of the author to delete
        db (Session): The database session

    Returns:
        dict: Success message
    """

    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(db_author)
    db.commit()

    return {"message": "Author deleted successfully"}
