from rest_framework import generics, status
from serializers.reset_password_serializer import ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.response import Response
from db.models.user_model import User
from utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
# from drf_yasg import openapi
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data  )
        
        email = request.data['email']
        
        if User.objects.filter(email = email).exists():
                user = User.objects.get(email = email)
                uidb64 =  urlsafe_base64_encode(user.id)
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request = request).domain
                relativeLink = reverse('password-reset-confirm', kwargs = {'uidb64': uidb64, 'token': token})
                absurl = 'http://'+current_site + relativeLink
                email_body = 'Hello, \n Use link below to reset your password \n' + absurl
                data = {'email_body': email_body, 'to_email': user.email,
                        'email_subject': 'Reset your password'}
                        
                Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status = status.HTTP_200_OK)
        
        
class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status = status.HTTP_401_UNAUTHORIZED)
            
            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status = status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status = status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset successful'}, status = status.HTTP_200_OK)
        