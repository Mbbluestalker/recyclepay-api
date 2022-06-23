from api.serializers.reset_password_serializer import ResetPasswordSerializer
from db.models.user_model import User
from lib.utils import Util
from rest_framework import generics, status, permissions
from rest_framework.response import Response


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, encoded_email):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            otp = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']
            email = Util.decode_email(encoded_email)
            print(email)
            user = User.objects.get(email=email)
            if user.otp != otp:
                return Response({'message': 'Error', 'data': 'The otp provided is not correct' }, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()

            return Response(data={'otp':otp ,'messsage': 'success', 'data': 'The new password set was successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        