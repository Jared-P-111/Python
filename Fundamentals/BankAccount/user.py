
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
    return self

  def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points += 200
    return self

  def spend_points(self, pointAmt):
    if self.gold_card_points - pointAmt >= 0:
      self.gold_card_points -= pointAmt
      return self



elvis = User('Elvis', 'Presley', "rip@outlook.com", "35").enroll().spend_points(20).display_info()

bigBird = User('Big', 'Bird', 'sesamestreet@bruh.com', "90").enroll().spend_points(80).display_info()

madonna = User('Mad', 'Onna', 'likeavirgin@nope.com', '65').display_info()

