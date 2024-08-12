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

    print Step(145) == 145
    print Step(169) == 363601
    print Step(871) == 45361
    print Step(Step(871)) == 871
    print Step(Step(872)) == 872

    print FindLoop(145) == [145]
    print FindLoop(169) == [169, 363601, 1454]
    print FindLoop(871) == [871, 45361]
    print FindLoop(872) == [872, 45362]

    print FindLoop(69) == [69, 363600, 1454, 169, 363601]

    numOfSixtySized = 0
    for i in range(10**6):
        loopSize = len(FindLoop(i))
        if (loopSize == 60):
            numOfSixtySized += 1


    return numOfSixtySized

    
   
    #results = ParallelProcess(aaa, range(1, LimitN), 4)   #map       
    #return SumArrayValues(results) #reduce



#145
#363601
#45361
#871
#872