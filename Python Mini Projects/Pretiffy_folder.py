# The program changes the name of files with user-input format into 1,2,3....
# files with name as a reserved word are not changed
# Names of other files not of the user-input format will be changed to upper-case
# format should be added with a '.' example- '.pdf'

import os
def change_path(n):
    os.chdir(n)

def Rename(oldname,newname):
    os.rename(oldname,newname)

list = []
def reserved_capitalize(A,file_words):
    for item1 in A :
        file_name = os.path.splitext(item1)[0]
        # ignore file named as any reserved word
        if file_name in file_words:
            continue
        else:
            ext = os.path.splitext(item1)[1]
            B = file_name.upper() + ext
            Rename(item1,B)
            list.append(B)
            continue

Path = input("Enter the path where you want to prettify the files.")
file = input("Enter the name of file which contains all reserved words.") # any file with name = a reserved word is not to be changed
format = input("Enter the file format which you want to list.") # changes name of all files of this format as 1,2,3.... in ascending order

is_path = os.path.exists(Path)

while True:
    if is_path != True :
        print("\nInvalid path... Please try again.")
        Path = input("Enter the path where you want to prettify the files.")
        is_path = os.path.exists(Path)
        continue
    else:
        change_path(Path)
        break

A = os.listdir() # to list names of all files
Open = open(file)
f = Open.read().split("\n")
Open.close()

file_path = os.path.join(Path,file)
is_file = os.path.isfile(file_path)

while True:
    if is_file == True:
        reserved_capitalize(A,f)
        break
    else:
        print("\nInvalid file name... Please try again.")
        file = input("\nEnter the name of file which contains all reserved words.")
        is_file = os.path.isfile(file_path)
        continue

for i in list:
    file_format = os.path.splitext(i)[1]
    if file_format == format:
        n = list.index(i)
        os.rename(i,f"{n+1}{file_format}")
        continue
    else:
        continue