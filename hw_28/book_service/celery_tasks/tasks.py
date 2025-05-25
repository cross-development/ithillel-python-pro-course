"""
Celery tasks for the application.

This module defines tasks to be executed asynchronously.
"""

import logging

from celery import shared_task
from django.contrib.auth.models import User

from book_service.celery_tasks.email_utils import send_mail_to_user, get_registration_email_content, \
    get_promo_email_content

logger = logging.getLogger(__name__)


@shared_task
def send_registration_email(user_id: int) -> None:
    """
    Send a welcome email to a newly registered user.

    Args:
        user_id (int): The ID of the user who registered.
    """

    try:
        user = User.objects.get(id=user_id)
        subject, message = get_registration_email_content(user)
        send_mail_to_user(user, subject, message)

        logger.info(f"Registration email sent to user {user.email}")
    except User.DoesNotExist:
        logger.error(f"User with ID {user_id} does not exist")

    except Exception as e:
        logger.error(f"Failed to send registration email: {str(e)}")


@shared_task
def send_promo_email(user_id: int) -> None:
    """
    Send a promotional email to a user 10 minutes after registration.

    Args:
        user_id (int): The ID of the user who registered.
    """

    try:
        user = User.objects.get(id=user_id)
        subject, message = get_promo_email_content(user)
        send_mail_to_user(user, subject, message)

        logger.info(f"Promotional email sent to user {user.email}")
    except User.DoesNotExist:
        logger.error(f"User with ID {user_id} does not exist")

    except Exception as e:
        logger.error(f"Failed to send promotional email: {str(e)}")


@shared_task
def log_user_count() -> int:
    """
    Log the total number of users in the database.
    """

    user_count = User.objects.count()
    logger.info(f"Current user count: {user_count}")

    return user_count
