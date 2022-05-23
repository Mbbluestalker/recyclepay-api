from db.models.user_model import User
from rest_framework import serializers

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=40)
    otp = serializers.CharField(max_length=6)
    confirm_password = serializers.CharField(max_length=40)
    
    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        if new_password != confirm_password:
            raise serializers.ValidationError('The new password must match the confirm password')
        return attrs