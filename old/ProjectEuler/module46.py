from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *

primeNumbers = []
oddCompositeNumbers = []

def StatisfyGoldbach(n):
    i = 0
    while (True):
        prime = primeNumbers[i]
        if (prime > n):
            break
        halfOfTheRest = (n - prime) / 2
        if (IntSqrt(halfOfTheRest) > 0):
            return True
        i += 1
    return False


def SolveProblem():
    for i in range(2,100000):
        if (IsPrime(i)):
            primeNumbers.append(i)
        elif (i % 2 == 1):
            oddCompositeNumbers.append(i)

    print primeNumbers
    print oddCompositeNumbers
   
    for num in oddCompositeNumbers:
        if (not StatisfyGoldbach(num)):
            return num

    return -1


