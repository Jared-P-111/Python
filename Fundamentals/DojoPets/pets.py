#class
class Ninja:
  #constructor
  def __init__(self, first_name, last_name, pet, treats, pet_food):
    #class attributes
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food
    self.pet = pet

  def feed(self):
    self.pet.eat()
    return self

  def walk(self):
    self.pet.play()
    return self



class Pet:
  def __init__(self, name, type, tricks, health, energy, sound):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy
    self.sound = sound

  def printInfo(self):
    print(self.name, self.type, self.tricks, self.health, self.energy)


  def play(self):
    self.health += 5
    print(self.health)
    return self

  def eat(self):
    self.energy += 5
    self.health += 10
    self.printInfo()
    return self

  def sleep(self):
    self.energy += 25
    self.printInfo()
    return self

  def noise(self):
    print(self.sound)
    return self


bubble = Pet("bubble", "cat", "bite", 80, 100, "meow")
mark = Ninja("mark", "smith", bubble, "cheese", "dry")













