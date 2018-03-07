# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#Program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect
print('Enter 10 integers: ')
c = 1
temp = 0
while c<=10:
    n = int(input('Enter the number :'))
    if n%2!=0:
        if n>temp:
            temp=n
    c=c+1
if temp==0:
    print('None is a odd number')
else:
    print('The largest odd is',temp)
