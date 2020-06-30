class Staff:

  # Attributes
  fname = ""
  lname = ""
  position = ""
  sarary = 15000
  branch  = "chiang mai"

  # Methods
  # def __init__(self,fname, lname, position): 
  #   self.fname = fname
  #   self.lname = lname
  #   self.position = position

  # Overloading Method
  def __init__(self,fname= None, lname= None, position= "trianee"):
    self.fname = fname
    self.lname = lname
    self.position = position

  # Overriding Method
  def __str__(self):
    return "Name {} {}".format(self.fname, self.lname)

  # def __repr__(self):
    #Type 1
    # return "({!r},{!r},{!r},{})".format(self.fname, self.lname, self.position, self.sarary)
    #Type 2
    # return repr((self.fname, self.lname, self.position, self.sarary, self.branch))
    #Type 3
    # return "{} {}".format(self.__class__.__name__, repr((self.fname, self.lname, self.position, self.sarary, self.branch)))

  
