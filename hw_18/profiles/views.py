"""
Class-based views for handling interactions.
"""

from typing import Any, Dict

from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView, TemplateView

from .models import UserProfile
from .forms import RegistrationForm, UserProfileForm, PasswordChangeForm


class RegisterView(FormView):
    """
    A view for registering a new user.
    """

    template_name = 'profiles/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

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
        UserProfile.objects.create(user=user)

        login(self.request, user)

        return super().form_valid(form)


class EditProfileView(LoginRequiredMixin, UpdateView):
    """
    A view for editing a user's profile.
    """

    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self) -> UserProfile:
        """
        Retrieves the user's profile object.

        Returns:
            UserProfile: The user's profile.
        """

        return self.request.user.userprofile


class ChangePasswordView(LoginRequiredMixin, FormView):
    """
    A view for changing a user's password.
    """

    template_name = 'profiles/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Adds the current user to the form kwargs.

        Returns:
            Dict[str, Any]: Form keyword arguments.
        """

        kwargs: Dict[str, Any] = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def form_valid(self, form: PasswordChangeForm) -> Any:
        """
        Handles a valid password change form.

        Args:
            form (PasswordChangeForm): The valid form.

        Returns:
            Any: Response for successful password change.
        """

        self.request.user.set_password(form.cleaned_data['new_password'])
        self.request.user.save()

        messages.success(self.request, 'Your password has been successfully updated!')

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    A view for displaying a user's profile.
    """

    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Adds the user's profile to the template context.

        Returns:
            Dict[str, Any]: Context data for the template.
        """

        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.userprofile

        return context
