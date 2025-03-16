"""
Signal handlers for ad-related actions.
"""

from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save

from .models import Ad


@receiver(post_save, sender=Ad)
def send_email_notification(sender: type[Ad], instance: Ad, created: bool, **kwargs) -> None:
    """
    Send email notification when a new ad is created.

    Args:
        sender (type[Ad]): Model class sending the signal.
        instance (Ad): Ad instance being saved.
        created (bool): Boolean indicating if this is a new record.
    """

    if created:
        send_mail(
            subject=f"New ad created: {instance.title}",
            message=f"Your ad '{instance.title}' has been successfully published.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.user.email],
        )


@receiver(post_save, sender=Ad)
def check_ad_expiry(sender: type[Ad], instance: Ad, **kwargs) -> None:
    """
    Check and deactivate expired ads.

    Args:
        sender (type[Ad]): Model class sending the signal.
        instance (Ad): Ad instance being saved.
    """

    instance.deactivate_old_ads()
