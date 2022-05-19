from django.urls import reverse
from django.core import mail
from rest_framework import status, response
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.reset_password_url = reverse('reset-password')
        
        self.user_data={
            'email': 'dummy@gmail.com',
            'otp': 'otp',
            'new_password': 'dummy123'
        }
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    
class TestResetPassword(TestSetUp):
    
    def test_user_can_reset_password(self):
        response = self.client.post(
            self.reset_password_url, self.user_data, format="json")
        self.assertEqual(response.data['email'], self.user_data('email'))
        self.assertEqual(response.data['otp'], self.user_data('otp'))
        self.assertEqual(response.data['new_password'], self.user_data('new_password'))
        self.assertEqual(response.status_code, 201)
        
        
    def test_user_can_reset_password_with_no_data(self):
        response = self.client.post(self.reset_password_url)
        self.assertEqual(response.status_code, 400)
        
        
    def test_reset_password_wrong_email(self):
        self.user_data = {"email": "wrong@email.com"}
        response = self.client.post(self.reset_password_url,self.user_data,format="json")
        self.assertEqual(response.status_code, status=status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(mail.outbox), 0)
        
    
    def test_reset_password_inactive_user(self):    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user_data = {"email": self.user_data["email"]}
        response = self.client.post(self.reset_password_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(mail.outbox), 1)