from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *





from gmpy import *
#from utility import factor
#from __future__ import division

def phi(n):
    res = n
    Nfac = Factor(n)
    for f in Nfac:
        res = res*(1 - 1/f)
    return res





def SolveProblem():
    print __name__



    nums = []
    for n in range(2, 1000001):
        if is_prime(n): continue
        nums.append(n)

    prior = 0
    for item in nums:
        ph = phi(item)
        val = item/ph
        if val > prior:
            prior = val
            print item, ph, val

    #maxProportion = 0
    #maxProportionN = 0


    #for n in range(2, 10**3+1):
    #    phi = GetNumberOfSmallerRelativePrimes2(n)
    #    proportion = float(n)/float(phi)
    #    #relativePrimes = GetSmallerRelativePrimes(n)

    #    #print ("%s \t %s \t %s \t %s" % (n, phi, proportion, relativePrimes))

    #    if (proportion > maxProportion):
    #        print ("%s \t %s \t %s" % (n, phi, proportion))
    #        maxProportion = proportion
    #        maxProportionN = n

    #    if (n % 1000 == 0):
    #        print n

       
    return maxProportionN


#2   1   2.0
#6   2   3.0
#30   8   3.75
#210   48   4.375
#2310   480   4.8125