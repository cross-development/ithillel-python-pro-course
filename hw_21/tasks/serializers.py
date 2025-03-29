"""
Task and User serializers.

This module defines serializers for handling task data,
including validation and nested user representation.
"""

from datetime import datetime

from django.utils import timezone
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    """
    Serializer for task data.
    """

    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    due_date = serializers.DateTimeField()

    def validate_due_date(self, value: datetime) -> datetime:
        """
        Validate that due_date is not in the past.

        Args:
            value (datetime): The due_date value to validate.

        Returns:
            datetime: The validated due_date.

        Raises:
            serializers.ValidationError: If due_date is in the past.
        """

        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")

        return value


class UserSerializer(serializers.Serializer):
    """
    Serializer for user data validation.
    """

    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class TaskWithUserSerializer(serializers.Serializer):
    """
    Serializer for task data with nested user.
    """

    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    due_date = serializers.DateTimeField()
    user = UserSerializer()

    def validate_due_date(self, value: datetime) -> datetime:
        """
        Validate that due_date is not in the past.

        Args:
            value (datetime): The due_date value to validate.

        Returns:
            datetime: The validated due_date.

        Raises:
            serializers.ValidationError: If due_date is in the past.
        """

        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")

        return value
