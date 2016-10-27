import ArrayHelpers
import NumericalHelpers
from FileHelpers import *

class PrimesCache:
    def CachePrimesInFileUpTo(self, maxNum, filePath = 'cache/primes.txt'):
        with open(filePath, 'w') as f:
            for i in xrange(maxNum):
                if (NumericalHelpers.IsPrime(i)):
                    f.write(str(i) + ' ')

    def LoadCachedPrimesFromFile(self, filePath = 'cache/primes.txt'):
        inputStr = file(filePath).read()
        primesStr = inputStr.split(' ')

        primes = []

        for p in primesStr:
            primes.append(ArrayHelpers.ConvertStringToInt(p))

        self.Primes = primes
        self.HigherPrime = primes[-1]

        return primes

    def _IsPrimeWithCache(self, value):
        if (value < 2):
            return False
        for divisor in self.Primes:
            if (value != divisor) and (value % divisor == 0):
                return False
        return True

    def IsPrime(self, num):
        if (num <= self.HigherPrime):
            return ArrayHelpers.IsInArray(self.Primes, num)
        elif (num < self.HigherPrime**2):
            return  self._IsPrimeWithCache(num)
        else:
            return NumericalHelpers.IsPrime(num)
