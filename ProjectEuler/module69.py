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

    for n in range(2, 10**6+1):
        phi = GetNumberOfSmallerRelativePrimes(n)
        proportion = float(n)/float(phi)

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