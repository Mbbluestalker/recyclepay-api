from db.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class LoginLogoutTestCase(APITestCase):
    def setup(self):
        self.client = APIClient()
        self.email = "admin@gmail.com"
        self.password = "admin@123"
        user = User.objects.create_user(email=self.email, password=self.password)
        user.save()

    def test_empty_input(self):
        user_data = {"email": "", "password": ""}
        res = self.client.post(reverse("login"), user_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unverified_user(self):
        user_data = {"email": "admin@gmail.com", "password": "admin"}
        res = self.client.post(reverse("login"), user_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incorrect_email_or_password(self):
        user_data = {"email": "admi@gmail.com", "password": "adin@123"}
        res = self.client.post(reverse("login"), user_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout(self):
        res = self.client.post(reverse("logout"))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
