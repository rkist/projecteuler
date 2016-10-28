from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *




def SolveProblem():
    print "."   

    pCache = PrimesCache()
    pCache.LoadCachedPrimesFromFile('cache/primes.1000.txt')

    numberOfPrimesWithProperty = 4

    print len(pCache.Primes)


    return -1