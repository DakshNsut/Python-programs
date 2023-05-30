rest = "Khana khazana"
list_calories = []
numb_food_items = int(input(f"How many food items you have in your {rest} restaraunt."))

i=1
while True:
    if i>numb_food_items:
        break
    else:
        cal = int(input(f"Enter the calorie of item{i}"))
        list_calories.append(cal)
        i+=1
        continue
list_calories.sort()
list_calories2 = list_calories[::-1]
print(f"1{list_calories2}")
list_calories3 =[]

n=len(list_calories)
while True:
    i = list_calories[n-1]
    list_calories3.append(i)
    n-=1
    if n-1<0:
        break
    else:
        continue
print(f"2{list_calories3}")
list_calories.reverse()
print(f"3{list_calories}")

if list_calories==list_calories2==list_calories3:
    print("All three methods of list reverse worked:)")
else:
    print("Some error occured check your code.")
