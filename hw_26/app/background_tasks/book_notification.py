# Background tasks module for book notification processing.

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_book_notification(book_id: int) -> None:
    """
    Background task to simulate notification processing.

    Args:
        book_id (int): ID of the book that was created
    """

    time.sleep(2)
    logger.info(f"Background task completed for book ID: {book_id}")
