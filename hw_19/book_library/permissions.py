"""
Custom permissions for the books app.

This module defines custom permission classes for book-related operations.
"""

from typing import Any

from rest_framework.views import View
from rest_framework import permissions
from rest_framework.request import Request


class IsAdminUserForDeletion(permissions.BasePermission):
    """
    Custom permission that allows:
    - Read (GET) and create (POST) operations for any authenticated user.
    - Delete (DELETE) operations only for admin users.
    - Update (PUT, PATCH) operations only for the owner of the object.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Checks if the user has permission for the requested operation.

        Args:
            request (Request): The request instance.
            view (View): The view handling the request.

        Returns:
            bool: True if the user has the required permission, False otherwise.
        """

        # Allow GET, POST operations for any authenticated user
        if request.method in ['GET', 'POST']:
            return request.user and request.user.is_authenticated

        # For DELETE operations, only allow admin users
        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        # For PUT, PATCH operations, check object-level permission in has_object_permission
        return True

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        """
        Checks if the user has permission to perform actions on a specific object.

        Args:
            request (Request): The request instance.
            view (View): The view handling the request.
            obj (Any): The object being accessed.

        Returns:
            bool: True if the user has the required permission, False otherwise.
        """

        # Read permissions are allowed to any authenticated request
        if request.method in permissions.SAFE_METHODS:
            return True

        # DELETE permissions only for admins
        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        # Write permissions (PUT, PATCH) only for the book owner
        return obj.user == request.user
