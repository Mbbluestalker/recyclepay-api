from django.urls import reverse
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from db.models import User

from lib import Util


test_email = Util.encode_email('dummy@gmail.com')
print(test_email)


user_data={
            'email': 'dummy@gmail.com',
            'otp': '1234',
            'new_password': 'dummy123'
        }


class TestResetPassword(APITestCase):
    
    def setUp(self):
        self.reset_password_url = reverse('reset-password', args=[test_email])
        
        self.user = User.objects.create(
            email='dummy@gmail.com',
            password='admin@123',
            first_name='Mr',
            last_name='Solu',
            otp = '12345',
            is_verified=True,
            is_admin=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.user_data={
            'email': 'dummy@gmail.com',
            'otp': self.user.otp,
            'new_password': 'dummy123'
        }
        
        
    def test_user_can_reset_password_with_no_data(self):
        response = self.client.post(self.reset_password_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_reset_password_wrong_email(self):
        self.user_data = {"email": "wrong@email.com"}
        response = self.client.post(self.reset_password_url, kwargs=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(mail.outbox), 0)
        
    def test_reset_password_inactive_user(self):    
        self.user_data = {"email": self.user_data["email"]}
        response = self.client.post(self.reset_password_url, kwargs=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


