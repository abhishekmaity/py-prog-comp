# -*- coding: utf-8 -*-
"""
@author: Abhishek

#What would the code in Figure 3.4 (below) do if the statement x = 25 were replaced by x = -25?
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)


Answer: 
"""    
x = -25
if x<0:
    print('Roots are imaginary')
else:
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of', x)
