""" URL Configuration for core auth """
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.reset_password_view import PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView


urlpatterns = [
    path('password_reset', RequestPasswordResetEmail.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', SetNewPasswordAPIView.as_view(), name='password_reset_complete'),
    
]