print('*************Type Casting with Python Set method***************','\n')
# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
myset.add("d")
print(myset,'\n')

print('*************Check unique and  Immutable with Python Set***************','\n')
# Python program to demonstrate that
# a set cannot have duplicate values 
# and we cannot change its items

# a set cannot have duplicate values
try:
    myset = {"Geeks", "for", "Geeks"}
    print(myset)
    myset[1] = "Hello"
    print(myset)
except:
    print('Python sets cannot have a duplicate value and once it is created we cannot change its value','\n')

print('*************Heterogeneous Element with Python Set***************','\n')
# Python example demonstrate that a set
# can store heterogeneous elements
myset = {"Geeks", "for", 10, 52.7, True}
print(myset,'\n')

print('*************Adding elements to Python Sets***************','\n')
# A Python program to
# demonstrate adding elements
# in a set

# Creating a Set
people = {"Jay", "Idrish", "Archi"}

print("People:", end = " ")
print(people)

# This will add Daxit
# in the set
people.add("Daxit")

# Adding elements to the
# set using iterator
for i in range(1, 6):
	people.add(i)

print("\nSet after adding element:", end = " ")
print(people,'\n')

print('*************Union operation on Python Sets***************','\n')
# Python Program to
# demonstrate union of
# two sets

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|"
# operator
population = people|dracula

print("\nUnion using '|' operator")
print(population,'\n')

