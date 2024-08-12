from ArrayHelpers import *
from NumericalHelpers import *


def IsTruncablePrime(num):
    if (not IsPrime(num)):
        return False
    numArr = ConvertIntToIntArray(num)
    for i in range(1, len(numArr)):
        arrLeft = numArr[i:]
        arrRight = numArr[:-i]
        numLeft = ConvertIntArrayToInt(arrLeft)
        numRight = ConvertIntArrayToInt(arrRight)
        if (not IsPrimeEXP(numLeft) or not  IsPrimeEXP(numRight)):
            return False
    return True





def SolveProblem():
    numSet = set()

    num = 10
    while (len(numSet) < 11):
        if (IsTruncablePrime(num)):
            print num
            numSet.add(num)
        num += 1
    
    return SumArray(numSet)



