import random

#list of items
list = ["rock","paper","scissors"]
x = random.choice(list)

y = input("Type in the object: ")
#final input
print(y+":"+x)