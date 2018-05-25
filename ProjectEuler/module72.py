from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *

LimitN = 10**6 + 1



def SolveProblem():
    print __name__

    #factors = GetPrimesUpTo(LimitN)

    numUniqueFractions = 0;
    for d in xrange(1, LimitN):

        if (d % 1000 == 0):
            print d, numUniqueFractions

        factors = Factorate(d)

        for n in xrange(1, d):
            #ratio = float(n)/float(d)
            if (not CanSimplifyFractionWithPrimes(n,d, factors)):
                numUniqueFractions += 1       

       
    return numUniqueFractions


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