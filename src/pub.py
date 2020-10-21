class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_collection = []

    def serve_drink(self, drink):
        self.till += drink.price