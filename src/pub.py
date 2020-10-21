class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_collection = []

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