from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def SolveProblem():
    print __name__

    maxProportion = 0
    maxProportionN = 0

    for n in xrange(2, 1000000) :
        factors = GetUniquePrimeFactors(n)
        dividend = n
        divisor = 1
        for factor in factors :
            dividend *= factor - 1
            divisor  *= factor
        
        totient = dividend / divisor
        proportion = float(n) / float(totient)
        if  maxProportion < proportion :
            maxProportion = proportion
            maxProportionN = n
            print n, totient, proportion
       
    return maxProportionN


#2   1   2.0
#6   2   3.0
#30   8   3.75
#210   48   4.375
#2310   480   4.8125