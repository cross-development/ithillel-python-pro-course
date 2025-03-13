"""
Views module for the main application.

This module defines view functions and class-based views for rendering
pages such as Home, About, Contact, and Services.
"""

from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """

    context: Dict[str, str] = {
        'title': "Home Page",
        'description': "Welcome to our website!",
    }

    return render(request, 'main/home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    """
    Renders the about page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about page template.
    """

    context: Dict[str, Any] = {
        'title': "About Us",
        'description': "We are a company providing IT consulting services. <b>Our mission</b> is to deliver high-quality solutions.",
        'last_updated': "2023-10-01",
        'years_in_business': 5,
    }

    return render(request, 'main/about.html', context)


class ContactView(TemplateView):
    """
    Renders the contact page using a class-based view.

    Attributes:
        template_name (str): Path to the contact page template.
    """

    template_name: str = "main/contact.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Adds contact details to the context.

        Args:
            **kwargs (Any): Additional keyword arguments.

        Returns:
            Dict[str, Any]: Context dictionary with contact information.
        """

        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['title'] = "Contact Us"
        context['contacts'] = {
            'address': "Kyiv, Main St, 1",
            'phone': "+380123456789",
            'email': "info@example.com",
        }

        return context


class ServiceView(TemplateView):
    """
    Renders the services page with optional filtering.

    Attributes:
        template_name (str): Path to the services page template.
    """

    template_name: str = "main/services.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Adds a list of services to the context, with optional search filtering.

        Args:
            **kwargs (Any): Additional keyword arguments.

        Returns:
            Dict[str, Any]: Context dictionary with filtered or full list of services.
        """

        context: Dict[str, Any] = super().get_context_data(**kwargs)
        query: str = self.request.GET.get('query', '')
        all_services: list[Dict[str, str]] = [
            {'name': "Website Development", 'description': "We create modern websites from scratch."},
            {'name': "SEO Optimization", 'description': "Improve your website's visibility in search engines."},
            {'name': "Technical Support", 'description': "Ensure uninterrupted operation of your product."},
        ]

        context['title'] = "Our Services"

        if query:
            context['services'] = [s for s in all_services if query.lower() in s['name'].lower()]
        else:
            context['services'] = all_services

        return context
