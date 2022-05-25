from db.models import User
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField()
