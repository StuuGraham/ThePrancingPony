import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("Peregrin Took", 80.00)
        self.customer2 = Customer("Meriadoc Brandybuck", 50.00)
        self.customer3 = Customer("Frodo Baggins", 100.00)
        self.customer4 = Customer("Samwise Gamgee", 60.00)

    def test_customer_name(self):
        self.assertEqual("Peregrin Took", self.customer1.name)