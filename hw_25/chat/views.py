"""
Views for handling chat rooms and user registration.

This module defines views for displaying the list of rooms, room details, and handling room creation.
It also includes an asynchronous API view for room listings and a form for user registration.
"""

from typing import Any

from asgiref.sync import sync_to_async
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

from .models import Room
from .forms import RoomForm, RegistrationForm


class RoomListView(LoginRequiredMixin, TemplateView):
    """
    Display list of all rooms and form to create new one.
    """

    template_name: str = 'chat/room_list.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handles GET requests to display rooms and room creation form.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Keyword arguments passed to the view.

        Returns:
            HttpResponse: The response object with the rendered template.
        """

        form = RoomForm()
        rooms = Room.objects.all()

        return render(request, self.template_name, {'rooms': rooms, 'form': form})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handles POST requests to create a new room.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Keyword arguments passed to the view.

        Returns:
            HttpResponse: The response object with the rendered template or redirect.
        """
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save()
            room.participants.add(request.user)
            return redirect('chat:room-detail', room_name=room.name)

        rooms = Room.objects.all()

        return render(request, self.template_name, {'rooms': rooms, 'form': form})


class RoomDetailView(LoginRequiredMixin, View):
    """
    Display chat room detail and join logic.
    """

    def get(self, request: HttpRequest, room_name: str, *args, **kwargs) -> HttpResponse:
        """
        Handles GET requests to display room details and join the room.

        Args:
            request (HttpRequest): The HTTP request object.
            room_name: The name of the room to display.
            *args: Variable length argument list.
            **kwargs: Keyword arguments passed to the view.

        Returns:
            HttpResponse: The response object with the rendered template.
        """

        room = get_object_or_404(Room, name=room_name)
        # join if not yet participant
        room.participants.add(request.user)

        return render(request, 'chat/room_detail.html', {
            'room_name': room.name,
            'username': request.user.username
        })


class RoomListAsyncAPIView(LoginRequiredMixin, View):
    """
    Async API to list all rooms (DB query in async context).
    """

    async def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handles async GET requests to list rooms.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Keyword arguments passed to the view.

        Returns:
            HttpResponse: The response object with the rendered template.
        """

        rooms = await sync_to_async(list)(Room.objects.values('name'))

        return render(request, 'chat/room_list.html', {'rooms': rooms, 'form': RoomForm()})


class RegisterView(FormView):
    """
    A view for registering a new user.
    """

    template_name: str = 'chat/register.html'
    form_class = RegistrationForm
    success_url: str = reverse_lazy('chat:room-list')

    def form_valid(self, form: RegistrationForm) -> Any:
        """
        Handles a valid registration form.

        Args:
            form (RegistrationForm): The valid form.

        Returns:
            Any: Response for successful registration.
        """

        user: User = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        login(self.request, user)

        return super().form_valid(form)
