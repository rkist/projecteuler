from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *




def SolveProblem():
    sum = 0
    for n in range(1,1000 + 1):
        sum += n**n

    intSumStr = str(int(sum))
    
    return intSumStr[-10:]