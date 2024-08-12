from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenerateSumsCombinations2(number):
    result = 0
    for n in range(1,number+1):
        result += GenerateSumsCombinationRecursion2(number, n, n)
    return result

combinationsCache = {}
def GenerateSumsCombinationRecursion2(finalSum, partialSum, lastAddedValue):
    k = (finalSum, partialSum, lastAddedValue)
    if (not combinationsCache.has_key(k)):
        sums = 0
        if (partialSum == finalSum):
            sums = 1
        else:            
            for n in xrange(lastAddedValue, finalSum - partialSum + 1):
                sums += GenerateSumsCombinationRecursion2(finalSum, partialSum + n, n)

        combinationsCache[k] = sums
    return combinationsCache[k]


pCache = {0:1, 1:1, 2:2, 3:3, 4:5, 5:7}
def p(n):
    if (n < 0):
        return 0

    if (not pCache.has_key(n)):       
        res = 0
        k = 1
        pent = 0
        while (pent < n):
            pent = PentagonalNumber(k)
            a = int((-1)**(k-1)) * p(n-pent)
            res += a
            k+=1
        
        k = 1
        pent = 0
        while (pent < n):
            pent = PentagonalNumber(-k)
            a = int((-1)**(-k-1)) * p(n-pent)
            res += a
            k+=1

        pCache[n] = res

    return pCache[n]


def SolveProblem():
    print __name__

    number = 1
    sums = p(number)

    while (sums % 1000000 != 0):
        number += 1 
        sums = p(number)
        #print number, sums

        
    return number