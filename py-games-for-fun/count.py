# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:50:22 2018

@author: Abhishek

Program that counts for the user. Let the user enter the
starting number, the ending number, and the amount by which to count

"""

start=int(input("Enter starting number :"))
end=int(input("Enter ending number :"))
count=int(input("Enter amount by which to count :"))
for i in range(start,end,count):
    print(i)

