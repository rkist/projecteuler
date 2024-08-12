from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *


def SolveProblem():
    print "."   
    numCounter = 0

    for n in range(100+1):
        for r in range(n):
            c = C(n,r)
            if (c > 1000000):
                numCounter += 1


    return numCounter