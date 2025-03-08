"""
URL configuration for the home app.

This module defines URL patterns for the home application, mapping URLs
to their respective view functions.
"""

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile'),
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.event_view, name='event'),
]
