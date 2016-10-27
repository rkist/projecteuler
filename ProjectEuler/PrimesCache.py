from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *

    

def CachePrimesUpTo(maxNum, filePath = 'cache/primes.txt'):
    with open(filePath, 'w') as f:
        for i in xrange(maxNum):
            if (IsPrime(i)):
                f.write(str(i) + ' ')

def LoadCachePrimes(filePath = 'cache/primes.txt'):
    inputStr = file(filePath).read()
    primesStr = inputStr.split(' ')

    primes = []

    for p in primesStr:
        primes.append(ConvertStringToInt(p))

    return primes