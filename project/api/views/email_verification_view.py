from db.models import User
from lib.utils import Util
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class VerifyEmail(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, encoded_email):
        try:
            decoded_email = Util.decode_email(encoded_email)
            user = User.objects.get(email=decoded_email)
            user.is_verified = True
            user.save()
            return Response(
                {"message": "success", "data": "Your account has been successfully verified"},
                status=status.HTTP_200_OK,
            )
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(data={"Invalid activation link!"}, status=status.HTTP_400_BAD_REQUEST)
