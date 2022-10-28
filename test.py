#!/usr/bin/python

import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')

# Parent Class
class A(object):
    def __init__(self, n='Rahul'):
        self.name = n
 
 
class B(A):
    def __init__(self, roll):
        self.roll = roll

        A.__init__(self)
 
 
object = B(23)
print(object.name)
