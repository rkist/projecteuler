from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def Step(value):
    valueArr = ConvertIntToIntArray(value)
    factorialSum = 0
    for n in valueArr:
        factorial = Factorial(n)
        factorialSum += factorial

    return factorialSum


def FindLoop(value):
    return FindLoopRecursion([value])

def FindLoopRecursion(valuesInLoop):
    newValue = Step(valuesInLoop[-1])

    if (newValue in valuesInLoop):
        return valuesInLoop
    
    valuesInLoop.append(newValue)
    return FindLoopRecursion(valuesInLoop)

def SolveProblem():
    print __name__

    numOfSixtySized = 0
    for i in range(10**6):
        loopSize = len(FindLoop(i))
        if (loopSize == 60):
            numOfSixtySized += 1


    return numOfSixtySized

    
   
    #results = ParallelProcess(aaa, range(1, LimitN), 4)   #map       
    #return SumArrayValues(results) #reduce
