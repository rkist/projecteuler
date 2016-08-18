from math import *

def GetDivisorsArray(value):
    arr = []
    for divisor in range(2,int(sqrt(value) + 1)+1):
        if (value != divisor) and (value % divisor == 0):
            arr.append(divisor)
    return arr

def IsPrime(value):
    if (value < 2):
        return False
    for divisor in range(2,int(sqrt(value) + 1)+1):
        if (value != divisor) and (value % divisor == 0):
            return False
    return True

def Factorial(num):
    return factorial(num)


fibonacciArray = [1,1,2,3]
def Fibonacci(n): 
    nMinusOne = n-1
    if (nMinusOne < len(fibonacciArray)):
        return fibonacciArray[nMinusOne]

    fibonacciArray.append(Fibonacci(nMinusOne) + Fibonacci(nMinusOne-1))
    return fibonacciArray[nMinusOne]




#EXPERIMENTAL
def Factor(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + Factor(n//q) or [n]

def IsPrimeEXP(n):
    if (n < 2):
        return False
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q > maxq 
