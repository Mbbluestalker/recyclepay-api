from api.serializers.forgotPasswordSerializer import ForgotPasswordSerializer
from db.models.user_model import User
from django.contrib.sites.shortcuts import get_current_site
from lib.utils import Util
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class ForgotpasswordAPIViews(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
                encoded_email = Util.encode_email(email)
                # link = f"{get_current_site(request).domain}/api/v1/auth/reset-password/{encoded_email}"
                link = f"http://localhost:3000/reset-password/{encoded_email}"
                user.otp = Util.generate_otp()
                user.save()
                data = {
                    "to_email": [user.email],
                    "email_body": f"""You're receiving this email because you requested a password reset for your account.
                    It can be safely ignored if you did not request a password reset. 
                    Click on this link {link} and use the OTP code {user.otp} to reset password.""",
                    "email_subject": "RESET PASSWORD",
                }
                Util.send_email(data)
                return Response(
                    {"success": "We have sent you a link to reset your password"},
                    status=status.HTTP_200_OK,
                )
            except User.DoesNotExist:
                return Response(
                    {"message":"Wrong email, please enter a correct email"},
                    status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
