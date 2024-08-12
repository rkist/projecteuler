from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *


def SolveProblem():
    print "."

    arr = []
    for n in range(1000,9999+1):
       if (IsPrime(n)):
           arr.append(n)

    print "."

    arrSecondFilter = []
    arrLen = len(arr)
    for i in range(0, arrLen-2):
        for j in range(i+1, arrLen-1):
            t1 = arr[i]
            t2 = arr[j]
            diff = t2 - t1
            possibleNext = t2 + diff
            if (IsInArray(arr, possibleNext)):
                arrSecondFilter += [(t1, t2, possibleNext)]

    print "."
    
    arrThirdFilter = []
    for item in arrSecondFilter:
        if (ArePermutations(item)):
            print item
            arrThirdFilter.append(item)

    return arrThirdFilter