from django.urls import path

from api.views import RegisterApiView
from api.views.forgotPasswordViews import ForgotpasswordAPIViews

from .views import forgotPasswordViews
from .views.email_verification_view import VerifyEmail


urlpatterns = [
    path("auth/forgot-password", ForgotpasswordAPIViews.as_view(), name="forgot-password"),
    path("auth/verify/<str:encoded_email>", VerifyEmail.as_view(), name="verify_email"),
    path("auth/register/", RegisterApiView.as_view(), name="api-register"),
]
