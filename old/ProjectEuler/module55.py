from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *




def SolveProblem():
    print "."   

    lychrelCounter = 0

    for nOriginal in range(10000):
        n = nOriginal
        isLychrel = True
        for iteraction in range(50+1):
            nInv = InvertNumber(n)
            sum = n + nInv
            if (IsNumberPalindrome(sum)):
                print str(nOriginal) + " -> " + str(sum) + " (" + str(iteraction) + ")" + ": Not Lychrel"
                isLychrel = False
                break
            n = sum
        if (isLychrel):
            lychrelCounter += 1           


    return lychrelCounter