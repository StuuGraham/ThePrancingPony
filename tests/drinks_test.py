import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Gin and Tonic", 2.50, 3, 10)
        self.drink2 = Drink("Rum and Coke", 2.50, 2, 15)
        self.drink3 = Drink("Brandy", 4.00, 5, 8)

    def test_drink_name(self):
        self.assertEqual("Gin and Tonic", self.drink1.name)

    def test_drink_price(self):
        self.assertEqual(4.00, self.drink3.price)

    def test_alcohol_level(self):
        self.assertEqual(2, self.drink2.alcohol_level)