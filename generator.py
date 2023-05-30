# ------------------- Example 1 -------------------------
import time
def name_searching():
    special = ["Ajay","Abhinav","Jack","Joe"]
    time.sleep(5)

    while True:
        name = (yield)
        if name in special:
            print("You got a seat.")
        if name not in special:
            print("You didn't get a seat.")

a = name_searching() # generator object
print("The list is being read, please wait.")
next(a) # This is needed when something has to be sent later by user using a.send()
# It pushes the iterator to the first yield statement, then things happen in this order:
# 1. whatever value is to be given is yielded
# 2. the first yield statement waits for next command to send any value using a.send() or next(a)
# 3. When next a.send() happens the function takes the value sent and also sends the value from next yield
# 4. Repeats 1 to 3 until yield statements end
# next(a)- is similar to a.send(None), this is used when nothing (None) has to be sent and the generator sends some value
myname = input("Enter your good name :)")
a.send(myname) # this send is recieved by yield

# ------------------- Example 2 -------------------------
def math():
    for i in range(2):
        x = yield i
        print(x+i)

d = math()
next(d) # has to be done
try:
    d.send(8) # i=0
    d.send(9) # i=1
    d.send(8) # i=2
except StopIteration:
    # Stop Iteration error will occur when there are not more 'yield' statements but we are trying to send some value
    pass

# ------------------- Example 3 -------------------------
# A generator function
def simpleGeneratorFun():
    for i in range(3):
        print("Nothing")
    y = yield 1
    print(y)
    y = yield 2
    print(y)
    y = yield 3
    print(y)

# x is a generator object
x = simpleGeneratorFun()
x.send(None) # the first yield has returned some value but is not printed or is lost

# Iterating over the generator object using next
print(next(x))
print(x.send("Hello World"))
print(next(x)) # raises StopIteration error because no more yield statement are present

# ------------------- Example 4 -------------------------
import itertools
# generator compression
primofibo = (i for i in itertools.count() if i%2 == 0 and i%3 == 0)

# this range has to be given otherwise returns infinite number of values
for i,_ in zip(primofibo,range(10)):
    print(i)
