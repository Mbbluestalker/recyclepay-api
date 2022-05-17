from django.shortcuts import reverse
from rest_framework import test, status, exceptions

from db.models.user_model import User


class TestRegisterApi(test.APITestCase):
    def test_to_check_for_empty_parameters(self):
        response = self.client.post(reverse('api-register'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_to_check_for_incomplete_data(self):
        sample_data = {
            'email': 'me@mail.com',
            'password': 'pass',
            'first_name': 'Micah',
        }
        response = self.client.post(reverse('api-register'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,
                         {'message!': {'last_name':
                                           [exceptions.ErrorDetail(string='This field is required.',
                                                                   code='required')]}})

    def test_to_determine_if_user_is_created_after_registration(self):
        sample_data = {
            'email': 'me@mail.com',
            'password': 'pass',
            'first_name': 'Micah',
            'last_name': 'Tundra'
        }
        initial_user_count = User.objects.all().count()
        response = self.client.post(reverse('api-register'), sample_data)

        current_user_count = User.objects.all().count()
        current_user = User.objects.get(email=sample_data['email'])

        self.assertEqual(current_user_count, initial_user_count + 1)
        self.assertIsNotNone(current_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(current_user, User)
