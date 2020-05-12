class Account:

    def __init__(self,name,balance):
        # initialise variables here
        self.name = name
        self.balance = balance

    # write methods here
    def balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def __str__(self):
        return self.name + ", balance: " + str(self.balance)
