
class User:
  def __init__(self, first_name, last_name, email, age):
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

  def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points += 200

  def spend_points(self, pointAmt):
    if self.gold_card_points - pointAmt >= 0:
      self.gold_card_points -= pointAmt



elvis = User('Elvis', 'Presley', "rip@outlook.com", "35")
elvis.enroll()
elvis.spend_points(20)

bigBird = User('Big', 'Bird', 'sesamestreet@bruh.com', "90")
bigBird.enroll()
bigBird.spend_points(80)

madonna = User('Mad', 'Onna', 'likeavirgin@nope.com', '65')

elvis.display_info()
bigBird.display_info()
madonna.display_info()