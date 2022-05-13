from rest_framework import generics, response, status, exceptions

from ..serializers import register_serializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Success',
                                      'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            raise exceptions.ValidationError(serializer.errors)
