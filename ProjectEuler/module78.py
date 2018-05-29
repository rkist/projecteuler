from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenerateSumsCombinations2(number):
    result = 0
    for n in range(1,number+1):
        result += GenerateSumsCombinationRecursion2(number, n, n)
    return result

def GenerateSumsCombinationRecursion2(finalSum, partialSum, lastAddedValue):
    if (partialSum == finalSum):
        return 1

    sums = 0
    for n in range(lastAddedValue, finalSum - partialSum + 1):
        sums += GenerateSumsCombinationRecursion2(finalSum, partialSum + n, n)
    return sums


def SolveProblem():
    print __name__

    number = 5
    sums = GenerateSumsCombinations2(number)
    while (sums % 1000000 != 0):
        number += 1 
        sums = GenerateSumsCombinations2(number)
        print number, sums
        
    return number