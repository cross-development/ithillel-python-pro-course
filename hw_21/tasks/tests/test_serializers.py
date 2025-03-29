"""
Test suite for TaskSerializer.

This module contains unit tests to validate the behavior of TaskSerializer,
ensuring proper data validation and error handling.
"""

import pytest
from typing import Dict, Any

from django.utils import timezone
from tasks.serializers import TaskSerializer


@pytest.mark.django_db
def test_valid_serializer() -> None:
    """
    Test that the serializer is valid with correct data.

    This test verifies that the serializer correctly accepts valid
    task data and successfully validates it.
    """

    data: Dict[str, Any] = {
        "title": "Test Task",
        "description": "This is a test task.",
        "due_date": (timezone.now() + timezone.timedelta(days=1)).isoformat()
    }
    serializer: TaskSerializer = TaskSerializer(data=data)

    assert serializer.is_valid(), "Serializer should be valid with correct data."


@pytest.mark.django_db
def test_missing_title() -> None:
    """
    Test that the serializer is invalid if the title field is missing.

    This test ensures that the serializer correctly detects the absence
    of the required 'title' field and raises a validation error.
    """

    data: Dict[str, Any] = {
        "description": "This is a test task.",
        "due_date": (timezone.now() + timezone.timedelta(days=1)).isoformat()
    }
    serializer: TaskSerializer = TaskSerializer(data=data)

    assert not serializer.is_valid(), "Serializer should be invalid without title."
    assert "title" in serializer.errors, "Title field should have an error."


@pytest.mark.django_db
def test_past_due_date() -> None:
    """
    Test that the serializer is invalid if the due_date is in the past.

    This test checks that the serializer properly detects and rejects
    past due dates, ensuring valid scheduling constraints.
    """

    data: Dict[str, Any] = {
        "title": "Test Task",
        "description": "This is a test task.",
        "due_date": (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer: TaskSerializer = TaskSerializer(data=data)

    assert not serializer.is_valid(), "Serializer should be invalid with past due_date."
    assert "due_date" in serializer.errors, "Due_date field should have an error."
