class A:
    def __init__(self):
        self.a = "1"

    @property
    def func(self):
        return f"Hello {self.a}"

    @func.setter
    def func(self,string):
        self.a += string

b = A()
b.func = "2"
print(b.func)