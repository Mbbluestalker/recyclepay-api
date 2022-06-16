from rest_framework import serializers

from db.models import Order


class AcceptItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status',)
