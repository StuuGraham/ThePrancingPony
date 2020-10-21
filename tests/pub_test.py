import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_drinks_collection(self):
        self.pub.drinks_collection = ["Gin and Tonic", "Rum and Coke", "Brandy"]
        self.assertEqual(3, len(self.pub.drinks_collection))

    def test_serve_drink(self):
        drink = Drink("Brandy", 4.00, 5)
        self.pub.serve_drink(drink)
        self.assertEqual(104.00, self.pub.till)

    def test_check_age__true(self):
        customer = Customer("Frodo Baggins", 100.00, 50)
        self.pub.check_age(customer)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age__false(self):
        customer = Customer("Peregrin Took", 80.00, 28)
        self.pub.check_age(customer)
        self.assertEqual(False, self.pub.check_age(customer))