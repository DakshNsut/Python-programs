Numb_Apples = int(input("Enter the number of apples Harry Potter has got."))
mn = int(input("Enter the start limit of range"))
mx = int(input("Enter the end limit of range"))

if mn==mx:
    print("This is not range. Limits are equal.")
    if Numb_Apples%mn==0:
        print(f"{mn} is the divisor of {Numb_Apples}.")
    elif Numb_Apples%mn!=0:
        print(f"{mn} is not the divisor of {Numb_Apples}.")
elif mn!=mx:
    for i in range(mn,mx+1):
        if Numb_Apples%i==0:
            print(f"{i} is the divisor of {Numb_Apples}.")
            continue
        elif Numb_Apples%i!=0:
            print(f"{i} is not the divisor of {Numb_Apples}.")
            continue
