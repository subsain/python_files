# Python3 program introducing f-string
val = 'Big'
print(f" if you think {val} then you become a {val} and this is a success factor of  {val}.",'\n')

print('**************************')

name = 'Rajesh'
age = 20
print(f"Hello, My name is {name} and I'm {age} years old.",'\n')

print('**************************')

# we can use this method for getting date of today
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}",'\n')

print('**************************')

val = { 'Id': 112,'Name': 'Harsh'}
print(f"Id of {val['Name']} is {val['Id']}",'\n')

print('***************************')
