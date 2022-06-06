import pdb
from django.urls import reverse
from rest_framework.test import APITestCase
from db.models import User, Category
from rest_framework.authtoken.models import Token


class TestPickupRestTest(APITestCase):

    def setUp(self):
        self.pickup_request_url = reverse('pickup_request')
        
        self.category = Category.objects.create(name='Plastic')
        
        self.user = User.objects.create(
            username = 'username',
            first_name = 'john',
            last_name = 'doe',
            email ="johndoe@example.com",
            phone = "0812345678",
            location = "east-west",
            otp ="654321"
        )

        self.user.is_verified = True
        self.user.is_individual = True

        self.user_token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

    def test_user_is_authenticated(self):
        """
            test to check that user requesting pickup is authenticated
        """
        self.assertTrue(self.user.is_authenticated)

    def test_user_cannot_request_pickup(self):
        """
            test to check that authenticated users cannot request for pick up
            without providing title, category and location
        """
        res = self.client.post(self.pickup_request_url)
        self.assertEqual(res.status_code, 403)

    def test_user_can_request_pickup(self):
        """
            test to check that authenticated users can successfully request for pick up
        """
        payload = {
            'title':'plastic waste',
            'category': 'Plastic',
            'location': 'Ebute-meta'
        }
        res = self.client.post(self.pickup_request_url, payload, format='json')
        self.assertEqual(res.status_code, 403)
