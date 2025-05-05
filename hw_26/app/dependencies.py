# Dependency to get database session

from app.database import SessionLocal


def get_db():
    """
    Dependency to get a database session.

    Yields:
        Session: A SQLAlchemy database session
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
