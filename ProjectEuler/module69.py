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

    print GetSmallerRelativePrimes(6)
    print GetSmallerRelativePrimes2(6)

    print GetSmallerRelativePrimes(12)
    print GetSmallerRelativePrimes2(12)

    
    print GetSmallerRelativePrimes(20)
    print GetSmallerRelativePrimes2(20)

    #for i in range(1,13):
    #    factors = Factorate(i)
    #    divisors = GetDivisors(i)


    #    print ("%s \t %s \t %s" % (i, factors, divisors))

    InitPrimesCache(1001)

    print GetSmallerRelativePrimes(6)
    print GetSmallerRelativePrimes2(6)

    for n in range(2, 10**3+1):
        phi = GetNumberOfSmallerRelativePrimes2(n)
        proportion = float(n)/float(phi)
        #relativePrimes = GetSmallerRelativePrimes(n)

        #print ("%s \t %s \t %s \t %s" % (n, phi, proportion, relativePrimes))

        if (proportion > maxProportion):
            print ("%s \t %s \t %s" % (n, phi, proportion))
            maxProportion = proportion
            maxProportionN = n

        if (n % 1000 == 0):
            print n

       
    return maxProportionN


#2   1   2.0
#6   2   3.0
#30   8   3.75
#210   48   4.375
#2310   480   4.8125