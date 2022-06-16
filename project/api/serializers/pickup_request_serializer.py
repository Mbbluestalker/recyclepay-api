from rest_framework import serializers


class PickupRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    