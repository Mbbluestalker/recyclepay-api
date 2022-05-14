from random import randint

from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, response, status, exceptions

from ..serializers import register_serializer
from ..utils import Utils


class RegisterApiView(generics.CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        otp = randint(10000, 99999)
        url = f'{get_current_site(request).domain}/api/v1/users/verify-email?otp={otp}/'

        # Send OTP to the serializer to save
        serializer.context['otp'] = otp

        if serializer.is_valid():
            email_data = {
                'subject': 'Registration Complete',
                'body': f"You have successfully registered on Recycle Pay."
                        f" Please click {url} to verify your account",
                'receiver': request.data['email']
            }

            try:
                Utils.send_email(email_data)
                serializer.save()
                return response.Response({'message': 'Success',
                                          'data': serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as err:
                raise exceptions.ValidationError({'message': err})
        else:
            raise exceptions.ValidationError(serializer.errors)
