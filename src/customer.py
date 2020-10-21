class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

# We want the customer to buy a drink of their choice,
# have the price of that drink taken from customers
# wallet and added to the pub till.
    def buy_drink(self, drink):
        self.wallet -= drink.price

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    def rejuvenate(self, food):
        self.drunkenness -= food.rejuvenation_level

        
