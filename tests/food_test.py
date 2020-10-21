import unittest
from src.customer import Customer
from src.drinks import Drink
from src.pub import Pub
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food1 = Food("Lembas Bread", 3.50, 5)
        self.food2 = Food("Stew", 2.50, 3)
        self.food3 = Food("Second Breakfast", 1.50, 2)

    def test_food_name(self):
        self.assertEqual("Lembas Bread", self.food1.name)

    def test_food_price(self):
        self.assertEqual(1.50, self.food3.price)

    def test_rejuvenation_level(self):
        self.assertEqual(3, self.food2.rejuvenation_level)
