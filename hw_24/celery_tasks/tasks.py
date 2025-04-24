"""
Celery tasks for the application.

This module defines tasks to be executed asynchronously.
"""

import logging

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
        subject = "Welcome to Book Library!"
        message = f"""
            Hello {user.username},
    
            Thank you for registering at our Book Library service!
            You can now log in and start adding your favorite books to the library.
    
            Best regards,
            Book Library Team
            """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

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
        subject = "Discover Our Book Library Features!"
        message = f"""
            Hello {user.username},
    
            Thank you for joining our Book Library!
    
            Here are some features you might enjoy:
            - Add and manage your personal book collection
            - Search for books by title, author, or genre
            - Track your reading progress
            - Connect with other book lovers
    
            We hope you enjoy using our service!
    
            Best regards,
            Book Library Team
            """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

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
