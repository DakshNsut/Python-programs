cases = int(input("Enter the number of test cases:- "))
list_case=[]
i = 1
for item in range(cases):
    if i>cases:
        break
    else:
        case = int(input(f"Enter the {i} case you want to find the next palindrome of:- "))
        list_case.append(case)
        i+=1
        continue

def next_palindrome(Index):
    end =list_case[Index]+10001
    for org in range(list_case[Index],end):
        org = str(org)
        new = org[::-1]
        if new == org:
            return f"Next palindrome after {list_case[Index]} is {org}."
        else:
            """ end+=1 Tried doing this using another func running here,
            but that showed maximum recursion depth exceeded for 10000000000000002."""
            continue

index=0
while index<len(list_case):
    obj = str(list_case[index])
    nobj = obj[::-1]
    if obj==nobj:
        print(f"{obj} is itself a palindrome.")
        index+=1
        continue
    else:
        if index < len(list_case):
            print(next_palindrome(index))
            index += 1
            continue
