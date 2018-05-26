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
    pass

def SolveProblem():
    print __name__

    print Step(145)
    print Step(169)
    print Step(871)
    print Step(Step(871))
    print Step(Step(872))

    return -1

    
   
    #results = ParallelProcess(aaa, range(1, LimitN), 4)   #map       
    #return SumArrayValues(results) #reduce



#145
#363601
#45361
#871
#872