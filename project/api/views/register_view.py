from random import randint

from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, response, status, exceptions

from ..serializers import register_serializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        otp = randint(10000, 99999)
        url = f'{get_current_site(request).domain}/api/v1/users/verify-email?otp={otp}/'

        print(url)

        if serializer.is_valid():
            # serializer.save()
            return response.Response({'message': 'Success',
                                      'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            raise exceptions.ValidationError(serializer.errors)
