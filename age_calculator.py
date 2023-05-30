Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:) ")

while "-" in Age_DOB:
    DOB_list = Age_DOB.split("-")
    if int(DOB_list[2]) < 1903:
        print("Did you write your name in Guinness book of world records? Try again.")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:) ")
        continue
    elif int(DOB_list[2]) > 2021:
        print("You are not yet born. Kindly check input and try again.")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:) ")
        continue
    elif int(DOB_list[0]) > 30 and int(DOB_list[1]) > 6 and int(DOB_list[1]) <= 12 and int(DOB_list[2]) >= 2021:
        print("You are not yet born. Kindly check input and try again.")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:) ")
        continue
    elif int(DOB_list[2]) + 100<2021:
        print(f"You already turned 100 years old in {int(DOB_list[2]) + 100}")
        break
    elif len(DOB_list) == 3:
        print(f"You will turn 100 years old in {int(DOB_list[2]) + 100}")
        break
    else:
        print("Invalid DOB input. Check the format and your input and try again.")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:)")
        continue

while "-" not in Age_DOB:
    # DOB_YEAR = 2021-int(Age_DOB)
    if int(Age_DOB) > 118:
        print("You seem to be the oldest person alive. Check your Age and try again")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:)")
        continue
    elif int(Age_DOB)<=100:
        print(f"You will turn 100 years old in {2021-int(Age_DOB)+100} .")
        break
    elif int(Age_DOB)>100:
        print(f"You were 100 years old in {2021-int(Age_DOB)+100}.")
    else:
        print("Invalid input. Please try again.")
        Age_DOB = input("Enter your Age or DOB in DD-MM-YYYY format:) ")
        continue

Input_Year = input("Enter any random year and i will tell your age in that year.(**THIS IS OPTIONAL)")
while True:
    if len(Input_Year) == 0:
        break
    elif "-" in Age_DOB:
        DOB_list = Age_DOB.split("-")
        if int(Input_Year)>=2021:
            print(f"Your age in {Input_Year} will be {int(Input_Year)-int(DOB_list[2])}")
            break
        elif int(Input_Year) < 2021 and int(Input_Year)>int(DOB_list[2]):
            print(f"Your age in {Input_Year} was {int(Input_Year) - int(DOB_list[2])}")
            break
        elif int(Input_Year)<int(DOB_list[2]):
            print("You were not even born at that time.")
            break
        else:
            print("Invalid Year input. Please try again.")
            Input_Year = input("Enter any random year and i will tell your age in that year.(**THIS IS OPTIONAL)")
            continue

    elif "-" not in Age_DOB:
        # DOB_YEAR = 2021-int(Age_DOB)
        if int(Input_Year)>=2021:
            print(f"Your age in {Input_Year} will be {int(Age_DOB)+int(Input_Year)-2021}")
            break
        elif int(Input_Year) < 2021 and int(Input_Year)<2021-int(Age_DOB):
            print("You were not even born at that time.")
            break
        elif int(Age_DOB)+int(Input_Year)-2021<0 and int(Input_Year)>2021-int(Age_DOB):
            print(f"Your age in {Input_Year} was {int(Age_DOB)+int(Input_Year)-2021-(2021 - int(Input_Year))}")
            break
        else:
            print("Invalid Year input. Please try again.")
            Input_Year = input("Enter any random year and i will tell your age in that year.(**THIS IS OPTIONAL)")
            continue
    else:
        print("Invalid input. Please try again.")
        Input_Year = input("Enter any random year and i will tell your age in that year.(**THIS IS OPTIONAL)")
        continue
