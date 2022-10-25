#!/usr/bin/python

import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')

# Python Program to Update
# character of a String
 
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
 
# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2]
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

list2 = list(String2)
list2.pop(2);
String7 = ''.join(list2)
print(String)



#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)