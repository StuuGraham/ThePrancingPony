class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_stock = []
        

    def serve_drink(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        if customer.age >= 30:
            return True
        else:
            return False

    def check_drunkenness(self, customer):
        if customer.drunkenness <= 20:
            return True
        else:
            return False

    def check_total_stock_level(self,drinks):
        total_stock_level = 0
        for drink in drinks:
           total_stock_level += drink.stock_level
        return total_stock_level


    def check_total_stock_price(self,drinks):
        total_stock_value = 0
        for drink in drinks:
            drink_stock_value = drink.stock_level * drink.price
            total_stock_value += drink_stock_value
        return total_stock_value

    def serve_food(self, food):
        self.till += food.price

