class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deduct_money(self, amount):
        self.balance -= amount
        return True