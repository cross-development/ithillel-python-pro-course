"""
Views for the books app.

This module defines the API views for book-related operations.
"""

from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Book
from .filters import BookFilter
from .permissions import IsAdminUserForDeletion
from .serializers import BookSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model.

    Provides CRUD operations for books with proper permissions.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ('title',)
    ordering_fields = ('publication_year', 'title')
    permission_classes = (IsAuthenticated, IsAdminUserForDeletion)

    def perform_create(self, serializer: BookSerializer) -> None:
        """
        Associate the current user with the book being created.

        Args:
            serializer (BookSerializer): The serializer instance.
        """

        serializer.save(user=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    Allows new users to register.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
