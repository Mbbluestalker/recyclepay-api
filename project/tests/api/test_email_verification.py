from db.models import User
from django.test import TestCase
from django.urls import reverse
from lib.utils import Util
from rest_framework import status
from rest_framework.test import APIClient


class TestEmailVerification(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.verify_email_url = "verify_email"
        self.email = "dummy@gmail.com"
        self.password = "123456"
        user = User.objects.create_user(email=self.email, password=self.password)
        user.save()
        self.encoded_email = Util.encode_email(self.email)

    def test_verification(self):
        res = self.client.get(
            reverse(self.verify_email_url, kwargs={"encoded_email": self.encoded_email})
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_verification_with_unauthorized_email(self):
        encoded_email = "ZHVtZHVtQG1haWwuY29t"
        res = self.client.get(
            reverse(self.verify_email_url, kwargs={"encoded_email": encoded_email})
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verification_with_empty_url(self):
        encoded_email = " "
        res = self.client.get(
            reverse(self.verify_email_url, kwargs={"encoded_email": encoded_email})
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
