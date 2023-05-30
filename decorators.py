class A:
    def __init__(self,fname,lname,):
        self.fname = fname
        self.lname = lname
        self.special = "This is a special string"

    @property
    def email(self):
       return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,newemail):
        name=newemail.split("@") [0]
        newfname=name.split(".") [0]
        newlname=name.split(".") [1]
        self.fname = newfname
        self.lname = newlname
        self.special = 1234
        self.special = "Good string"

a=A("Abhinav","Arora")
print(a.email)
print(a.special)
a.fname="Gaurav"
print(a.fname)
print(a.email)
a.email="Gaurav.Taneja"
print(a.email)
print(a.special)