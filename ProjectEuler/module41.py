from ArrayHelpers import *
from NumericalHelpers import *





def SolveProblem():
    maxPanPrime = 0
    arr = []
    for i in range(1,10):
        arr += ConvertIntToIntArray(i) 
        arrPerm = Permute(arr)     

        for perm in arrPerm:
            permNum = ConvertIntArrayToInt(perm)
            if (IsPrime(permNum) and permNum > maxPanPrime):
                print permNum
                maxPanPrime = permNum

    return maxPanPrime