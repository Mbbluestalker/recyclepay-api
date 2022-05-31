from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from api.permissions import IsCollector
from api.serializers import AcceptItemOrderSerializer
from db.models import Order

    
class AcceptItemView(generics.GenericAPIView):
    serializer_class = AcceptItemOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCollector]
    
    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
            order.picked_by = request.user
            order.status = 'accepted'
            order.save()
            return Response({'message': 'Successfully accepted request!'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error': 'This order no longer exists!'}, status=status.HTTP_400_BAD_REQUEST)    
    