from django.urls import path

from .views.register_view import RegisterApiView


urlpatterns = [
    path('auth/register/', RegisterApiView.as_view(), name='api-register'),
]
