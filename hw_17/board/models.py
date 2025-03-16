"""
Database models for the application.

This module defines the database models used in the application. Each model
corresponds to a table in the database.
"""

from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    Attributes:
        phone_number (str): User's phone number (optional).
        address (str): User's address (optional).
    """

    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        """
        Return username as string representation.
        """

        return self.username


class Category(models.Model):
    """
    Category model for organizing ads.

    Attributes:
        name (str): Unique category name.
        description (str): Optional category description.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def active_ads_count(self) -> int:
        """
        Return number of active ads in this category.
        """

        return self.ads.filter(is_active=True).count()

    def __str__(self) -> str:
        """
        Return category name as string representation.
        """

        return self.name


class Ad(models.Model):
    """
    Advertisement model with metadata and relationships.

    Attributes:
        title (str): Ad title.
        description (str): Ad content.
        price (Decimal): Price with validation.
        created_at (datetime): Auto-set creation timestamp.
        updated_at (datetime): Auto-updated modification timestamp.
        is_active (bool): Ad visibility status.
        user (FK): Creator relationship.
        category (FK): Category relationship.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name="ads", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="ads", on_delete=models.CASCADE)

    def get_short_description(self) -> str:
        """
        Return first 100 characters of description with ellipsis.
        """

        return f"{self.description[:100]}..." if len(self.description) > 100 else self.description

    def deactivate_old_ads(self) -> None:
        """
        Deactivate ad if older than 30 days.
        """

        if timezone.now() - self.created_at > timedelta(days=30):
            self.is_active = False
            self.save()

    def __str__(self) -> str:
        """
        Return ad title as string representation.
        """

        return self.title


class Comment(models.Model):
    """
    Comment model for user feedback on ads.

    Attributes:
        content (str): Comment text.
        created_at (datetime): Auto-set creation timestamp.
        ad (FK): Associated advertisement.
        user (FK): Comment author.
    """

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)

    def get_comment_count(self) -> int:
        """
        Return number of comments for the ad.
        """

        return self.ad.comments.count()

    def __str__(self) -> str:
        """
        Return comment summary with author and ad title.
        """

        return f"Comment by {self.user.username} on {self.ad.title}"
