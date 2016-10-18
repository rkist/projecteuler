from NumericalHelpers import *
from FileHelpers import *

    

def CachePrimesUpTo(maxNum, filePath = 'cache/primes.txt'):
    with open(filePath, 'w') as f:
        for i in xrange(maxNum):
            if (IsPrime(i)):
                f.write(str(i) + ' ')

