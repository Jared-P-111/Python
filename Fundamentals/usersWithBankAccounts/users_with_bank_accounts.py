class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    def display_deposit(self):
        print(self.account.display_account_info())
        return self

class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print("Balance: " + str(self.balance))
    def yield_interest(self):
        self.balance *= self.int_rate
        return self


steve = User("Steve", "surferdude22@yahoo.com")
steve.make_deposit(20).display_deposit()