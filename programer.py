from staff import Staff
from exam import Testexam

# Create Object
staff1 = Staff("kaweepong", "promsen")
print("Infomation sfaff")
print("Name {} {}".format(staff1.fname, staff1.lname))
print("Position " + staff1.position)

staff2 = Staff("Jonh", "Park")
print(staff2)

testExam1 = Testexam(50,60)
print(testExam1)

