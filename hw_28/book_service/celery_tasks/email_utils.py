"""
Utilities for sending emails via celery tasks.
"""

from typing import Tuple

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_mail_to_user(user: User, subject: str, message: str) -> None:
    """
    Send an email to a given user.

    Args:
        user (User): The Django User instance to email.
        subject (str): The subject line of the email.
        message (str): The body content of the email.

    Raises:
        SMTPException: If sending the email fails and `fail_silently` is False.
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


def get_registration_email_content(user: User) -> Tuple[str, str]:
    """
    Generate the subject and body for a new-user registration email.

    Args:
        user (User): The Django User instance who just registered.

    Returns:
        Tuple[str, str]: A tuple containing (subject, message).
    """

    subject: str = "Welcome to Book Library!"
    message: str = f"""
        Hello {user.username},
        
        Thank you for registering at our Book Library service!
        You can now log in and start adding your favorite books to the library.
        
        Best regards,
        Book Library Team
        """

    return subject, message


def get_promo_email_content(user: User) -> Tuple[str, str]:
    """
    Generate the subject and body for a promotional email.

    Args:
        user (User): The Django User instance to send the promo to.

    Returns:
        Tuple[str, str]: A tuple containing (subject, message).
    """

    subject: str = "Discover Our Book Library Features!"
    message: str = f"""
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

    return subject, message
