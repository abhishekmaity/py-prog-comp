# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
#When the implementation of fib in Figure 4.7 (below) is used to compute fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)
def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        
testFib(5)        