from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *


def CalculateSqrtContFraction(num):
    intSqr = SmallerIntSqrt(num)

    contFractions = _CalculateSqrtContFractionRecursion(num, intSqr, 1)







def _CalculateSqrtContFractionRecursion(sqrTerm, secondTerm, denominator):
    newDenominator = sqrTerm - secondTerm**2
    copyDenominator = denominator
    





def SolveProblem():
    print __name__

    for num in [23]:
        faction = CalculateSqrtContFraction(num)

       
    return -1