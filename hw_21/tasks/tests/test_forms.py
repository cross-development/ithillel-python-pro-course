"""
Test suite for TaskForm.

This module contains unit tests for validating the behavior of the TaskForm.
"""

import pytest
from typing import Dict, Any

from django.utils import timezone

from tasks.forms import TaskForm


@pytest.mark.django_db
class TestTaskForm:
    """
    Test suite for TaskForm.

    This class contains test cases to ensure that TaskForm correctly validates input data.
    """

    def test_valid_form(self) -> None:
        """
        Test that the form is valid when all required fields are provided correctly.

        The form should pass validation when the title, description, and a due_date
        in the future are supplied.
        """

        data: Dict[str, Any] = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": timezone.now() + timezone.timedelta(days=1)
        }
        form: TaskForm = TaskForm(data=data)

        assert form.is_valid(), "Form should be valid with correct data."

    def test_missing_title(self) -> None:
        """
        Test that the form is invalid if the title field is missing.

        The form should return an error indicating that the title field is required.
        """

        data: Dict[str, Any] = {
            "description": "This is a test task.",
            "due_date": timezone.now() + timezone.timedelta(days=1)
        }
        form: TaskForm = TaskForm(data=data)

        assert not form.is_valid(), "Form should be invalid without title."
        assert "title" in form.errors, "Title field should have an error."

    def test_past_due_date(self) -> None:
        """
        Test that the form is invalid if the due_date is set in the past.

        The form should return an error indicating that the due_date must be in the future.
        """

        data: Dict[str, Any] = {
            "title": "Test Task",
            "description": "This is a test task.",
            "due_date": timezone.now() - timezone.timedelta(days=1)
        }
        form: TaskForm = TaskForm(data=data)

        assert not form.is_valid(), "Form should be invalid with past due_date."
        assert "due_date" in form.errors, "Due_date field should have an error."
