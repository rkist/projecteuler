from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenerateSumsCombinations2(number):
    result = 0
    for n in range(1,number):
        result += GenerateSumsCombinationRecursion2(number, [n], n)
    return result

def GenerateSumsCombinationRecursion2(finalSum, partialArray, lastAddedValue):
    partialSum = SumArrayValues(partialArray)
    if (partialSum == finalSum):
        return len([partialArray])

    sums = 0
    for n in range(lastAddedValue, finalSum - partialSum + 1):
        newPartialArray = partialArray + [n]
        sums += GenerateSumsCombinationRecursion2(finalSum, newPartialArray, n)
    return sums


def SolveProblem():
    print __name__

    
    for n in range(1,20):
        print len(GenerateSumsCombinations(n))

    number = 100
    sums = GenerateSumsCombinations2(number)
    #print sums
       
    return sums