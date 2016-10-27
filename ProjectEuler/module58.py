from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *

from module28 import BuildMatrix, PrintMatrix

def CalculatePrimesRatioInDiagnals(matrix, primesCache):
    sum = 0
    pos = [0,0]
    lenght = len(matrix)

    totalNumbers = 2*lenght - 1
    totalPrimes = 0

    while (pos[0] < lenght):
        n = matrix[pos[0]][pos[1]]
        if (primesCache.IsPrime(n)):
            totalPrimes += 1
        pos[0] += 1
        pos[1] += 1

    pos = [0, lenght-1]
    while (pos[0] < lenght):
        n = matrix[pos[0]][pos[1]]
        if (primesCache.IsPrime(n)):
            totalPrimes += 1
        pos[0] += 1
        pos[1] -= 1

    return float(totalPrimes)/float(totalNumbers)


def SolveProblem():

    pCache = PrimesCache()

    pCache.LoadCachedPrimesFromFile('cache/primes.5000000.txt')


    matrixSize = 1007
    ratio = 1.0
    while (ratio > 0.1):
        matrix = BuildMatrix(matrixSize)
        #PrintMatrix(matrix)

        ratio = CalculatePrimesRatioInDiagnals(matrix, pCache)

        print str(matrixSize) + " : " + str(ratio)

        matrixSize += 500

    return matrixSize

    return -1