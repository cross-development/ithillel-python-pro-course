"""
Forms for the application.

This module defines the forms used in the application.
"""

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating new comments.
    """

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        }
