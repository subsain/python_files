
# ***Create a Tuple With One Item
values : tuple[int | str, ...] = (1,2,4,"html")
print(values,'\n')

mytuple = ("python",)
print(type(mytuple))

#NOT a tuple
mytuple = ("java")
print(type(mytuple),'\n')

# ***Tuple Constructor in Python
tuple_constructor = tuple(("dsa", "developement", "deep learning"))
print(tuple_constructor,'\n')

# ***Immutable in Tuples?
mytuple = (1, 2, 3, 4, 5)

# tuples are indexed
print(mytuple[1])
print(mytuple[4])

# 
mytuple = (1, 2, 3, 4, 2, 3)
print(mytuple)
try:
    mytuple[1] = 100
    print(mytuple,'\n')
except:
    print('We can find items in a tuple since finding any item does not make changes in the tuple.','\n')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@ Different Operations Related to Tuples @@@@@@@@@@@@@@@@@@@@@@@@@@
'''
Concatenation
Nesting
Repetition
Slicing
Deleting
Finding the length
Multiple Data Types with tuples
Conversion of lists to tuples
Tuples in a Loop
'''
print('******************************Concatenation of Python Tuples***********************************','\n')

# Code for concatenating 2 tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'machine learning')

# Concatenating above two
print(tuple1 + tuple2,'\n')

print('******************************Nesting of Python Tuples***********************************','\n')
# Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'learing')

tuple3 = (tuple1, tuple2)
print(tuple3,'\n')

print('******************************Repetition Python Tuples***********************************','\n')
# Code to create a tuple with repetition
tuple3 = ('python',)*3
print(tuple3,'\n')

print('******************************Slicing Tuples in Python***********************************','\n')
# code to test slicing
tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4],'\n')

print('******************************Deleting a Tuple in Python***********************************','\n')
# Code for deleting a tuple
try:
    tuple3 = ( 0, 1)
    del tuple3
    print(tuple3,'\n')
except:
    print('The output will be in the form of error because after deleting the tuple, it will give a NameError.','\n')

print('******************************Finding the Length of a Python Tuple***********************************','\n')
# Code for printing the length of a tuple
tuple2 = ('python', 'developer')
print(len(tuple2),'\n')

print('******************************Multiple Data Types With Tuple***********************************','\n')
# tuple with different datatypes
tuple_obj = ("immutable",True,23)
print(tuple_obj,'\n')

print('**************************Converting a List to a Tuple***********************','\n')
# Code for converting a list and a string into a tuple
list1 = [0, 1, 2]

print(tuple(list1))

# string 'python'
print(tuple('python'),'\n')

print('**************************Tuples in a Loop***********************','\n')
# python code for creating tuples in a loop
tup = ('subhash',)

# Number of time loop runs
n = 5
for i in range(int(n)):
	tup = (tup,)
	print(tup,'\n')

print('**************************Create a List of Tuples in Python***********************','\n')
# list() and tuple() method.
# zip() method
# zip() and iter() method
# map() method
# List comprehension and tuple() method
# Using built-in functions
print('**************************Create a List of Tuples Using list() and tuple() methods***********************','\n')
# create tuples with college id and
# name and store in a list
data = [(1, 'sravan'), (2, 'ojaswi'), (3, 'bobby'),
		(4, 'rohith'), (5, 'gnanesh')]

# display data
print(data,'\n')

print('***********Create a List of Tuples Using zip() function****','\n')
# create two lists with college id and name
roll_no = [1, 2, 3, 4, 5]
name = ['sravan', 'ojaswi', 'bobby', 'rohith', 'gnanesh']

# zip the two lists using zip() function
data = list(zip(roll_no, name))

# display data
print(data,'\n')

print('******Create a List of Tuples Using Using zip() and iter() method************','\n')
# create a list with name
name = ['sravan', 'ojaswi', 'bobby', 'rohith', 'gnanesh']

# zip the two lists using iter() function
data = [x for x in zip(*[iter(name)])]

# display data
(data,'\n')

print('******Create a List of Tuples Using map() function************','\n')
# create a list with name
name = [['sravan'], ['ojaswi'], ['bobby'], 
		['rohith'], ['gnanesh']]

# create list of tuple using above 
# list using map function
data = list(map(tuple, name))

# display data
(data,'\n')

print('******Create a List of Tuples Using list comprehension and tuple() method************','\n')

# create a list with name
name = [['sravan'], ['ojaswi'], ['bobby'],
		['rohith'], ['gnanesh']]

# create list of tuple using above list
# using list comprehension and tuple() 
# method
data = [tuple(x) for x in name]

# display data
(data,'\n')

print('******Create a List of Tuples without using built-in functions************','\n')
# Function to create a list of tuples
def create_list_of_tuples(lst1, lst2):
	result = [] # Empty list to store the tuples
	for i in range(len(lst1)):
		# Create a tuple from corresponding elements
		tuple_element = (lst1[i], lst2[i])
		result.append(tuple_element) # Append the tuple to the list
	return result


# Example usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list_of_tuples = create_list_of_tuples(list1, list2)
print(list_of_tuples,'\n')

print('******Convert a List into a Tuple************','\n')
# program to convert a 
# list into a tuple
def convert(list):
	return tuple(list)

# Driver function
list = [1, 2, 3, 4]
print(convert(list),'\n')

print('******Convert a list into a  tuple Using list************','\n')

# program to convert a 
# list into a tuple
def convert(list):
	return (*list, )

# Driver function
list = [1, 2, 3, 4]
print(convert(list),'\n')

print('******Convert a list into a tuple without Using builtin function************','\n')
# Function to convert a list to a tuple
def convert_list_to_tuple(lst):
	tuple_result = () # Empty tuple to store the converted elements
	for element in lst:
		tuple_result += (element,) # Append each element to the tuple
	return tuple_result
# Example usage
my_list = [1, 2, 3, 4]
my_tuple = convert_list_to_tuple(my_list)
print(my_tuple,'\n')

print('******Using lists and tuple() method************','\n')
# Python3 code to demonstrate
# unzip a list of tuples

# Initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# Empty dictionary
res = []

a = []
b = []

for i in test_list:
	a.append(i[0])
	b.append(i[1])

res.append(tuple(a))
res.append(tuple(b))

# Printing modified list
print("Modified list is : " + str(res),'\n')

print('******Unpacking a Tuple in Python************','\n')
# Program to understand about 
# packing and unpacking in Python

# this lines PACKS values
# into variable a
a = ("MNNIT Allahabad", 5000, "Engineering") 

# this lines UNPACKS values
# of variable a
(college, student, type_ofcollege) = a 

# print college name
print(college)

# print no of student
print(student)

# print type of college
print(type_ofcollege,'\n')

print('******Unpacking a Tuple in Python************','\n')
# Python3 code to study about
# unpacking python tuple using *

# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

# print details
print(x)
print(y)
print(z)

# first and second will be assigned to x and y
# remaining will be assigned to z
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)
print(x)
print(y)
print(z,'\n')

print('******Unpacking a Tuple in Python************','\n')

# Python3 code to study about
# unpacking python tuple using function

# function takes normal arguments
# and multiply them
def result(x, y):
	return x * y
# function with normal variables
print (result(10, 100))

# A tuple is created
z = (10, 100)

# Tuple is passed
# function unpacked them

print (result(*z),'\n')

print('******Accessing nth element from tuples in list***********','\n')
# ***Method #1 : Using list comprehension
# Python3 code to demonstrate 
# get nth tuple element from list
# using list comprehension 

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list 
print ("The original list is : " + str(test_list))

# using list comprehension to get names
res = [lis[1] for lis in test_list]
	
# printing result
print ("List with only nth tuple element (i.e names) : " + str(res),'\n')

print('******Using a for loop***********','\n')
# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is:", test_list)

# using a for loop to access the nth element of each tuple
n = 1 # specify the index of the element to access
res = []
for tup in test_list:
	res.append(tup[n])

# printing result
print("List with only nth tuple element:", res,'\n')


































