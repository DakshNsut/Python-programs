# to show implementation of derived class in python

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        # self.classvar1 = "Instance var in class A"

class B(A):
    # classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        # self.classvar1 = "Instance var in class B"
        self.special = "Special"

        # invoking init of super class here
        # super().__init__()
        print(self.classvar1)

a = A()
b = B()