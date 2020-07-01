class Person: # Superclass
  def __init__(self, fname, lname):
    self.fname = fname.strip().title()
    self.lname = lname

  def __str__(self):
    # !r ใช้สำหรับนำ ''ครอบ string
    return "Name:{!r} {!r} ".format(self.fname, self.lname)

# สืบทอดมาจากคุณสมบัติมาจาก Person
# เรียกใช้งานคุณสมบัติจากแม่โดยใช้ Super()
class Student(Person): # Subclass
  def __init__(self, studentId, fname, lname):
    self.studentId = studentId
    super().__init__(fname, lname)

  def __str__(self):
    return "ID: {} \n{}".format(self.studentId, super().__str__())

  def info(self):
    return "Full name: {}".format(self.fname + " " + self.lname)

person1 = Person("kawee","prom")
print(person1)

person2 = Student("62988", "kawee", "prom")
print(person2.fname)
print(person2.info())
print(person2)
   