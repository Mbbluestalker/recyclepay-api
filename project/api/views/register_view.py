from rest_framework import generics, response, status, permissions

# from ...db.models.user_model import User
from db.models.user_model import User
from ..serializers import register_serializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]



