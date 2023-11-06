from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializers

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(Title='Burger', Price=9.99, Inventory=50)
        self.menu2 = Menu.objects.create(Title='Pizza', Price=12.99, Inventory=30)
        self.menu3 = Menu.objects.create(Title='Salad', Price=7.99, Inventory=20)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuSerializers(Menu.objects.all(), many=True).data

        self.assertEqual(response.data, expected_data)