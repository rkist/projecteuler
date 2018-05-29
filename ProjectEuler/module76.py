from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *





def SolveProblem():
    print __name__

    number = 5

    sums = GenerateSumsCombinations(number)

    print sums
       
    return len(sums)