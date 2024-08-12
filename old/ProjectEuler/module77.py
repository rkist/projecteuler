from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenerateSumsCombinations2(number):
    result = 0
    for n in GetPrimesUpTo(number):
        result += GenerateSumsCombinationRecursion2(number, n, n)
    return result

def GenerateSumsCombinationRecursion2(finalSum, partialSum, lastAddedValue):
    if (partialSum == finalSum):
        return 1

    sums = 0
    for n in GetPrimesInRange(range(lastAddedValue, finalSum - partialSum + 1)):
        sums += GenerateSumsCombinationRecursion2(finalSum, partialSum + n, n)
    return sums


def SolveProblem():
    print __name__

    number = 5
   
    sums = 0
    while (sums < 5000):   
        number += 1
        sums = GenerateSumsCombinations2(number)
        print number, sums   
       
    return number