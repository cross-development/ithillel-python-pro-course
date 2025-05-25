"""
Serializers for the books app.

This module defines the serializers for converting Book models to JSON and vice versa.
"""

from typing import Dict, Any

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Book


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    Handles serialization and deserialization of User objects.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        Create and return a new User instance, given the validated data.

        Args:
            validated_data (Dict[str, Any]): The validated user data.

        Returns:
            User: The newly created user.
        """

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

        return user


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.

    Handles serialization and deserialization of Book objects.
    """

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'publication_year', 'created_at', 'user')

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate that the book is unique based on title, author, and publication_year.

        Args:
            data (Dict[str, Any]): The data to validate.

        Returns:
            Dict[str, Any]: The validated data.

        Raises:
            serializers.ValidationError: If a book with the same title, author and
                                         publication_year already exists.
        """

        # Get the current instance if we're updating
        instance = getattr(self, 'instance', None)

        # Check if a book with the same title, author, and year already exists
        title = data.get('title')
        author = data.get('author')
        publication_year = data.get('publication_year')

        if title and author and publication_year:
            query = Book.objects.filter(
                title=title,
                author=author,
                publication_year=publication_year
            )

            # If we're updating, exclude the current instance
            if instance:
                query = query.exclude(pk=instance.pk)

            if query.exists():
                raise serializers.ValidationError({
                    'non_field_errors': ['A book with this title, author, and publication year already exists.']
                })

        return data
