class Student:
  num_student = 0
  def __init__(self, fname, lname, w_kg, h_cm):
    self.fname = fname
    self.lname = lname
    self.w_kg = w_kg
    self.h_cm = h_cm

  def __str__(self):
    return "{} Kg.({:.2f} P.) {} Cm.({:.2f} Inc.)".format(self.w_kg, self.kg_pound(self.w_kg), self.h_cm, Student.cm_inch(self.h_cm))

  @property
  def bmi(self): # instance methon
    return self.w_kg / (self.h_cm / 100) **2

  @staticmethod
  def kg_pound(kg):
    return kg * 2.20462

  @staticmethod
  def cm_inch(cm):
    return cm * .393701

  @staticmethod
  def show_id(id):
    Student.num_student = id
    return Student.num_student 

s = Student("KK","PPPP", 50, 165)
print(s.bmi)
print(Student.kg_pound(50))
print(Student.cm_inch(165))
print(s)
print(Student.show_id(10))

