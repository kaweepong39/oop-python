from datetime import date

class PersonV1:
  def __init__(self, title, fname, lname, titleth, fnameth, lnameth, bod):
    self.title = title
    self.fname = fname
    self.lname = lname
    self.titleth = titleth
    self.fnameth = fnameth
    self.lnameth = lnameth
    self.bod = str(bod)

  def __str__(self):
    return "{} {} {}\n{} {} {}\n{}".format(self.title, self.fname, self.lname, self.titleth, self.fnameth, self.lnameth, self.bod)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

class PersonName:
  def __init__(self, title, fname, lname):
    self.title = title
    self.fname = fname
    self.lname = lname

  def __str__(self):
    return "{} {} {}".format(self.title, self.fname, self.lname)

class PersonV2:
  def __init__(self, nameTh, nameEn, bod):
    self.nameTh = nameTh
    self.nameEn = nameEn
    self.bod = str(bod)

  def __str__(self):
    return "{} \n{} \n{}".format(self.nameTh, self.nameEn, self.bod)

person1 = PersonV1("Mr.", "AAAAA", "BBBBB", "นาย", "เอ", "บี", date(2020,1,1))
print(person1)
print("*"*40)
person2 = PersonV2(PersonName("นาย", "เอ", "บี"), PersonName("Mr.", "AAAAA", "BBBBB"), date(2020, 1, 1))
print(person2)
