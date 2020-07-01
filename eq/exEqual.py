class Student:
  def __init__(self, fname, score):
    self.fname = fname
    self.score = score

  def __str__(self):
    return "{}, score = {}".format(self.fname, self.score)

  # การเปรียบเทียบแค่ค่า score
  def __eq__(self, other):
    return self.score == other.score

s1 = Student("Peter", 75)
s2 = Student("Taylor", 75)
s3 = Student("Taylor", 75)
s4 = Student("Art", 80)
print(s1 == s2)
print(s2 == s3)
print(s1 == s4)
print(s1.__eq__(s4))  # มีค่าเท่ากับ s1 == s4

