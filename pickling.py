# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte
# stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

# object hierarchy here is Python list

import requests
link = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(link).text

# file = "iris.txt"
# f1 = open(file,"w+")
# f1.write(data)

import pickle
data_items = data.split("\n")
# data_item = [element.split(",")  for element in data_items if len(element)!=0]

data_item = []
for element in data_items:
    if len(element)!=0:
        element = element.split(",")
        data_item.append(element)

file_pickle = "iris.pkl"
f2_a = open(file_pickle,"wb")
pickle.dump(data_item,f2_a)
f2_a.close()

f2_b = open(file_pickle,"rb")
DATA = pickle.load(f2_b)
print(DATA)
f2_b.close()