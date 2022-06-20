from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, response, status, permissions

from api.serializers import register_serializer
from lib.utils import Util


class RegisterApiView(generics.CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        otp = Util.generate_otp()

        # Send OTP to the serializer to save
        serializer.context["otp"] = otp

        if serializer.is_valid():
            user_email = request.data["email"]

            # Code to encode email address
            encoded = Util.encode_email(user_email)

            url = f"{get_current_site(request).domain}/api/v1/auth/verify/{encoded}"
            email_data = {
                "email_subject": "Recycle-Pay | Registration Complete",
                "email_body": f"You have successfully registered on the Recycle-Pay Platform."
                f" Please click this <a href={url}><b>link</b></a> to verify your account",
                "to_email": [
                    user_email,
                ],
            }

            try:
                Util.send_email(email_data)
                serializer.save()
                return response.Response(
                    {"message": "Success", "data": serializer.data}, status=status.HTTP_201_CREATED
                )
            except Exception as err:
                return response.Response({"message!": str(err)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(
                {"message!": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
