from rest_framework import generics, status
from serializers.reset_password_serializer import RequestPasswordResetEmail
from rest_framework.response import Response
from db.models.user_model import User
from lib.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmail
    
    def post(self, request, encoded_email):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']
            email = Util.decode_email(encoded_email)
            user = User.objects.get(email=email)
            if user.otp != otp:
                return Response({'message': 'Error', 'data': 'The otp provided is not correct' }, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save(status=status.HTTP_200_OK)
            return Response({'messsage': 'success', 'data': 'The new_password set was successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        