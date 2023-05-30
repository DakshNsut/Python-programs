class Student:
    leaves = 11
    @classmethod
    def updateLeaves(cls,newleaves):
        cls.leaves = newleaves

rohan = Student()
harry = Student()
# Automatically creates name variable

rohan.name = "Rohan"
harry.name = "Harry"
Student.leaves = 8
rohan.leaves = 9
harry.leaves = 12
print(f"{rohan.__dict__}  {harry.__dict__}")

rohan.updateLeaves(8)
# this function should change the value of rohan.leaves to 8,
# but it did'nt because it is a classmethod and only class in allowed to use this method, not instance
print(harry.leaves)
print(rohan.leaves)
print(Student.leaves)