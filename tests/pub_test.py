import unittest
from src.pub import Pub

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