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
    myset = {"hero", "for", "tata"}
    print(myset)
    myset[1] = "Hello"
    print(myset)
except:
    print('Python sets cannot have a duplicate value and once it is created we cannot change its value','\n')

print('*************Heterogeneous Element with Python Set***************','\n')
# Python example demonstrate that a set
# can store heterogeneous elements
myset = {"good", "for", 10, 52.7, True}
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

print('*************Using add() Method***************','\n')
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1,'\n')

print('*************Using update() Method***************','\n')
# Addition of elements to the Set
# using Update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1,'\n')

print('*************Accessing a Set in Python***************','\n')
# Creating a set
set1 = set(["abc", "For", "def"])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")

# Checking the element
# using in keyword
print("\n")
print("abc" in set1,'\n')

print('*************Removing Elements from the Set in Python***************','\n')
# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set  using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1,'\n')

print('*************Using clear() Method***************','\n')
#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)


# Removing all the elements from 
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1,'\n')

print('*************Frozen Sets in Python***************','\n')
# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset(),'\n')

print('*************Example: Implementing All Functions***************','\n')
def create_set():
    my_set = {1, 2, 3, 4, 5}
    print(my_set)


def add_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    print(my_set)


def remove_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.remove(3)
    print(my_set)


def clear_set():
    my_set = {1, 2, 3, 4, 5}
    my_set.clear()
    print(my_set)


def set_union():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    my_set = set1.union(set2)
    print(my_set)


def set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.intersection(set2)
    print(my_set)


def set_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.difference(set2)
    print(my_set)


def set_symmetric_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.symmetric_difference(set2)
    print(my_set)


def set_subset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    subset = set2.issubset(set1)
    print(subset)


def set_superset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    superset = set1.issuperset(set2)
    print(superset,'\n')


if __name__ == '__main__':
    create_set()
    add_element()
    remove_element()
    clear_set()
    set_union()
    set_intersection()
    set_difference()
    set_symmetric_difference()
    set_subset()
    set_superset()











