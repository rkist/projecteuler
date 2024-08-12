from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *




def SolveProblem():
    factorsArray = []
    for i in range(0, 200000):
        factors = Factor(i)
        cleanFactors = RemoveDuplicatedItemsFromArray(factors)
        factorsArray.append((i, cleanFactors))

    print "."

    numOfRepetitions = 4
    for i in range(0,len(factorsArray) - numOfRepetitions):
        divisors = []
        for index in range(i, i + numOfRepetitions):
            (num, factors) = factorsArray[index]
            divisors += factors

        if (len(divisors) == numOfRepetitions*numOfRepetitions): #wrong because "a*a == (a+1) + (a-1) + (a-2)*a" , but it works for this problem
            return i



   
    return -1