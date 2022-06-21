from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from api.views import AcceptItemView
from db.models import Order, User, Category


class AcceptItemViewAPITestCase(APITestCase):

    def setUp(self):
        self.accept_item_url = reverse('accept_item', kwargs={'id': 1})

        '''Create Collector with id=1'''
        self.user = User.objects.create_user(
            username='collector',
            password='collectors_password',
            first_name='Adam',
            last_name='Peters',
            email='adampeters@gmail.com',
            phone=+2348036555600,
            is_verified=True,
            is_collector=True,
            is_individual = False
        )

        '''Create Individual customer with id=2'''
        self.user_customer = User.objects.create_user(
            username='individual',
            password='individuals_password',
            first_name='Justin',
            last_name='Bieber',
            email='justinbieber@gmail.com',
            phone=+2347036555600,
            is_verified=True,
            is_collector=False,
            is_individual = True
        )

        '''Set Collector Credentials'''
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        '''Create Record with pk=1 in Category'''
        category = Category.objects.create(name="PLASTIC")

        '''Create Order by Individual'''
        Order.objects.create(
            title = "request for pickup of plastics",
            location = "Ajah",
            weight_in_kg = 0,
            status = "pending",
            category = category,
            requested_by = self.user_customer,
            picked_by = None,
        )


    def test_get_accept_item_is_resolved(self):
        url = self.accept_item_url
        ConfirmItem=""
        self.assertEqual(resolve(url).func.view_class, AcceptItemView)
        self.assertNotEqual(resolve(url).func.view_class, ConfirmItem)

    def test_get_accept_item_not_authenticated_without_credentials(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.accept_item_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_get_accept_item_Customer_authenticated_with_credentials(self):
        self.client.force_authenticate(user=None, token=None)
        self.token = Token.objects.create(user=self.user_customer)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.accept_item_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
