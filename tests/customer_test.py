import unittest
from src.customer import Customer
from src.drinks import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("Peregrin Took", 80.00, 28, 0)
        self.customer2 = Customer("Meriadoc Brandybuck", 50.00, 36, 0)
        self.customer3 = Customer("Frodo Baggins", 100.00, 50, 0)
        self.customer4 = Customer("Samwise Gamgee", 60.00, 38, 0)

    def test_customer_name(self):
        self.assertEqual("Peregrin Took", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer3.wallet)

    def test_buy_drink(self):
        drink = Drink("Brandy", 4.00, 5)
        self.customer2.buy_drink(drink)
        self.assertEqual(46.00, self.customer2.wallet)

    def test_drunkenness_level(self):
        self.assertEqual(0, self.customer1.drunkenness)

    def test_increase_drunkenness(self):
        drink = Drink("Gin and Tonic", 2.50, 3)
        self.customer3.increase_drunkenness(drink)
        self.assertEqual(3, self.customer3.drunkenness)