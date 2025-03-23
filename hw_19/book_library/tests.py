"""
Tests for the books app.

This module defines the tests for the book library API.
"""

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

from .models import Book


class BookAPITestCase(TestCase):
    """
    Test case for Book API endpoints.
    
    Tests the CRUD operations, filtering, and permissions.
    """

    def setUp(self) -> None:
        """
        Set up data for tests.
        
        Creates test users and books.
        """

        # Create regular user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

        # Create admin user
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='adminpassword',
            is_staff=True
        )

        # Create another regular user
        self.another_user = User.objects.create_user(
            username='anotheruser',
            email='another@example.com',
            password='anotherpassword'
        )

        # Create a book
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            genre='Test Genre',
            publication_year=2023,
            user=self.user
        )

        # Initialize client
        self.client = APIClient()

    def get_token(self, username: str, password: str) -> str:
        """
        Get JWT token for a user.
        
        Args:
            username: The username of the user.
            password: The password of the user.
            
        Returns:
            str: JWT access token.
        """

        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': username, 'password': password},
            format='json'
        )

        return response.data['access']

    def test_get_books_authenticated(self) -> None:
        """
        Test that authenticated users can get a list of books.
        """

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Get books
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_books_unauthenticated(self) -> None:
        """
        Test that unauthenticated users cannot get books.
        """

        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book(self) -> None:
        """
        Test creating a new book as an authenticated user.
        """

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Create book
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'genre': 'New Genre',
            'publication_year': 2024
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).user, self.user)

    def test_create_duplicate_book(self) -> None:
        """
        Test creating a duplicate book should fail.
        """

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Try to create a duplicate book
        url = reverse('book-list')
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'genre': 'Different Genre',
            'publication_year': 2023
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual(Book.objects.count(), 1)

    def test_update_book_owner(self) -> None:
        """
        Test that the owner of a book can update it.
        """

        # Login as the book owner
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Update book
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Updated Book',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'publication_year': 2023
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_update_book_non_owner(self) -> None:
        """
        Test that non-owners cannot update a book.
        """

        # Login as another user (not the book owner)
        token = self.get_token('anotheruser', 'anotherpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Try to update book
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Hacked Book',
            'author': 'Hacker',
            'genre': 'Hacking',
            'publication_year': 2024
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Test Book')

    def test_delete_book_admin(self) -> None:
        """
        Test that admin users can delete books.
        """

        # Login as admin
        token = self.get_token('admin', 'adminpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Delete book
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_non_admin(self) -> None:
        """
        Test that non-admin users cannot delete books.
        """

        # Login as regular user (even as the book owner)
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Try to delete book
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self) -> None:
        """
        Test filtering books by author.
        """

        # Create additional books
        Book.objects.create(
            title='Python Book',
            author='Python Author',
            genre='Programming',
            publication_year=2022,
            user=self.user
        )
        Book.objects.create(
            title='Django Book',
            author='Python Author',
            genre='Web Development',
            publication_year=2021,
            user=self.user
        )

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Filter books by author
        url = reverse('book-list') + '?author=Python Author'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_search_books(self) -> None:
        """
        Test searching books by title.
        """

        # Create additional books
        Book.objects.create(
            title='Python Programming',
            author='Python Author',
            genre='Programming',
            publication_year=2022,
            user=self.user
        )
        Book.objects.create(
            title='Django Web Framework',
            author='Django Author',
            genre='Web Development',
            publication_year=2021,
            user=self.user
        )

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Search books by title
        url = reverse('book-list') + '?search=Python'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Python Programming')

    def test_ordering_books(self) -> None:
        """
        Test ordering books by publication year.
        """

        # Create additional books with different years
        Book.objects.create(
            title='Old Book',
            author='Old Author',
            genre='Classic',
            publication_year=1950,
            user=self.user
        )
        Book.objects.create(
            title='Newer Book',
            author='New Author',
            genre='Modern',
            publication_year=2000,
            user=self.user
        )

        # Login as regular user
        token = self.get_token('testuser', 'testpassword')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Order books by publication_year ascending
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Old Book')

        # Order books by publication_year descending
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')
