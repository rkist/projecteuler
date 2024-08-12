from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *




def SolveProblem():
    print __name__

    propNumCounter = 0

    for n in range(1000):
        for p in range(30):
            num  = n**p
            numArr = ConvertIntToIntArray(num)
            numArrLen = len(numArr)

            if (numArrLen == p):
                propNumCounter += 1
                print str(n) + "**" + str(p) + " = " + str(num)

            


       
    return propNumCounter