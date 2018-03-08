# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#What is the decimal equivalent of the binary number 10011?
decimal=0
c=1
for a in '10011':
    decimal+=int(a)*(2**(5-c))
    c+=1
print(decimal)
