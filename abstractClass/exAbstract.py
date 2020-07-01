from abc import ABC, abstractmethod # Abstract base class

# class abstract
class Member(ABC):
  def __init__(self, memderId, fname, lname):
    self.memderId = memderId
    self.fname = fname
    self.lname = lname

  def __str__(self):
    return "MEMBER: {} NAME: {}".format(self.memderId,self.fname + " " + self.lname)

  @abstractmethod
  def discount(self,money):
    pass
  
class Gold(Member): 
  def discount(self, money):
    self.money = money
    discount = self.money * .10
    return "{} Total:{} ฿. discount:{} ฿.".format(self.fname, self.money, discount)

class Silver(Member):
  def discount(self, money):
      self.money = money
      discount = self.money * .05
      return "{} Total:{} ฿. discount:{} ฿.".format(self.fname, self.money, discount)

# member1 = Member("582011", "A", "a")
# print(member1)

member2 = Gold("582011", "B", "b")
print(member2)
print(member2.discount(1000))

member3 = Silver("582011", "C", "c")
print(member3)
print(member3.discount(1000))
