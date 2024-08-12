from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *

north = (0,-1)
south = (0,1)
east = (1,0)
west = (-1,0)

def CalculateBuildMatrixRatio(primesCache):
    ratio = 1.0
    lateralSize = 30001
     
    totalPrimes = 0

    maxVal = lateralSize*lateralSize
    margin = lateralSize/2 - 1

    #matrix = [[0 for x in range(lateralSize)] for y in range(lateralSize)] 
    maxMatrixPosition = lateralSize-1
    matrixPosition = [lateralSize/2, lateralSize/2]

    direction = east

    for number in xrange(1,maxVal+1):
        if (direction == east and matrixPosition[0] == maxMatrixPosition - margin):
            if (primesCache.IsPrime(number)):
                totalPrimes += 1
            direction = north
        elif (direction == north and matrixPosition[1] == margin):
            if (primesCache.IsPrime(number)):
                totalPrimes += 1
            direction = west
        if (direction == west and matrixPosition[0] == margin):
            if (primesCache.IsPrime(number)):
                totalPrimes += 1
            direction = south
        elif (direction == south and matrixPosition[1] == maxMatrixPosition - margin):
            if (primesCache.IsPrime(number)):
                totalPrimes += 1
            direction = east

            currSize = lateralSize-2*margin
            totalNumbers = 2*(currSize) - 1
            ratio = float(totalPrimes)/float(totalNumbers)
            print str(currSize) + ' : ' + str(ratio)

            if (ratio < 0.1):
                return currSize

            margin -= 1


        #matrix[matrixPosition[0]][matrixPosition[1]] = number
        matrixPosition[0] += direction[0]
        matrixPosition[1] += direction[1]          

    return -1


def PrintMatrix(matrix):
    for j in range(len(matrix)):
        string = ""
        for i in range(len(matrix[j])):
            string += str(matrix[i][j]) + "\t"
        print string


def SolveProblem():
    pCache = PrimesCache()
    pCache.LoadCachedPrimesFromFile('cache/primes.20000000.txt')

    matrixSize = CalculateBuildMatrixRatio(pCache)

    return matrixSize
