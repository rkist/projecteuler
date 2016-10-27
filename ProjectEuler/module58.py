from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *

north = (0,-1)
south = (0,1)
east = (1,0)
west = (-1,0)

def BuildMatrix(lateralSize):
    maxVal = lateralSize*lateralSize
    numbers = range(1,maxVal+1)

    margin = lateralSize/2 - 1

    matrix = [[0 for x in range(lateralSize)] for y in range(lateralSize)] 
    maxMatrixPosition = lateralSize-1
    matrixPosition = [lateralSize/2, lateralSize/2]

    direction = east

    for number in numbers:
        if (direction == east and matrixPosition[0] == maxMatrixPosition - margin):
            direction = north
        elif (direction == north and matrixPosition[1] == margin):
            direction = west
        if (direction == west and matrixPosition[0] == margin):
            direction = south
        elif (direction == south and matrixPosition[1] == maxMatrixPosition - margin):
            direction = east
            margin -= 1


        matrix[matrixPosition[0]][matrixPosition[1]] = number
        matrixPosition[0] += direction[0]
        matrixPosition[1] += direction[1]
    return matrix




def PrintMatrix(matrix):
    for j in range(len(matrix)):
        string = ""
        for i in range(len(matrix[j])):
            string += str(matrix[i][j]) + "\t"
        print string


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
    pCache.LoadCachedPrimesFromFile('cache/primes.1000000.txt')

    matrixSize = 107
    ratio = 1.0
    while (ratio > 0.1):
        matrix = BuildMatrix(matrixSize)
        ratio = CalculatePrimesRatioInDiagnals(matrix, pCache)

        PrintMatrix(matrix)
        break

        print str(matrixSize) + " : " + str(ratio)

        matrixSize += 500

    return matrixSize
