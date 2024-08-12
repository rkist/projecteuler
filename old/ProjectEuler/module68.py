from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


NumOfGons = 5
PossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def GetRemainingValues(perm):
    remainingValues = []
    for val in PossibleValues:
        if (val not in perm):
            remainingValues.append(val)
    return remainingValues

def FormDescriptionArray(trianglePermutation, externalPermutation):
    descriptionArray = [-1,] * NumOfGons
    for i in range(NumOfGons):
        descriptionArray[i] = (externalPermutation[i], trianglePermutation[i-1], trianglePermutation[i])

    return descriptionArray

def TestMagicalTotal(descriptionArray, total):
    for gon in descriptionArray:
        if (SumArrayValues(gon) != total):
            return False
    return True

def TestRightRotation(descriptionArray):
    firstGon = descriptionArray[0]
    for gon in descriptionArray[1:]:
        if (firstGon[0] > gon[0]):
            return False
    return True

def CreateStringFromDescriptionArray(descriptionArray):
    descriptionArrayStr = ''
    for gon in descriptionArray:
        for n in gon:
            descriptionArrayStr += str(n) 
    return descriptionArrayStr


def SolveProblem():
    print __name__

    totals = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    solutions = []
    descriptionArrays = []

    trianglePermutations = Permute(PossibleValues, NumOfGons)  

    
    for trianglePermutation in trianglePermutations:
        #print trianglePermutation
        
        remainingValues = GetRemainingValues(trianglePermutation)       
        externalPermutations = Permute(remainingValues)

        for externalPermutation in externalPermutations:
            #print "\t" + str(externalPermutation)

            descriptionArray = FormDescriptionArray(trianglePermutation, externalPermutation)

            descriptionArrays.append(descriptionArray)

            #print "\t=" + str(descriptionArray)

    for total in totals:
        for descriptionArray in descriptionArrays:
            matchesTotal = TestMagicalTotal(descriptionArray, total)
            isRightRotation = TestRightRotation(descriptionArray)
            
            if (matchesTotal and isRightRotation):
                solutions.append(descriptionArray)                    
                print str(total) + "\t" + str(descriptionArray) 
       
    maxSolution16 = 0
    maxSolution17 = 0
    for solution in solutions:
        solutionStr = CreateStringFromDescriptionArray(solution)
        solutionInt = int(solutionStr)

        if (len(solutionStr) == 16):
            if solutionInt > maxSolution16:
                maxSolution16 = solutionInt

        if (len(solutionStr) == 17):
            if solutionInt > maxSolution17:
                maxSolution17 = solutionInt


    return maxSolution16


#9	4,2,3; 5,3,1; 6,1,2
#9	4,3,2; 6,2,1; 5,1,3
#10	2,3,5; 4,5,1; 6,1,3
#10	2,5,3; 6,3,1; 4,1,5
#11	1,4,6; 3,6,2; 5,2,4
#11	1,6,4; 5,4,2; 3,2,6
#12	1,5,6; 2,6,4; 3,4,5
#12	1,6,5; 3,5,4; 2,4,6