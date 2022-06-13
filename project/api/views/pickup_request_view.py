from api.permissions.pickup_request_permission import IsIndividualOrParner
from api.serializers.pickup_request_serializer import PickupRequestSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from db.models import Category, Order


class PickUpRequestAPI(CreateAPIView):
    serializer_class = PickupRequestSerializer
    permission_classes = [IsIndividualOrParner]
    authentication_classes = [TokenAuthentication]

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data['title']
            category = serializer.validated_data['category'].capitalize()
            location = serializer.validated_data['location']
            try:
                category = Category.objects.get(name=category)
                order = Order.objects.create(title=title, category=category, location=location)
                order.requested_by = request.user
                order.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({'error':f'could not find category with name {category}'}, status=status.HTTP_400_BAD_REQUEST)   
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
