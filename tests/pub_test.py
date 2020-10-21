import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Gin and Tonic", 2.50, 3, 10)
        self.drink2 = Drink("Rum and Coke", 2.50, 2, 15)
        self.drink3 = Drink("Brandy", 4.00, 5, 8)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_drinks_collection(self):
        self.pub.drinks_stock = ["Gin and Tonic", "Rum and Coke", "Brandy"]
        self.assertEqual(3, len(self.pub.drinks_stock))

    def test_serve_drink(self):
        drink = Drink("Brandy", 4.00, 5, 8)
        self.pub.serve_drink(drink)
        self.assertEqual(104.00, self.pub.till)

    def test_check_age__true(self):
        customer = Customer("Frodo Baggins", 100.00, 50, 0)
        self.pub.check_age(customer)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age__false(self):
        customer = Customer("Peregrin Took", 80.00, 28, 0)
        self.pub.check_age(customer)
        self.assertEqual(False, self.pub.check_age(customer))

    def test_check_drunkenness__true(self):
        customer = Customer("Frodo Baggins", 100.00, 50, 0)
        self.pub.check_drunkenness(customer)
        self.assertEqual(True, self.pub.check_drunkenness(customer))

    def test_check_drunkenness__false(self):
        customer = Customer("Peregrin Took", 80.00, 28, 21)
        self.pub.check_drunkenness(customer)
        self.assertEqual(False, self.pub.check_drunkenness(customer))

    def test_check_stock_level(self):
        drink1 = Drink("Gin and Tonic", 2.50, 3, 10)
        self.assertEqual(10, drink1.stock_level)

    def test_check_total_stock_level(self):
       self.drinks_stock = [self.drink1, self.drink2, self.drink3]
       self.pub.check_total_stock_level(self.drinks_stock)
       self.assertEqual(33, self.pub.check_total_stock_level(self.drinks_stock))

    def test_check_total_stock_price(self):
       self.drinks_stock = [self.drink1, self.drink2, self.drink3]
       self.pub.check_total_stock_price(self.drinks_stock)
       self.assertEqual(94.50, self.pub.check_total_stock_price(self.drinks_stock))

    def test_serve_food(self):
        food = Food("Second Breakfast", 1.50, 2)
        self.pub.serve_food(food)
        self.assertEqual(101.50, self.pub.till)