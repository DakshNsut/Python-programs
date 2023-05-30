import re
list_of_phone_numbers = "+1-202-555-0173 +1-202-555-0108  +44-1632-960493 +61-1900-654-321 +22 1234567899 +91 9910002216 +91 9911102212"
country_code = re.compile(r'[+][9][1] \d{10}')
matches1 = country_code.findall(list_of_phone_numbers)
print(matches1)

str = """Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com
And I am learning programming on code with harry youtube channel and I have one more
email:"deepak@dt.com"
and some more
email id:<dt@codewithharry.com>

email:"deepak@dt.com.in" and I have one more harrybhai@codewithharry.com."""

matches = re.findall(r'\w+[@]\S+\w',str)
print(matches)

n = 1
for i in matches:
    with open("B.txt","a") as f:
        f.write(f"Email{n}: ")
        f.write(i)
        if n == len(matches):
            break
        else:
            f.write("\n")
        n+=1
        continue