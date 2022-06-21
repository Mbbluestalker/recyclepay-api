from api.permissions import IsCollector
from api.serializers import PickupsUpdateSerializer
from db.models import Order
from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status
from lib.utils import Util


class PickupsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = PickupsUpdateSerializer
    permission_classes = [IsCollector]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        order = get_object_or_404(Order, id=kwargs['id'])

        if request.user != order.picked_by:
            return response.Response(data={'message': 'Order can only be completed by whoever accepted the request'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            order.status = 'completed'
            weight_in_kg = serializer.validated_data['weight_in_kg']
            order.weight_in_kg = weight_in_kg
            order.save()

            requested_by = order.requested_by
            requested_by.points_earned += Util.points_earned(weight_in_kg)

            return response.Response({'message': 'Successfully updated', 'data': self.serializer_class(order).data}, status=status.HTTP_200_OK)
        return response.Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
