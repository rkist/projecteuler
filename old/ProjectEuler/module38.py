from ArrayHelpers import *
from NumericalHelpers import *


def IsPandigital(arr):
    if (len(arr) != 9):
        return False

    for i in range(1,10):
        hasIt = False
        for n in arr:
            if (i == n):
                hasIt = True
                break
        if (not hasIt):
            return False
    return True



def SolveProblem():
    maxPan = 0

    for n in range(1,100000):
        concat = []
        for m in range(1,10):
            mult = n * m
            concat += ConvertIntToIntArray(mult)
            if (IsPandigital(concat)):
                maxPan = ConvertIntArrayToInt(concat)
                print maxPan
            if (len(concat) > 9):
                break
    return maxPan



    
