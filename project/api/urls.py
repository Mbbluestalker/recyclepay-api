from api.views import RequestPasswordResetEmail
from django.urls import path


urlpatterns = [
    path('auth/reset-password/<str:encoded_email>', RequestPasswordResetEmail.as_view(), name='reset-password'),
]