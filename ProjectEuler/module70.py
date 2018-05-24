from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *




def SolveProblem():
    print __name__

    #nThatSatisfyPermutabilityProperty = []

    minProportion = 1000000000
    nWithMinProportion = 0

    for n in xrange(2, 10000000) :
        factors = GetUniquePrimeFactors(n)
        dividend = n
        divisor = 1
        for factor in factors :
            dividend *= factor - 1
            divisor  *= factor         

        totient = dividend / divisor
        proportion = float(n) / float(totient)
        if  ArePermutations([n, totient]):
            #nThatSatisfyPermutabilityProperty.append((n, totient, proportion))
            if (proportion < minProportion):
                minProportion = proportion
                nWithMinProportion = n
                print n, totient, proportion


    #for  n, totient, proportion in nThatSatisfyPermutabilityProperty:
    #    if (proportion < minProportion):
    #        minProportion = proportion
    #        nWithMinProportion = n

       
    return nWithMinProportion
