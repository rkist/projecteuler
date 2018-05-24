from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *

from sortedcollections import SortedDict

LimitN = 10**6 + 1

def Simplify(n,d):
    i = 2
    while(i <= n):
        if (n % i == 0 and d % i == 0):
            n /= i
            d /= i
        else:
            i += 1     

    return (n,d)



def SolveProblem():
    print __name__

    #orderedFractionsDic = SortedDict()

    #for d in range(1, LimitN):
    #    for n in range(1, d):
    #        ratio = float(n)/float(d)
    #        t = Simplify(n,d)   
    #        orderedFractionsDic[ratio] = t
           
    #for key, val in orderedFractionsDic.iteritems():
    #    print val, key


    tressetimos = float(3)/float(7)

    smallerDiff = 100000
    nForSmallerDiff = 0

    for d in range(1, LimitN):

        if (d % 1000 == 0):
            print d

        for n in range(int(d * tressetimos) - 1, int(d * tressetimos) + 1):
            ratio = float(n)/float(d)
            diff = tressetimos - ratio
            if (diff > 0 and abs(diff) < smallerDiff):
                smallerDiff = diff
                nForSmallerDiff = n
                
       
    return nForSmallerDiff