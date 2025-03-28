"""
Module for custom middleware implementations.
"""

import logging

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class ProtectedAccessLogMiddleware(MiddlewareMixin):
    """
    Middleware to log access attempts to protected pages.
    """

    PROTECTED_PATHS = ['/dashboard/']

    def process_request(self, request: HttpRequest) -> None:
        """
        Log access attempts to protected pages.

        Args:
            request (HttpRequest): The incoming request object.
        """

        if request.path in self.PROTECTED_PATHS:
            user: str = request.user.username if request.user.is_authenticated else 'Anonymous'
            logger.info(f"Access attempt to {request.path} by {user}")


class ErrorHandlingMiddleware(MiddlewareMixin):
    """
    Middleware to handle and log 404 and 500 errors.
    """

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        """
        Log 404 and 500 errors.

        Args:
            request (HttpRequest): The incoming request object.
            response (HttpResponse): The outgoing response object.

        Returns:
            HttpResponse: The original response object.
        """

        if response.status_code == 404:
            logger.warning(f"404 error for path {request.path}")
        elif response.status_code == 500:
            logger.error(f"500 error for path {request.path}")

        return response
