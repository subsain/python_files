
# Example 1 : Accessing elements from a multi-dimensional list
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['jaipur', 'For'], ['tourist']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0],'\n')

print('****************Taking Input of a Python List******************\n')

# **Taking Input of a Python List**

# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst,'\n') 

print('*****************Adding Elements to a Python List*****************\n')

# ****Adding Elements to a Python List****
# Method 1: Using append() method

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(3)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(4, 6):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((6,7))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['jaipur', 'tourist']
List.append(List2)
print("\nList after Addition of a List: ")
print(List,'\n')

print('****************Using insert() method******************\n')

# ****Method 2: Using insert() method****

# Python program to demonstrate 
# Addition of elements in a List

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'jaipur')
print("\nList after performing Insert Operation: ")
print(List,'\n')

print('******************Using extend() method****************\n')

# ***Method 3: Using extend() method

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List,'\n')

print('****************Reversing a List******************\n')

# ****Reversing a List*****
# Method 1:  A list can be reversed by using the reverse() method in Python.
# Reversing a list
mylist = [1, 2, 3, 4, 5, 'hello', 'hi']
mylist.reverse()
print(mylist,'\n')

# Method 2: Using the reversed() function:
# Reversing a list
mylist = [1, 2, 3, 4, 5, 'hello', 'Python']
mylist.reverse()
print(mylist,'\n')

print('****************Removing Elements from the List******************\n')

# ****Removing Elements from the List****
# Method 1: Using remove() method
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
	List.remove(i)
print("\nList after Removing a range of elements: ")
print(List,'\n')

# Method 2: Using pop() method
List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List,'\n')

print('*****************Slicing of a List*****************\n')

# ****Slicing of a List****
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = ['N', 'O', 'P', 'Q', 'R', 'S',
		'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Initial List: ")
print(List)

# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

# Negative index List slicing

# Creating a List
List = ['A', 'B', 'C', 'D', 'E', 'F',
		'G', 'H', 'I', 'J', 'K', 'L', 'M']
print("Initial List: ")
print(List)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List,'\n')

print('******************List Comprehension****************\n')

# List Comprehension :- newList = [ expression(element) for element in oldList if condition ]

# Python program to demonstrate list
# comprehension in Python

# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square,'\n')

# using for loop
# for understanding, above generation is same as
print('using for loop')
odd_square = []

for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)

print(odd_square,'\n')







