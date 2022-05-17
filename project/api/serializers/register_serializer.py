from rest_framework import serializers

from db.models.user_model import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

        # Prevents the password from showing after submission
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])

        # Retrieve OTP from view
        otp = self.context['otp']
        new_user.otp = otp

        new_user.save()
        return new_user
