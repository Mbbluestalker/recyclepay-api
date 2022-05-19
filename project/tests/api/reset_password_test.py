from django.urls import reverse
from django.core import mail
from rest_framework import status
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
        result = self.client.post(
            self.reset_password_url, self.user_data, format="json")
        self.assertEqual(result.data['email'], self.user_data('email'))
        self.assertEqual(result.data['otp'], self.user_data('otp'))
        self.assertEqual(result.data['new_password'], self.user_data('new_password'))
        self.assertEqual(result.status_code, 201)
        
        
    def test_user_can_reset_password_with_no_data(self):
        result = self.client.post(self.reset_password_url)
        self.assertEqual(result.status_code, 400)
        
        
    def test_reset_password_wrong_email(self):
        self.user_data = {"email": "wrong@email.com"}
        response = self.client.post(self.reset_password_url,self.user_data,format="json")
        self.assertEqual(response.status_code, status=status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(mail.outbox), 0)




















# from django.core import mail
# from db.models.user_model import User
# from django.urls import reverse
# from faker import Faker
# from rest_framework import status
# from rest_framework.test import APITestCase


# class TestSetUp(APITestCase):

#     def setUp(self):
#         self.password_reset_url = reverse('reset-password')
#         self.passwrod_reset_confirm_url = reverse('reset-password-confirm')
#         self.fake = Faker()

#         self.user_data = {
#             'email': self.fake.email(),
#             'username': self.fake.email().split('@')[0],
#             'password': self.fake.email(),
#         }

#         return super().setUp()

#     def tearDown(self):
#         return super().tearDown()
    


# class PasswordResetTest(APITestCase):

#     send_reset_password_email_url = "/api/reset-password/"
#     confirm_reset_password_url = "/api/reset-password-confirm/"
#     complete_reset_password_url = "/api/reset-password-complete"
    
#     user_data = {
#         "email": "test@example.com", 
#         "username": "test_user", 
#         "password": "verysecret"
#     }
#     login_data = {
#         "email": "test@example.com", 
#         "password": "verysecret"
#     }

#     def test_reset_password(self):
#         response = self.client.post(self.register_url, self.user_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(len(mail.outbox), 1)
        
#         email_lines = mail.outbox[0].body.splitlines()
#         activation_link = [l for l in email_lines if "/activate/" in l][0]
#         uid, token = activation_link.split("/")[-2:]
        
#         data = {"uid": uid, "token": token}
#         response = self.client.post(self.activate_url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         data = {"email": self.user_data["email"]}
#         response = self.client.post(self.send_reset_password_email_url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         email_lines = mail.outbox[1].body.splitlines()
#         reset_link = [l for l in email_lines if "/reset_password/" in l][0]
#         uid, token = activation_link.split("/")[-2:]


#         data = {"uid": uid, "token": token, "new_password": "new_verysecret"}
#         response = self.client.post(self.confirm_reset_password_url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
#         response = self.client.post(self.login_url, self.login_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
#         login_data = dict(self.login_data)
#         login_data["password"] = "new_verysecret"
#         response = self.client.post(self.login_url, login_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        

#     def test_reset_password_inactive_user(self):
        
#         response = self.client.post(self.register_url, self.user_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
#         data = {"email": self.user_data["email"]}
#         response = self.client.post(self.send_reset_password_email_url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         self.assertEqual(len(mail.outbox), 1)
        

#     def test_reset_password_wrong_email(self):
#         data = {"email": "wrong@email.com"}
#         response = self.client.post(self.send_reset_password_email_url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
#         self.assertEqual(len(mail.outbox), 0)