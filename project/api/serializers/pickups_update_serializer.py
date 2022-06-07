from db.models import Order
from rest_framework import serializers


class PickupsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['title', 'category', 'location', 'requested_by', 'picked_by', 'status', 'weight_in_kg']
        extra_kwargs = {
            'title': {'read_only': True},
            'category': {'read_only': True},
            'location': {'read_only': True},
            'requested_by': {'read_only': True},
            'picked_by': {'read_only': True},
            'status': {'read_only': True}
        }
