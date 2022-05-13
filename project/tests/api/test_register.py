from django.shortcuts import reverse
from rest_framework import test, status


class TestRegisterApi(test.APITestCase):

    def test_to_check_for_empty_parameters(self):
        response = self.client.post(reverse('api-register'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
