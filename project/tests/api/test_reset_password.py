# from django.urls import reverse
# from django.core import mail
# from rest_framework import status, response
# from rest_framework.test import APITestCase
#
#
# class TestResetPassword(APITestCase):
#     def setUp(self):
#         self.reset_password_url = reverse('reset-password')
#         self.user_data={
#             'email': 'dummy@gmail.com',
#             'otp': 'otp',
#             'new_password': 'dummy123'
#         }
#
#     def test_user_can_reset_password(self):
#         response = self.client.post(self.reset_password_url, self.user_data, format="json")
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_can_reset_password_with_no_data(self):
#         response = self.client.post(self.reset_password_url)
#         self.assertEqual(response.status_code, 400)
#
#     def test_reset_password_wrong_email(self):
#         self.user_data = {"email": "wrong@email.com"}
#         response = self.client.post(self.reset_password_url, self.user_data, format="json")
#         self.assertEqual(response.status_code, status=status.HTTP_400_BAD_REQUEST)

# To be refactored by the dev in charge.