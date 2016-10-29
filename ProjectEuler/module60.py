from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *

def ConcatNums(num0, num1):
    num0Arr = ConvertIntToIntArray(num0)
    num1Arr = ConvertIntToIntArray(num1)
    newNumArr = num0Arr + num1Arr
    newNum = ConvertIntArrayToInt(newNumArr)
    return newNum

def TestProperty(primesCache, num0, num1):
    conc0 = ConcatNums(num0, num1)
    conc1 = ConcatNums(num1, num0)

    return primesCache.IsPrime(conc0) and primesCache.IsPrime(conc1)
           


def SolveProblem():
    print "."   

    primesCache = PrimesCache()
    primesCache.LoadCachedPrimesFromFile('cache/primes.10000.txt')

    numberOfPrimesWithProperty = 5

    pairsWithProperty = []

    for i in xrange(0, primesCache.PrimesLen):
        for j in xrange(i, primesCache.PrimesLen):
            p = (primesCache.Primes[i], primesCache.Primes[j])
            if (TestProperty(primesCache, p[0], p[1])):
                pairsWithProperty.append(p)
                

    
    graph = CreateGraph(primesCache.Primes, pairsWithProperty)

    clique = DetectClique(graph, numberOfPrimesWithProperty)

    sum = SumArray(clique)


    return sum