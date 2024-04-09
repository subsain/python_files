# *****Python Dictionary****** :-Dictionaries in Python is a data structure, used to store values in key:value format
Dict = {1: 'jaipur', 2: 'For', 3: 'touris'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'jaipur', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict,'\n')

print('****************Different Ways to Create a Python Dictionary******************\n')
Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'sikar', 2: 'For', 3: 'tourist'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'ajmer'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict,'\n')

print('****************Nested Dictionaries******************\n')
Dict = {1: '', 2: 'For',
		3: {'A': 'Welcome', 'B': 'To', 'C': 'jodhpur'}}
print(Dict,'\n')

print('****************Adding Elements to a Dictionary******************\n')
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'alwer'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'good'}}
print("\nAdding a Nested Key: ")
print(Dict,'\n')

print('****************Access a Value in Dictionary using get() in Python******************\n')
Dict = {1: 'nice', 'name': 'For', 3: 'life'}

print("Accessing a element using get:")
print(Dict.get(3),'\n')

print('****************Deleting Elements using ‘del’ Keyword******************\n')
Dict = {1: 'sikar', 'name': 'For', 3: 'ajay'}
print("Dictionary =")
print(Dict)
del(Dict[1]) 
print("Data after deletion Dictionary=")
print(Dict,'\n')

print('****************Multiple Dictionary Operations in Python******************\n')
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values(),'\n')

print('****************Check if a value exists in the dictionary using a loop ******************\n')
# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Test if element is dictionary value
# Using loops
res = False
for key in test_dict:
	if(test_dict[key] == 3):
		res = True
		break

# printing result
print("Is 3 present in dictionary : " + str(res),'\n')

print('**************** Using isinstance() function: ******************\n')
def check_dict_value_1(d, val):
	if isinstance(d, dict):
		return any(val == v for v in d.values())
	return False
my_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}, 'f': 5}
my_value = 4
result = check_dict_value_1(my_dict, my_value)
print(result,'\n')

print('**************** Delete items from dictionary while iterating: ******************\n')

# *******Method 2: Creating a List of Keys to delete
# Creating a dictionary
myDict = {1: 'eat', 2: 'For', 3: 'health'}

# Using a list comprehension to make a list of the keys to be deleted
# (keys having value in 3.)
delete = [key for key in myDict if key == 3]

# delete the key/s
for key in delete:
	del myDict[key]

# Modified Dictionary
print(myDict,'\n')

# ******Method 3: Or if you’re new to list comprehensions:
# Creating a dictionary
myDict = {1: 'walk', 2: 'For', 3: 'health'}

# create a list of keys to delete
delete = []
for key in myDict:
	if key == 3:
		delete.append(key)

for i in delete:
	del myDict[i]

# Modified Dictionary
print(myDict,'\n')

# ******Method 4: Using list(myDict) 
# Creating a dictionary
myDict = {1: 'tour', 2: 'For', 3: 'enjoy'}

# Iterating through the list of keys
for key in list(myDict):
	if key == 2:
		del myDict[key]

# Modified Dictionary
print(myDict)











