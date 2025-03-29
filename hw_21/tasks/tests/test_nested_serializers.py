"""
Test suite for TaskWithUserSerializer.

This module contains unit tests to validate the behavior of the
TaskWithUserSerializer, including handling nested UserSerializer data.
"""

import pytest
from typing import Dict, Any

from django.utils import timezone
from django.contrib.auth.models import User

from tasks.serializers import TaskWithUserSerializer


@pytest.mark.django_db
class TestTaskSerializer:
    """
    Test suite for TaskWithUserSerializer with nested UserSerializer.

    This class contains test cases to ensure that TaskWithUserSerializer
    correctly validates and processes nested user data.
    """

    def test_valid_nested_serializer(self) -> None:
        """
        Test that the serializer is valid when provided with correct nested user data.

        This test verifies that the serializer properly accepts valid user information
        and task details, ensuring that the nested UserSerializer functions correctly.
        """

        user: User = User.objects.create_user(username="testuser", email="test@example.com", password="testpass")
        data: Dict[str, Any] = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": (timezone.now() + timezone.timedelta(days=1)).isoformat(),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }
        serializer: TaskWithUserSerializer = TaskWithUserSerializer(data=data)

        assert serializer.is_valid(), "Serializer should be valid with correct nested data."

    def test_invalid_nested_serializer(self) -> None:
        """
        Test that the serializer is invalid when nested user data is incorrect.

        This test ensures that the serializer properly detects errors in the
        nested UserSerializer data, such as an invalid email format.
        """

        data: Dict[str, Any] = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": (timezone.now() + timezone.timedelta(days=1)).isoformat(),
            "user": {
                "username": "testuser",
                "email": "invalid_email"
            }
        }
        serializer: TaskWithUserSerializer = TaskWithUserSerializer(data=data)

        assert not serializer.is_valid(), "Serializer should be invalid with incorrect user data."
        assert "user" in serializer.errors, "User field should have an error."
