from Bankaccount import BankAccount

class User:

    def __init__(self,name,intrest_rate,balance):
        self.name = name
        self.account = BankAccount(intrest_rate, balance)

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def displayinfo(self):
        print(f"User name is: {self.name}")
        print(f"Account balance: {self.account.balance}$")
        print(f"Account Intrest Rate: {self.account.intrest_rate}$")

    def deposite(self,amount):
        self.account.deposite(amount)


user1 = User("Jad",.02,5000)
user1.displayinfo()


