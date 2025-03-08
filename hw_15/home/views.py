"""
Django views for rendering different pages.

This module defines views for various pages such as home, about, contact,
individual posts, user profiles, and event details.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: Rendered home page.
    """

    context = {
        'title': 'Home Page',
        'description': 'This is a home page'
    }

    return render(request, 'home/home.html', context)


def about_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the about page.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: Rendered about page.
    """

    context = {
        'title': 'About Page',
        'description': 'This is a about page'
    }

    return render(request, 'home/about.html', context)


def contact_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the contact page.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: Rendered contact page.
    """

    context = {
        'title': 'Contact Page',
        'description': 'This is a contact page'
    }

    return render(request, 'home/contact.html', context)


def post_view(request: HttpRequest, id: int) -> HttpResponse:
    """
    Renders a specific post page.

    Args:
        request (HttpRequest): The incoming request object.
        id (int): The ID of the post.

    Returns:
        HttpResponse: Rendered post page.
    """

    context = {
        'title': f'Post #{id}',
        'description': f'You are viewing a post with ID: {id}'
    }

    return render(request, 'home/post.html', context)


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    """
    Renders a user profile page.

    Args:
        request (HttpRequest): The incoming request object.
        username (str): The username of the profile being viewed.

    Returns:
        HttpResponse: Rendered profile page.
    """

    context = {
        'title': f'Profile {username}',
        'description': f"You are viewing a user's profile: {username}"
    }

    return render(request, 'home/profile.html', context)


def event_view(request: HttpRequest, year: int, month: int, day: int) -> HttpResponse:
    """
    Renders an event page for a specific date.

    Args:
        request (HttpRequest): The incoming request object.
        year (int): The year of the event.
        month (int): The month of the event.
        day (int): The day of the event.

    Returns:
        HttpResponse: Rendered event page.
    """

    context = {
        'title': 'Event Page',
        'description': f'Date of event: {year}-{month}-{day}'
    }

    return render(request, 'home/event.html', context)
