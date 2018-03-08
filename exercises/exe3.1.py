# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#Program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.
num = int(input("Enter an integer: "))
pwr = 2
# pwr has been defined to 2 instead of 1 because num**1 always suffices the condition. 
root = 0
found = False
if num < 0:
    neg = True
else:
    neg = False
while pwr < 6:
    while abs(root**pwr) <= abs(num):
        if root**pwr == num:
            print(str(root) + "**" + str(pwr) + " = " + str(num))
            found = True
        if abs(root) > abs(num):
            root = 0
        elif neg:
            root -= 1
        else:
            root +=1
    pwr += 1
    root = 0
if not found:
    print("No pair of integers, 'root' and 'pwr', exists such that 0 < pwr < 6 and root**pwr = " + str(num))
