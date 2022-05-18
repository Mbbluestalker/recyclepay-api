from django.urls import path

# from .views.register_view import RegisterApiView
from api.views import RegisterApiView


urlpatterns = [
    path('auth/register/', RegisterApiView.as_view(), name='api-register'),
]
