from math import *

def GetPrimesInRange(range):
    primes = []
    for i in range:
        if (IsPrime(i)):
            primes.append(i)

    return primes 

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

def IntSqrt(n): #Root Square of Integer, -1 if not Integer result
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    if (x*x == n):
        return x
    else:
        return -1


fibonacciArray = [1,1,2,3]
def Fibonacci(n): 
    nMinusOne = n-1
    if (nMinusOne < len(fibonacciArray)):
        return fibonacciArray[nMinusOne]

    fibonacciArray.append(Fibonacci(nMinusOne) + Fibonacci(nMinusOne-1))
    return fibonacciArray[nMinusOne]

def TriangleNumber(n):
    res = (n * (n + 1)) / 2
    return res

def PentagonNumber(n):
    res = (n * (3*n - 1)) / 2
    return res

def HexagonNumber(n):
    res = n * ((2 * n) - 1)
    return res

def Factor(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + Factor(n//q) or [n]


#EXPERIMENTAL

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
