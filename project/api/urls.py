from django.urls import path
from api.views import RegisterApiView, LoginView, LogoutView, VerifyEmail, ForgotpasswordAPIViews



urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/forgot-password", ForgotpasswordAPIViews.as_view(), name="forgot-password"),
    path("auth/verify/<str:encoded_email>", VerifyEmail.as_view(), name="verify_email"),
    path("auth/register/", RegisterApiView.as_view(), name="api-register"),
]
