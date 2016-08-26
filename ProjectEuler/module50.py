from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *




def SolveProblem():
    print "."   

    primes = []
    for i in range (1,1000000):
        if (IsPrime(i)):
            primes.append(i)

    print "."   

    primesLen = len(primes)

    maxPrime = 0
    maxLen = 0
    for i in range(0, primesLen-1):
        for j in range(i+1, primesLen):
            subArrPrimes = primes[i:j]
            subArrPrimesLen = len(subArrPrimes)
            sum = SumArray(subArrPrimes)
            if (sum > primes[primesLen-1]):
                break
            if (IsInArray(primes, sum) and subArrPrimesLen > maxLen):
                maxPrime = sum
                maxLen = subArrPrimesLen
                print str(subArrPrimes) + "; " + str(subArrPrimesLen) + "; " + str(maxPrime) 

    return maxPrime