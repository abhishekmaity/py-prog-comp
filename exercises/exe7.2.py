# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#Implement a function that satisfies the specification
def isEven(l):
   '''
   Assumes l is a list of integars
   returns the first even number in list
   raises an exception if no even number in list
   '''
   for i in l: 
       if i % 2 == 0: 
           return i 
   raise ValueError("No even numbers in list!")