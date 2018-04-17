# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:56:29 2018

@author: Abhishek

Create a program that gets a message from the user and then
prints it out backwards.
"""
s=input("Enter a string:")
n=""
for i in range(len(s)-1,-1,-1):
    n+=s[i]
print(n)
