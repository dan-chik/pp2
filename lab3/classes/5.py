class Account:
    def __init__(self):
        #self.owner = owner
        self.balance = 0

    def deposit(self):
        amount = float(input())
        self.balance += amount

    def withdraw(self):
        amount = float(input())
        if self.balance >= amount:
            self.balance -= amount
            print("good")
        else: print(oh, no)

d1 = Account()
d1.deposit()
d1.withdraw()

