""" URL Configuration for core auth """
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.reset_password_view import RequestPasswordResetEmail


urlpatterns = [
    path('auth/reset-password/<str:encoded_email>', RequestPasswordResetEmail.as_view(), name='reset-password'),
]