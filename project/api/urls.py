""" URL Configuration for core auth """
from api.views.reset_password_view import RequestPasswordResetEmail
from django.urls import path


urlpatterns = [
    path('auth/reset-password/<str:encoded_email>', RequestPasswordResetEmail.as_view(), name='reset-password'),
]