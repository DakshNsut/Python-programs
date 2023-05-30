class Employee:
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    @classmethod
    def fromm(cls,string):
        return cls(*string.split("-"))
#This shows that class argument is not a keyword
# but it's name can be any user-defined named

karan = Employee.fromm("Karan-480-Student")
print(karan.salary)