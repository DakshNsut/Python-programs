h = "abcdefghijklmnopqrstuvwxyz"
a = h.__iter__()
h.__iter__().__next__() # does not change to 'a'
print(a.__next__())
x = next(a)
next(a)
next(a)
next(a)
print(next(a))
print(x)
print(a) # returns the address that the iterator is pointing