from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *


def HashPermutation(num):
    numArr = ConvertIntToIntArray(num)
    orderedArr = [0,0,0,0,0,0,0,0,0,0] #10 alg

    for n in numArr:
        orderedArr[n] += 1

    oederedHash = ConvertIntArrayToInt(orderedArr)

    return oederedHash


def SolveProblem():
    print __name__
       
    permSetSize = 5

    cubicPermutationDictionary = dict()

    for n in range(10000):
        nCube = n**3
        cubicPermHash = HashPermutation(nCube)
        if cubicPermHash not in cubicPermutationDictionary:
            cubicPermutationDictionary[cubicPermHash] = []
        cubicPermutationDictionary[cubicPermHash].append(n)

        if (len(cubicPermutationDictionary[cubicPermHash]) == permSetSize):
            print cubicPermutationDictionary[cubicPermHash]
            return cubicPermutationDictionary[cubicPermHash][0]**3




    return -1