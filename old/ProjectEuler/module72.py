from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *

LimitN = 10**6 + 1



def aaa(d):
    numUniqueFractions = 0;
    factors = Factorate(d)
    for n in xrange(1, d):
        go = 1
        for f in factors:
            if (n % f == 0):   
                go = 0
                break

        numUniqueFractions += go 
    
    if (d % 1000 == 0):
        print d, numUniqueFractions

    return numUniqueFractions



def SolveProblem():
    print __name__
   
    results = ParallelProcess(aaa, range(1, LimitN), 4)   #map
       
    return SumArrayValues(results) #reduce


#1000 303791
#2000 1215787
#3000 2735387
#4000 4862001
#5000 7598457
#6000 10941563
#7000 14892745
#8000 19452581
#9000 24619117
#10000 30393485
#11000 36778369