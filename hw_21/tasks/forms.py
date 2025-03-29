"""
TaskForm definition.

This module provides a form for creating a new task, including
validation to ensure due dates are not set in the past.
"""

from datetime import datetime

from django import forms
from django.utils import timezone


class TaskForm(forms.Form):
    """
    Form for creating a new task.
    """

    title = forms.CharField(max_length=255, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Task Description")
    due_date = forms.DateTimeField(label="Due Date")

    def clean_due_date(self) -> datetime:
        """
        Validate that due_date is not in the past.

        Returns:
            datetime: The validated due_date.

        Raises:
            forms.ValidationError: If due_date is earlier than now.
        """

        due_date: datetime = self.cleaned_data["due_date"]

        if due_date < timezone.now():
            raise forms.ValidationError("Due date cannot be in the past.")

        return due_date
