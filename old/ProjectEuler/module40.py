from ArrayHelpers import *
from NumericalHelpers import *

def GenerateProblemArray():
    arr = []
    arrLen = 0
    num = 1
    while (arrLen < 1000001):
        numArr = ConvertIntToIntArray(num)
        arr += numArr
        num += 1
        arrLen += len(numArr)
    return arr





def SolveProblem():
    arr = GenerateProblemArray()
    print len(arr)
    res = arr[1-1] * arr[10-1] * arr[100-1] * arr[1000-1] * arr[10000-1] * arr[100000-1] * arr[1000000-1]
    return res