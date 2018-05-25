from math import *
from ArrayHelpers import AreSortedArraysDisjointed, MultiplyArrayValues, SumArrayValues, Permute, Combination

primesCache = [2, 3, 5]
def GetPrimesUpTo(value):
    global primesCache
    lastValInCache = primesCache[-1]
    if (value < lastValInCache):
        i = 0
        while (value < primesCache[i]):
            i += 1
        return primesCache[:i+1]
    else:
        primes = GetPrimesInRange(range(lastValInCache+1, value))
        primesCache += primes
        return primesCache

def GetPrimesInRange(range):
    primes = []
    for i in range:
        if (IsPrime(i)):
            primes.append(i)
    return primes 

#divisorsArrayCache = {}
#def GetDivisorsSortedArray(value):
#    if (not divisorsArrayCache.has_key(value)):
#        arr = []
#        for divisor in range(2,(value/2)+1):
#            if (value % divisor == 0):
#                arr.append(divisor)
#        arr.append(value)

#        divisorsArrayCache[value] = arr

#    return divisorsArrayCache[value]


#divisorsSetsCache = {}
#def GetDivisorsSet(value):
#    if (not divisorsSetsCache.has_key(value)):
#        divSet = set()
#        for divisor in range(2,(value/2)+1):
#            if (value % divisor == 0):
#                divSet.add(divisor)
#        divSet.add(value)

#        divisorsSetsCache[value] = divSet

#    return divisorsSetsCache[value]


def GetUniquePrimeFactors(value):
    resultSet = set()
    loopLimit = value**0.5
    n = 2
    while (value != 1):
        if (n > loopLimit):
            n = value
        if (value % n == 0):
            value /= n
            resultSet.add(n)  
        else:
            n += 1
    return list(resultSet)


def Factorate(value):
    resultArray = []
    loopLimit = value**0.5
    n = 2
    while (value != 1):
        if (n > loopLimit):
            n = value
        if (value % n == 0):
            value /= n
            resultArray.append(n)
        else:
            n += 1
    return resultArray

def GetDivisors(value):
    factors = Factorate(value)
    factorsCombinations = Combination(factors)
    divisors = set()
    for comb in factorsCombinations:
        mul = MultiplyArrayValues(comb)
        divisors.add(mul)
    return divisors


divisorsSetsCache = {}
def GetDivisorsUsingCache(value):
    if (not divisorsSetsCache.has_key(value)):
        divSet = GetDivisors(value)
        divisorsSetsCache[value] = divSet
    return divisorsSetsCache[value]


def IsPrime(value):
    if (value < 2):
        return False

    limit = int(sqrt(value) + 1)+1
    for divisor in range(2,limit):
        if (value != divisor) and (value % divisor == 0):
            return False
    return True

def Factorial(num):
    return factorial(num)

def C(n,r):
    return Factorial(n)/(Factorial(r) * Factorial(n-r))




def IsSquare(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

def GetClosestIntegerSquareRoot(n):
    srn = sqrt(n)
    minor = long(floor(srn))
    major = long(ceil(srn))
    diffMinor = abs(n - minor*minor)
    diffMajor = abs(n - major*major)
    if (diffMinor < diffMajor):
        return minor
    else:
        return major





def GetSmallerRelativePrimes(value):
    valueDivs = GetDivisorsUsingCache(value)
    nArr = [1]
    for n in range(2, value):
        nDivs = GetDivisorsUsingCache(n)
        if (AreSortedArraysDisjointed(nDivs,valueDivs)):
            nArr.append(n)        
    return nArr

def GetNumberOfSmallerRelativePrimes(value):
    valueDivs = GetDivisorsUsingCache(value)
    counter = 1
    for n in range(2, value):
        nDivs = GetDivisorsUsingCache(n)
        if (AreSortedArraysDisjointed(nDivs,valueDivs)):
            counter += 1       
    return counter

def GetNumberOfSmallerRelativePrimes2(value):
    return len(GetSmallerRelativePrimes2(value))

def GetSmallerRelativePrimes2(value):
    nSet = set()
    factors = Factorate(value)
    primes = GetPrimesUpTo(value/2 + 1)

    for f in factors:
        primesRepeat = [0] * len(primes)
        GetSmallerRelativePrimes2PrimeRecursion(nSet, f, primes, primesRepeat, value)

    relativePrimesSet = set(range(1,value)) - nSet

    return  relativePrimesSet



def GetSmallerRelativePrimes2PrimeRecursion(nSet, value, primes, repeat, limit):
    n = value
    for i in range(len(primes)):
        n *= primes[i] ** repeat[i]

    if (n > limit):
        return

    nSet.add(n)

    for i in range(len(primes)):
        newRepeat = repeat[:]
        newRepeat[i] += 1
        GetSmallerRelativePrimes2PrimeRecursion(nSet, value, primes, newRepeat, limit)



def IntSqrt(n): #Root Square of Integer, -1 if not Integer result
    x = SmallerIntSqrt(n)
    if (x*x == n):
        return x
    else:
        return -1

def SmallerIntSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x






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

def SquareNumber(n):
    res = (n * n) 
    return res

def PentagonalNumber(n):
    res = (n * (3*n - 1)) / 2
    return res

def HexagonalNumber(n):
    res = n * ((2 * n) - 1)
    return res

def HeptagonalNumber(n):
    res = n * ((5 * n) - 3) / 2
    return res

def OctagonalNumber(n):
    res = n * ((3 * n) - 2)
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


def SimplifyFraction(n,d):
    i = 2
    while(i <= n):
        if (n % i == 0 and d % i == 0):
            n /= i
            d /= i
        else:
            i += 1     

    return (n,d)




def CanSimplifyFraction(n,d):
    i = 2
    while(i <= n):
        if (n % i == 0 and d % i == 0):
            return True
        i += 1     

    return False

def CanSimplifyFractionWithPrimes(n, d, primes):
    for p in primes:
        if (n % p == 0 and d % p == 0):
            return True  

        if (p > n):
            return False       

    return False




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
