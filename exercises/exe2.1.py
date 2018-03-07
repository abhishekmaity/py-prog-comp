# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#Program that examines three variables—x, y, and z—and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.
x = int(input('Enter a number x: '))
y = int(input('Enter a number y: '))
z = int(input('Enter a number z: '))
if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x>y and x>z:
        print('x is the largest odd')
    elif y>x  and y>z:
        print('y is the largest odd')
    else:
        print('z is the largest odd')
else:
    print('One of the numbers is not odd')
