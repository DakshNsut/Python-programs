from random import randint
Num = int(input("Enter the number whose multiplication table you want:- "))
dict = dict()

def Rohan_func(num):
    Random = randint(1, 10)
    for i in range(11):
        if i==0:
            continue
        elif i!=Random:
            print(num*i)
            prod = num*i
            key = str(num)+"*"+str(i)
            dict[key]= prod
            continue
        elif i==Random:
            # printing a prime number would be easy to assume it wont be the correct product.
            print(17)
            prod = 17
            key = str(num) + "*" + str(i)
            dict[key] = prod
            continue
    return '\n'.join([])

Rohan_func(Num)
list_keys=[]

# Rohan's function has been given to find multiplication table of a given number
# Check any wrong value given by the function

def Checking_Fraud(num):
    for i in range(11):
        key = str(num) + "*" + str(i)
        if i==0:
            continue
        elif dict[key] == num*i:
            continue
        elif dict[key] != num*i:
            keys = dict.keys()
            for j in keys:
                list_keys.append(j)
                continue
            for j in list_keys:
                if j == key:
                    print(f"The index where the product is wrong is: {list_keys.index(j)}")
                    continue
                else:
                    continue
    return '\n'.join([])

Checking_Fraud(Num)