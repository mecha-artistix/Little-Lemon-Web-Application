from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Beef Pasta", Price=6.00, Inventory=99)
        expected_title = "Beef Pasta"
        expected_price = 6.00

        self.assertEqual(item.Title, expected_title)
        self.assertEqual(item.Price, expected_price)