from ArrayHelpers import *
from NumericalHelpers import *


def GenerateRotations(num):
    numArr = ConvertIntToIntArray(num)
    numArrLen = len(numArr)

    resArr = []

    for start in range(0, numArrLen):
        
        rotation = []
        for i in range(start, start + numArrLen):
            index = i % numArrLen
            rotation.append(numArr[index])

        retatedNum = ConvertIntArrayToInt(rotation)
        resArr.append(retatedNum)

    return resArr

def SolveProblem():
    results = []

    for num in range(2, 1000000):
        rotations = GenerateRotations(num)

        allPrimes = True
        for rotation in rotations:
            allPrimes &= IsPrime(rotation)
            if(not allPrimes):
                break

        if (allPrimes):
            print num
            results.append(num)



    print results
    print len(results)



