import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Gin and Tonic", 2.50)
        self.drink2 = Drink("Rum and Coke", 2.50)
        self.drink3 = Drink("Brandy", 4.00)

    def test_drink_name(self):
        self.assertEqual("Gin and Tonic", self.drink1.name)
        