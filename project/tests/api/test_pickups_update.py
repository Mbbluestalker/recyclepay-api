from db.models import Category, Order, User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestCompleteOrder(APITestCase):
    def setUp(self):
        individual = {
            'username': 'customer',
            'password': 'customer',
            'first_name': 'Customer',
            'last_name': 'Customer',
            'email': 'test@mail.com',
            'is_verified': True,
            'is_individual': True,
            'is_collector': False,
        }

        self.individual = User.objects.create_user(**individual)

        collector = {
            'email': 'test2@mail.com',
            'password': 'test1234',
            'is_collector': True,
            'is_verified': True,
            'is_individual': False
        }

        self.collector = User.objects.create_user(**collector)
        self.collector_token = Token.objects.create(user=self.collector)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.collector_token.key)

        self.category = Category.objects.create(name='Paper')

        order = {
            'id': 10,
            'title': 'Paper',
            'category': self.category,
            'location': 'Lagos',
            'weight_in_kg': 0.0,
            'status': 'accepted',
            'requested_by': self.individual,
            'picked_by': self.collector
        }

        self.order = Order.objects.create(**order)

        self.order.save()

        self.pickups_update_url = reverse('pickups-update', kwargs={'id': 10})

    def test_order_not_found(self):
        order = {}
        res = self.client.put(self.pickups_update_url, order)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_to_get_single_product(self):
        res = self.client.get(self.pickups_update_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_to_check_for_a_non_existing_product(self):
        res = self.client.get(reverse('pickups-update', args=[15]))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_not_logged_in(self):
        self.client.force_authenticate(user=None, token=None)
        res = self.client.get(self.pickups_update_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_complete_order(self):
        order = {'weight_in_kg': 15}
        res = self.client.put(self.pickups_update_url, order)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
