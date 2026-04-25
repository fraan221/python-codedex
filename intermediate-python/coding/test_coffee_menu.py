import unittest
from coffee_menu import CoffeeMenu


class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu = None

    def test_get_price_existing_item(self):
        price = self.menu.get_price("cappuccino")
        self.assertEqual(price, 3.20)

    def test_get_price_non_existing_item(self):
        price = self.menu.get_price("mocha")
        self.assertIsNone(price)

    def test_add_item(self):
        self.menu.add_item("ice latte", 3.05)
        self.assertEqual(self.menu.menu["ice latte"], 3.05)

    def test_remove_item(self):
        self.menu.delete_item("espresso")
        self.assertFalse("espresso" in self.menu.menu)

    def test_modify_price_existing_item(self):
        self.menu.modify_price("espresso", 3)
        self.assertEqual(self.menu.menu["espresso"], 3)

    def test_modify_price_non_existing_item(self):
        self.menu.modify_price("ice latte", 4)
        self.assertNotIn(4, self.menu.menu)


if __name__ == "__main__":
    unittest.main()
