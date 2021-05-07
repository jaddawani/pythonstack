class BankAccount:

    def __init__(self, intrest_rate, balnance=0):
        self.intrest_rate = intrest_rate
        self.balance = balnance

    def deposite(self,amount):
        self.balance = self.balance+amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount

    def display_account(self):
        print("Account Balance: {}".format(self.balance))
        print(f"Interest Rate is: {self.intrest_rate*100}%")

    def yield_interest(self):
        self.balance = self.balance + self.balance*self.intrest_rate






