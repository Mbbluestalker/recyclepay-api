from api.serializers.login_logout_serializer import UserLoginSerializer
from db.models.user_model import User
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                return Response(
                    data={
                        "message": "error",
                        "data": "Ensure email and password are correct and you have verified your account",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            else:
                if not user.is_verified:
                    return Response(
                        data={
                            "message": "error",
                            "data": "Please verify your account before you log in.",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if user.is_verified and user.check_password(password):
                        token, _ = Token.objects.get_or_create(user=user)
                        return Response(
                            data={"token": token.key,
                                  "success": "You've successfully Logged in",
                                  "user_type": user.user_type()},
                            status=status.HTTP_200_OK,
                        )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        request.user.auth_token.delete()
        return Response(data={"success": "You've been logged out"}, status=status.HTTP_200_OK)
