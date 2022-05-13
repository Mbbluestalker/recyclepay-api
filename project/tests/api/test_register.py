from django.shortcuts import reverse
from rest_framework import test, status

from db.models.user_model import User


class TestRegisterApi(test.APITestCase):

    def test_to_check_for_empty_parameters(self):
        response = self.client.post(reverse('api-register'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_to_determine_if_user_is_created_after_registration(self):
        sample_data = {
            'email': 'me@mail.com',
            'username': 'me',
            'password': 'pass',
            'first_name': 'Micah',
            'last_name': 'Tundra'
        }
        initial_user_count = User.objects.all().count()
        self.assertEqual(initial_user_count, 1)
