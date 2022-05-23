from db.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ForgetPasswordTestCase(APITestCase):
    def setUp(self):

        self.email = "dummy@gmail.com"
        self.password = "123456"
        User.objects.create(email=self.email, password=self.password)

    def test_forget_password_check(self):
        email = self.email
        response = self.client.post(reverse("forgot-password"), {"email": email})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forget_password_without_email(self):
        response = self.client.post("auth/forgot-password", json="")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_forget_password_wrong_email(self):
        response = self.client.post("auth/forgot-password", json={"email": "j.akpa@yahoo.com"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
