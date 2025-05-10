"""
Defines the Customer model used to represent customer data.

Includes basic fields such as email, name, and timestamps.
"""

from django.db import models


class Customer(models.Model):
    """
    Model representing a customer.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Returns a string representation of the Customer."""

        return self.email
