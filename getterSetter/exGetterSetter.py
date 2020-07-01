# Java style
class Person:
  def __init__(self, fname, lname, position):
    self.fname = fname
    self.lname = lname
    self.setPosition(position)

  def __str__(self):
    return "Name:{} {} position:{}".format(self.fname, self.lname, self.__position)
    
  def getPosition(self):
    return self.__position

  def setPosition(self, position):
    self.__position = position

person1 = Person("Kaweepong", "Promsen", "programer")
print(person1)
print(person1.__dict__)
print("Position: {}".format(person1._Person__position))

# ///////////////////////////////////////////////////////////////////////////////////////////////////

# Pythonic style
# class Person:
#   def __init__(self, fname, lname, position):
#     self.fname = fname
#     self.lname = lname
#     self.position = position

#   def __str__(self):
#     return "Name:{} {} position:{}".format(self.fname, self.lname, self.position)

#   @property # getter
#   def position(self):
#     return self.__position

#   # position คือชื่อ property/Attribute
#   @position.setter  # setter
#   def position(self, position):
#     self.__position = position

# person1= Person("kaweepong", "Promsen", "programer")
# person1.position = "SA"
# print(person1) 
# fullName = person1.fname + " " + person1.lname
# print("Full name: {} ".format(fullName))
# print("Position: {}".format(person1.position))
