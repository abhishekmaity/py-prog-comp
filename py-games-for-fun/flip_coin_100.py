# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:06:54 2018

@author: Abhishek
"""

#Write a program that flips a coin 100 times and then tells you
#the number of heads and tails

import random

print("Let flip a coin 100 times.")
h=1
t=1

for i in range(1,100,1):
    r=random.randint(1,2)
    if r==1:
        h+=1
    else:
        t+=1
print("The number of tails occured is ",t)