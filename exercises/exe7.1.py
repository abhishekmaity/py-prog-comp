# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#Implement a function that meets the specification below. Use a try-except block
def sumDigits(s):
    '''
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
    '''
    result = 0
    try:
        for i in range(len(s)):
            if s[i].isdigit():
                result += int(s[i])
        return result
    except TypeError:
        print('Input is not a string !')
