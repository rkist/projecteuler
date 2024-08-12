from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *


solveCache = [(1,1)]

def Solve(interaction):
    if (len(solveCache) > interaction):
        return solveCache[interaction]
    rn1 = Solve(interaction-1)
   
    nominator = rn1[0] + 2*rn1[1]
    denominator = rn1[0] + rn1[1]

    rn = (nominator, denominator)

    solveCache.append(rn)

    return rn


def SolveProblem():
    print "."   
    counter = 0

    for n in range(1000+1):
        nominator, denominator = Solve(n)
        nominatorArr = ConvertIntToIntArray(nominator)
        denominatorArr = ConvertIntToIntArray(denominator)
        if (len(nominatorArr) > len(denominatorArr)):
            counter += 1

    

    #print str(nominator) + '/' + str(denominator)

    return counter