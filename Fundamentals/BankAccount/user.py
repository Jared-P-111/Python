
class User:
  def __init__(self, first_name, last_name, email, age):
    #INSTANCE ATTRIBUTES
    self.first_name =  first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0

  def display_info(self):
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print("Is rewards member: ", self.is_rewards_member)
    print("Gold card points: ", self.gold_card_points)
    return self

  def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points += 200
    return self

  def spend_points(self, pointAmt):
    if self.gold_card_points - pointAmt >= 0:
      self.gold_card_points -= pointAmt
      return self

class BankAccount:
    def __init__(self, balance = 0, int_rate = .9):
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

sean = BankAccount()
mary = BankAccount()

sean.deposit(10)
sean.display_account_info()

sean.deposit(10)
sean.display_account_info()

sean.deposit(10)
sean.display_account_info()

sean.yield_interest().display_account_info()

mary.deposit(20)
mary.withdraw(2)
mary.withdraw(2)
mary.withdraw(2)
mary.withdraw(2)
mary.yield_interest().display_account_info()